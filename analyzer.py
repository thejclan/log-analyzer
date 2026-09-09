FAILED_LOGIN_THRESHOLD = 3

success_count = 0
failed_count = 0
failed_users = {}

with open("log.txt", "r") as file:
    for line in file:
        parts = line.strip().split()

        status = parts[2]
        user = parts[3]

        if status == "LOGIN_SUCCESS":
            success_count += 1

        elif status == "LOGIN_FAILED":
            failed_count += 1

            if user not in failed_users:
                failed_users[user] = 0

            failed_users[user] += 1


print(f"Login success: {success_count}")
print(f"Login failed: {failed_count}")

print("\nWarning:")

for user, count in failed_users.items():
    if count >= FAILED_LOGIN_THRESHOLD:
        print(f"{user} has {count} failed login attempts")
