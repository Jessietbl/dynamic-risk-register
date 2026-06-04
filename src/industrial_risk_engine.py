
class AssetRiskEngine:
    def __init__(self, asset_type):
        self.asset_type = asset_type

    def calculate_base_risk(self, likelihood, consequence):
        return likelihood * consequence

    def calculate_dynamic_risk(
        self,
        likelihood,
        consequence,
        alarm_score,
        inspection_score,
        maintenance_score
    ):
        base_risk = self.calculate_base_risk(likelihood, consequence)

        signal_multiplier = 1 + (
            0.4 * alarm_score +
            0.3 * inspection_score +
            0.3 * maintenance_score
        )

        return round(base_risk * signal_multiplier, 2)

    def classify_risk_level(self, risk_score):
        if risk_score >= 18:
            return "Critical"
        elif risk_score >= 12:
            return "High"
        elif risk_score >= 6:
            return "Medium"
        return "Low"
