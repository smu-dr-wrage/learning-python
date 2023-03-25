from textfsm import TextFSM


def main():
    # template_path: str = 'templates/netscaler-add-server.textfsm'
    # template_path: str = 'templates/netscaler-add-service.textfsm'
    template_path: str = 'templates/netscaler-add-gslb-vserver.textfsm'
    config_path: str = 'data/lb-config.txt'

    config: str
    with open(config_path) as cf:
        config = "\r\n".join(cf.readlines())

    fsm: TextFSM
    parsed_text: list
    with open(template_path) as tf:
        fsm = TextFSM(tf)
        parsed_text = fsm.ParseTextToDicts(config)

    headers: list = fsm.header
    print(f"Headers: {headers}")
    print(f"Number of records: {len(parsed_text)}")

    for element in parsed_text[:15]:
        print(element)


if __name__ == '__main__':
    main()
