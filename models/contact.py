from odoo import models, fields, api

class ContactCard(models.Model):
    _name = 'contact.card'
    _description = 'Contact Card Model'

    # Campos del modelo
    name = fields.Char(string='Name', required=True)  # Nombre del contacto
    email = fields.Char(string='Email')  # Correo electrónico del contacto
    phone = fields.Char(string='Phone')  # Teléfono del contacto
    address = fields.Text(string='Address')  # Dirección del contacto
    company = fields.Many2one('res.partner', string='Company')  # Compañía del contacto
    identification = fields.Char(string='Identification')  # Identificación del cliente
    country = fields.Char(string='Country', compute='_compute_country', store=True)  # País determinado

    # Diccionario para mapear códigos de identificación de países
    country_map = {
        'US': 'United States',  # Estados Unidos
        'CA': 'Canada',  # Canadá
        'MX': 'Mexico',  # México
        'FR': 'France',  # Francia
        'DE': 'Germany',  # Alemania
        'EC': 'Ecuador',  # Ecuador
        
    }

    @api.depends('identification')
    def _compute_country(self):
        """
        Método para determinar el país basado en las dos primeras letras de la identificación del cliente.
        Este método se ejecuta automáticamente cuando cambia el campo 'identification'.
        """
        for record in self:
            # Verifica si la identificación tiene al menos dos caracteres
            if record.identification and len(record.identification) >= 2:
                # Obtiene las dos primeras letras de la identificación y las convierte a mayúsculas
                country_code = record.identification[:2].upper()
                # Asigna el país correspondiente basado en el diccionario country_map
                record.country = self.country_map.get(country_code, 'Unknown')
            else:
                # Asigna 'Unknown' si la identificación no es válida o no tiene suficiente longitud
                record.country = 'Unknown'

