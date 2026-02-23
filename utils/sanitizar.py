import unicodedata

def sanitizar(texto):
      """
          Limpia el texto del usuario:
              - Convierte a minusculas
                  - Elimina tildes y acentos
                      - Elimina la enie (n~)
                          - Elimina la dieresis
                              """
      # Convertir a minusculas
      texto = texto.lower()
      # Normalizar unicode y eliminar diacriticos (tildes, dieresis, etc.)
      texto = unicodedata.normalize('NFD', texto)
      texto = ''.join(
          c for c in texto
          if unicodedata.category(c) != 'Mn'
      )
      # Reemplazar n~ por n (por si queda algun residuo)
      texto = texto.replace('\u00f1', 'n')
      return texto
