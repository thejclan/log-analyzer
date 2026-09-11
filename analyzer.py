FAILED_LOGIN_THRESHOLD = 3

success_count = 0
failed_count = 0
failed_users = {}
failed_ips = {}

with open("log.txt", "r") as file:
    for line in file:
        parts = line.strip().split()

        status = parts[2]
        user = parts[3]
        ip = parts[4]

        if status == "LOGIN_SUCCESS":
            success_count += 1

        elif status == "LOGIN_FAILED":
            failed_count += 1

            if user not in failed_users:
                failed_users[user] = 0

            if ip not in failed_ips:
                failed_ips[ip] = 0

            failed_users[user] += 1
            failed_ips[ip] += 1


print(f"Login success: {success_count}")
print(f"Login failed: {failed_count}")
print(f"Unique failed users: {len(failed_users)}")
print(f"Unique failed IPs: {len(failed_ips)}")

print("\nWarning - Users:")

for user, count in failed_users.items():
    if count >= FAILED_LOGIN_THRESHOLD:
        print(f"{user} has {count} failed login attempts")

print("\nWarning - IPs:")

for ip, count in failed_ips.items():
    if count >= FAILED_LOGIN_THRESHOLD:
        print(f"{ip} has {count} failed login attempts")
