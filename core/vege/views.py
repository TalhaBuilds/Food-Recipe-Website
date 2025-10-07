from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe

# List + Add new recipe
def recipe_list(request):
    recipes = Recipe.objects.all().order_by('-id')

    if request.method == "POST":
        name = request.POST.get('recipe_name')
        description = request.POST.get('recipe_description')
        image = request.FILES.get('recipe_image')

        if name and description:   # basic validation
            Recipe.objects.create(name=name, description=description, image=image)
            return redirect('recipe_list')

    return render(request, 'index.html', {'recipes': recipes})


# Update recipe
def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == "POST":
        recipe.name = request.POST.get('recipe_name')
        recipe.description = request.POST.get('recipe_description')
        if request.FILES.get('recipe_image'):
            recipe.image = request.FILES.get('recipe_image')
        recipe.save()
        return redirect('recipe_list')

    return render(request, 'index.html', {'recipe': recipe})


# Delete recipe
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return redirect('recipe_list')
