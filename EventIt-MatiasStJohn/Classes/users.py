from abc import ABC


class Usuario(ABC):
    def __init__(self, username, password):
        self.password = password
        self.username = username
        self.notificaciones = []

class Ciudadano(Usuario):
    def __init__(self, username, password, CUIL, telefono):
        Usuario.__init__(self, username, password)
        self.cuil = CUIL
        self.telefono = telefono
        self.friends = []
        self.NoOfTimesRejected = 0
        self.pendingRequests = []
        self.BlockedState = False
    
    def __repr__(self):
        return f"{self.username} - Tel: {self.telefono} - CUIL: {self.cuil}"
        
