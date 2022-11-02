from collections import Counter


class TrackOrders:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def add_new_order(self, customer, order, day):
        order = [customer, order, day]
        self.list.append(order)

    def get_most_ordered_dish_per_customer(self, customer):
        allorders = []
        for order in self.list:
            if order[0] == customer:
                allorders.append(order[1])
        return (Counter(allorders)).most_common()[0][0]

    def get_never_ordered_per_customer(self, customer):
        all_items = {'hamburguer', 'pizza', 'coxinha', 'misto-quente'}
        for order in self.list:
            if order[0] == customer:
                if order[1] in all_items:
                    all_items.remove(order[1])
        return all_items

    def get_days_never_visited_per_customer(self, customer):
        all_days = {'segunda-feira', 'terça-feira', 'sabado'}
        for order in self.list:
            if order[0] == customer:
                if order[2] in all_days:
                    all_days.remove(order[2])
        return all_days

    def get_busiest_day(self):
        all_days = []
        for order in self.list:
            all_days.append(order[2])
        return (Counter(all_days)).most_common()[0][0]

    def get_least_busy_day(self):
        all_days = []
        for order in self.list:
            all_days.append(order[2])
        return (Counter(all_days)).most_common()[-1][0]
