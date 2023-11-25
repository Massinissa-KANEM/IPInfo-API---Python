from ipinfo import IPInfoRes

def main():
    api_token = '39163d78747e6c'
    ip = IPInfoRes(api_token)

    ip_address = input("Entrez une adresse IP (laissez vide pour votre propre IP): ").strip()

    if not ip_address:
        ip_address = ip.get_ipinfo().get('ip')

    valides = ["ip", "hostname", "city", "region", "country", "loc", "org", "postal", "timezone"]
    print("Liste des informations : " + ", ".join(valides))

    while True:
        user_choices_input = input("Entrez les informations que vous souhaitez afficher, séparées par des virgules ou \"all\" pour tout afficher : ").strip().lower()

        if user_choices_input == "all":
            user_choices = "all"
            break
        else:
            user_choices = [choice.strip() for choice in user_choices_input.split(',')]

            if all(choice in valides for choice in user_choices):
                break
            else:
                print("Choix invalide, veuillez réessayer.")

    ip_info = ip.get_ipinfo(ip_address)

    if ip_info:
        print("Informations sur l'adresse IP :")

        if user_choices == "all":
            for key, value in ip_info.items():
                print(f"{key}: {value}")
        else:
            for choice in user_choices:
                value = ip_info.get(choice)
                if value is not None:
                    print(f"{choice}: {value}")
                        
    else:
        print("Impossible de récupérer les informations de l'adresse IP.")

if __name__ == "__main__":
    main()
