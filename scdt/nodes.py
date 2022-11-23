import numpy as np

from util.distance_helper import haversine_km


class SKU:
    """Stock keeping unit. """
    next_id = 0

    def __init__(self):
        self.id = SKU.next_id
        SKU.next_id += 1


class Location:
    """Lat/lon-pair."""

    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

    def haversine_km(self, other):
        return haversine_km(self.lat, self.lon, other.lat, other.lon)


class Node:
    next_id = 0

    def __init__(self, name, location):
        self.id = Node.next_id
        Node.next_id += 1
        self.name = name
        self.location = location


class Supplier(Node):

    def __init__(self, name, location):
        super().__init__(name, location)


class Warehouse(Node):

    def __init__(self, name, location):
        super().__init__(name, location)


class ProductionSite(Node):

    def __init__(self, name, location):
        super().__init__(name, location)


class DemandNode(Node):

    def __init__(self, name, location):
        super().__init__(name, location)
        self.demands = []


class Demand:
    def __init__(self, sku: SKU, sampling):
        self.sku = sku
        # history can be used to forecast
        self.historic_dates = []
        self.historic_quantities = []
        # TODO: sampling


class Production:
    """Processing raw materials to products."""

    def __init__(self, product, batch_size, setup_time, processing_time_unit):
        self.input_materials = []
        self.input_quantities = []
        self.product = product
        self.batch_size = batch_size
        self.setup_time = setup_time
        self.processing_time_unit = processing_time_unit
        self.lines = []


class ProductionLine:
    next_id = 0

    def __init__(self, production_site):
        self.id = ProductionLine.next_id
        ProductionLine.next_id += 1
        self.production_site = production_site


class Network:
    @classmethod
    def get_test_instance(cls):
        skus = []
        suppliers = [Supplier("SP_A", Location(19.43, -99.13)),
                     Supplier("SP_B"), Location(-25.26, -57.58)]
        site_medellin = Location(6.2, -75.6)
        site_bogota = Location(4.7, -74.1)
        warehouses = [Warehouse("WH_MDL", site_medellin),
                      Warehouse("WH_BGT", site_bogota)]
        production_sites = [ProductionSite("MFG_MDL", site_medellin),
                            ProductionSite("MFG_BGT", site_bogota)]
        demand_nodes = [DemandNode(f"DM_{i},{j}", Location(i, j))
                        for i in np.linspace(1, 30, 10)
                        for j in np.linspace(-90, -70, 10)]
        for dn in demand_nodes:
            for sku in skus:
                demand_nodes.demands.append(Demand(sku, None))
        return Network(suppliers, warehouses, production_sites, demand_nodes)

    def __init__(self, suppliers, warehouses, production_sites, demand_nodes):
        self.suppliers = suppliers
        self.warehouses = warehouses
        self.production_sites = production_sites
        self.demand_nodes = demand_nodes
