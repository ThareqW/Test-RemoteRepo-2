"""
Very advanced Employee management system.
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional


class contract_employee(ABC):

    @abstractmethod
    def get_payment(self) -> float:
        pass


class commission(ABC):

    @abstractmethod
    def get_payment(self) -> float:
        pass


@dataclass
class ContractCommission(commission):
    commission: float = 100
    contracts_landed: int = 0

    def get_payment(self) -> float:
        return self.commission * self.contracts_landed


@dataclass
class Employee:
    name: str
    id: int
    contract: contract_employee
    commission: Optional[ContractCommission] = None

    def compute_pay(self):
        check = self.contract.get_payment()
        if self.commission is not None:
            check += self.commission.get_payment()

        return check


@dataclass
class HourlyEmployee(contract_employee):
    """Employee that's paid based on number of worked hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.pay_rate * self.hours_worked
            + self.employer_cost
        )


@dataclass
class SalariedEmployee(contract_employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 0
    percentage: float = 1

    def get_payment(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.monthly_salary * self.percentage
        )


@dataclass
class Freelancer:
    """Freelancer that's paid based on number of worked hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def get_payment(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.pay_rate * self.hours_worked
        )


def main() -> None:
    """Main function."""

    henry_contract = HourlyEmployee(pay_rate=50, hours_worked=100)
    henry = Employee(name = "Henry", id = 14568, contract = henry_contract)

    print(
        f"{henry.name} worked for {henry_contract.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah_contract = SalariedEmployee(monthly_salary=5000)
    sarah_commission = ContractCommission(contracts_landed = 8)
    sarah = Employee(name = "Sarah", id = 14569, contract = sarah_contract, commission = sarah_commission)

    print(
        f"{sarah.name} landed {sarah_commission.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()
