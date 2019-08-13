import mongoengine
import infrastructure.state as state

def global_init(): 
    state.active_account = None
    mongoengine.register_connection(alias='core4',name='CatCageRentalApp')
    """I removed host and port."""
