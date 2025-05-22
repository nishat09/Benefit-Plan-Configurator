class BenefitPlan:
    def __init__(self, name, deductible, copay, coverage):
        self.name = name
        self.deductible = deductible
        self.copay = copay
        self.coverage = coverage  # e.g., {"Dental": 80, "Vision": 50}

    def validate(self):
        errors = []

        if not self.name.strip():
            errors.append("Plan name is required.")
        if self.deductible is None or not isinstance(self.deductible, (int, float)) or self.deductible < 0:
            errors.append("Deductible must be a non-negative number.")
        if self.copay is None or not isinstance(self.copay, (int, float)) or self.copay < 0:
            errors.append("Copay must be a non-negative number.")
        if not isinstance(self.coverage, dict) or not self.coverage:
            errors.append("Coverage must be defined as a dictionary with at least one service.")
        else:
            for service, percent in self.coverage.items():
                if not (0 <= percent <= 100):
                    errors.append(f"Invalid coverage percent for '{service}': {percent}%")

        return errors

    def summary(self):
        return {
            "Plan Name": self.name,
            "Deductible": f"${self.deductible}",
            "Copay": f"${self.copay}",
            "Coverage": self.coverage
        }

if __name__ == "__main__":
    print("[*] Simulating Benefit Plan Configuration...\n")

    plan = BenefitPlan(
        name="GoldCare",
        deductible=500,
        copay=20,
        coverage={"Dental": 80, "Vision": 50, "General": 100}
    )

    errors = plan.validate()

    if errors:
        print("❌ Validation Errors:")
        for err in errors:
            print(f" - {err}")
    else:
        print("Plan configured successfully.\nSummary:")

        summary = plan.summary()
        for k, v in summary.items():
            print(f"{k}: {v}")
