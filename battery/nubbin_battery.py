from battery import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super.__init__()
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.current_date - self.last_service_date > 1460