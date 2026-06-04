def calculate_dynamic_risk(likelihood, consequence, alarm_score, inspection_score, maintenance_score):
    base_risk = likelihood * consequence
    signal_multiplier = 1 + (0.4 * alarm_score + 0.3 * inspection_score + 0.3 * maintenance_score)
    return round(base_risk * signal_multiplier, 2)


example = calculate_dynamic_risk(
    likelihood=4,
    consequence=5,
    alarm_score=0.8,
    inspection_score=0.6,
    maintenance_score=0.7
)

print(f"Dynamic Risk Score: {example}")
