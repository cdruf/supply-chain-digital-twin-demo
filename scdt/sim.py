from datetime import date, timedelta

import simpy as sp
from nodes import Network


class Env:
    def __init__(self, start_date: date, network: Network,
                 log=True, out=True):
        self.env = sp.Environment()
        self.start_date = start_date
        print(f"Start date: {start_date}")
        self.network = network
        self.log = log
        self.out = out

    def date_to_simtime(self, date: date):
        return (date - self.start_date).days

    def simtime_to_date(self, t):
        return self.start_date + timedelta(days=t)

    def current_date(self):
        return self.simtime_to_date(self.env.now)

    def init(self):
        print("Schedule demand processes")
        # Schedule demand processes
        for dn in network.demand_nodes:
            for d in dn.demands:
                self.env.process(d.demand_process.process(self))

    def print(self, str: str):
        if self.out:
            print(f"{self.current_date()}:\t {str}")


if __name__ == "__main__":
    print("Hi")
    start_date = date.today()
    network = Network.get_test_instance(start_date)
    env = Env(start_date, network)
    env.init()

    env.env.run(until=365 * 5)
    print(f"Final date: {env.current_date()}")
