from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['curso', 'duracion', 'plataforma', 'dificultad']

    def clean_curso(self):
        curso = self.cleaned_data.get('curso', '').strip()
        self._validar_longitud(curso)
        self._validar_reservado(curso)
        return curso

    def _validar_longitud(self, curso):

        # Validación de longitud mínima
        if len(curso) < 3:
            raise forms.ValidationError('El nombre del curso debe tener al menos 3 caracteres.')
    
    def _validar_reservado(self, curso):

        # Validación de nombre reservado
        if curso.lower()== 'prueba':
            raise forms.ValidationError('El nombre "Prueba" está reservado para test.')

        

    def clean_duracion(self):
        duracion = self.cleaned_data.get('duracion')
        if not duracion:
            raise forms.ValidationError('La duración es obligatoria.')
        return duracion

    def clean_plataforma(self):
        plataforma = self.cleaned_data.get('plataforma')
        if not plataforma:
            raise forms.ValidationError('La plataforma es obligatoria.')
        return plataforma

