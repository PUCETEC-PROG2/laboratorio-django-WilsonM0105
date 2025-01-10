from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from django.shortcuts import redirect, render
from pokedex.forms import PokemonForm

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
            'pokemons': pokemons,
            'trainers': trainers
        },
        request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer_details(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

def add_pokemon(request):
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save
            return redirect('pokemon:index')
    else:
        form = PokemonForm()
    
    return render(request, 'pokemon_form.html', {'form': form}) 