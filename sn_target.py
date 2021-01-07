import sys,os,shodan


p = sys.platform.lower()

if 'win' in p:
	os.system("cls")
else:
	os.system("clear")
	

print("<$> Creted By Special_Esmit")
print("<$> Sponsor: Zero Security Team | https://t.me/zero_security_tm")
print("<^> Just For Fun :)\n")

api_key = str(input("<^> Enter Your API_KEY: "))
api = shodan.Shodan(api_key)

if len(sys.argv) < 2:
	target_ip = str(input("<^> Enter Target IP: "))
else:
	target_ip = sys.argv[1]

try:
	data = api.host(target_ip)
	print("<^> Request Sent !\n\n\n")
	print("<^> Your Target: " + str(data["ip_str"]) + "\n<^>Ports: " + str(data["ports"]) + "\n<^>Country Name: " + str(data["country_name"]) + "\n<^>Country Code: " + str(data["country_code"]) + "\n<^> City: " + str(data["city"]) + "\n<^>Postal Code: " + str(data["postal_code"]) + "\n<^>ORG: " + str(data["org"]) + "\n<^>Area Code: " + str(data["area_code"]) + "\n<^>ISP: " + str(data["isp"]) + "\n<^>Domains: " + str(data["domains"]) + "\n<^>Hostnames: " + str(data["hostnames"]) + "\n<^>ASN: " + str(data["asn"]) +"\n<^>os: " + str(data["os"]))
	try:
		print("\n<^>Vulns: " + str(data["vulns"]))
	except:
		print("<^> Target is Good :)")
	x = str(input("Show Datas?(y,n): "))
	if x == 'y':
		print(data["data"])
	else:
		print("<^> by by")	
except:
	print("<!> Error ")
