import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Навчальні дані
data = {
    "commits": [2, 3, 10, 12, 5, 15, 1, 20, 8, 18,
                4, 11, 7, 16, 6, 14, 9, 13, 2, 19],
    "test_failures": [0, 0, 3, 4, 1, 5, 0, 6, 2, 5,
                      0, 3, 1, 4, 1, 4, 2, 3, 0, 6],
    "review_delay": [1, 2, 8, 10, 3, 12, 1, 15, 5, 11,
                     2, 9, 4, 13, 3, 10, 6, 8, 1, 14],
    "build_failed": [0, 0, 1, 1, 0, 1, 0, 1, 0, 1,
                     0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["commits", "test_failures", "review_delay"]]
y = df["build_failed"]

# Навчання моделі
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Нові показники проєкту
new_data = pd.DataFrame(
    [[12, 4, 9]],
    columns=["commits", "test_failures", "review_delay"]
)

# Прогноз
risk = model.predict_proba(new_data)[0][1] * 100

print(f"Build failure risk: {risk:.2f}%")

if risk >= 50:
    print("Recommendation: High risk. Run all tests.")
else:
    print("Recommendation: Low risk. Standard testing is sufficient.")