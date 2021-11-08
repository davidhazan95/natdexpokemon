from ..config import getnatdex
def add_ability(ability_name,ability_description):
    if __name__ == "__main__":    
        
        # Get the database
        dbname = getnatdex.get_database()
        
        collection_name = dbname["ability"]
        ability = {
        "ability_name" : ability_name,
        "ability_description" : ability_description
        }
        collection_name.insert_one(ability)
add_ability("Aftermath","Damages the attacker if it contacts the Pokémon with a finishing hit.")