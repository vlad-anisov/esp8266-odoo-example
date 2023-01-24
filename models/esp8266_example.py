from odoo import models, fields
import requests


class ESP8266Example(models.Model):
    _name = "esp8266.example"
    _description = "esp8266 example"

    display_text = fields.Char(string="Display")
    is_led = fields.Boolean(string="LED")
    is_button = fields.Boolean(string="Button")

    def write(self, values):
        result = super().write(values)
        self.send_data_to_esp8266()
        return result

    def send_data_to_esp8266(self):
        self.ensure_one()
        headers = {
            "Host": "192.168.100.13",
        }
        payload = {
            "led": "on" if self.is_led else "off",
            "text": self.display_text or "False",
        }
        requests.get("http://192.168.100.13", params=payload, headers=headers)

