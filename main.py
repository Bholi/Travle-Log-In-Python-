travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]


def add_new_country(country, visits, cities):
    travel_log.append({'country': country, 'cities_visited': cities, 'total_visits': visits})


add_new_country("Russia", 2, ['Moscow', 'Sain Peter'])
print(travel_log)
