controller='devnetapi.cisco.com/sandbox/apic.em'
create_ticket= __input__("create_ticket")
def getconnecthosts(ticket):
    t=ticket['response']['serviceticket']
    print(t)
    url = "https://" + controller + "/api/v1/host?limit=1&offset=1"
    header = {"content-type": "application/json", "X-Auth-Token":ticket}
    response = requests.get(url, headers=header, verify=False)

getconnecthosts(tickets)
