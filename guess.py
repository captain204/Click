import click
import random   



@click.command()
@click.option('--number',prompt='Enter your guess',
               required=True, type=int, help='Number between 1 and 10')    

def guess(number):
    """Simple number guessing game"""
    k = list(range(1,11))
    if random.choice(k) == int(number):
        click.echo('Congratulations you guessed correctly')
    else:
        click.echo('Wrong choice please try again')
    



if __name__ == '__main__':
    guess()

    
