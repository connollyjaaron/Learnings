class Strategy():
    def __init__(self, kind):
        self.kind = kind


class ContractAggregate():
    def __init__(self, contracts):
        self.contracts = contracts
        self.entry_credit = self.calculate_entry_credit

    def calculate_entry_credit(self):
        return None


class Contract():
    def __init__(self, expiration: float, bid_price: dict, ask_price: dict, strategy_name: str):
        """

        :param expiration: a date or iso string
        :param bid_price: {'short call': value, 'short put': value}
        :param ask_price: {'long call': value, 'long put': value}
        :param strategy_name: str from Strategy
        """
        self.expiration = expiration
        self.bid_price = bid_price
        self.ask_price = ask_price
        self.strategy_name = strategy_name
        self.max_risk = self.calculate_max_risk()
        self.max_return_on_risk = self.calculate_max_return_on_risk()
        self.break_even = self.calculate_break_even()
        self.prob_of_profit = self.calculate_prob_of_profit()
        self.credits_debits = self.calculate_credits_debits()

    def calculate_credits_debits(self):
            return {'short call': None, 'short put': None, 'long call': None, 'long put': None}

    def calculate_max_risk(self):
        return None

    def calculate_max_return_on_risk(self):
        return None

    def calculate_break_even(self):
        # condition on strategy type
        # try to abstract those conditions into their own functions
        return {'high':None, 'low': None}

    def calculate_prob_of_profit(self):
        return None


class Security():
    def __init__(self, ticker: str, contracts: list, underlying_price: float,
                 dividend: float, historical_price: dict):
        """

        :param contracts: list of Contract (object)
        :param underlying_price: the price of the security (float)
        :param dividend: the dividend of the security (float)
        :param historical_prices: list of date, price dictionaries [{'date': 'yyyy-mm-dd', 'price': float}, ...]
        """
        self.ticker = ticker
        self.contracts = contracts
        self.underlying_price = underlying_price
        self.dividend = dividend
        self.volatility = self.calculate_volatility()
        self.historical_price = historical_price

    def calculate_volatility(self):
        """
        standard deviation of historical prices
        :return:
        """
        return None

def contract_recomender(list_of_aggregate_contracts):
    # list of aggregate contracts objects
    # analyze them against one another
    # we are comparing contracts to contracts here
    # return best combination of contracts (return best aggregate_contract object for that security)
    return None

def security_recomender(list_of_securities):
    # list of Security objects
        # each of those has a list of contracts
    # loop each security
        # run contracts through contract recomender

    # perform aggregate analysis based on results of contract recomender
        # here we are comparing securities
    return None
