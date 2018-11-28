#include <cstdio>

int main(int argc, char const *argv[])
{
	int casos, flipper, contador;
	scanf("%d", &casos);

	char string[1002] = {0};
	int i = 0;
	char c, var;
	int tam, k;
	const char dummy = '+' ^ '-';

	while ( i < casos)
	{
		//Recepcion de datos
		var = '+';
		tam = 0;
		getchar();
		while((c = getchar()) != ' '){
			string[tam] = c ^ var;
			var = c; 
			tam++;
		}
		string[tam] = var ^ '+';

		scanf("%d", &flipper);

		//Evaluacion
		contador = 0;
		for (k = 0; k <= tam - flipper; ++k){
			if ( string[k])
			{
				string[k + flipper] ^= dummy;
				contador++;
			}
		}

		while(k <= tam){
			if (string[k])
				break;
			k++;
		}

		printf("Case #%d: ",++i);
		
		if (k > tam)
			printf("%d\n", contador );
		else
			printf("IMPOSSIBLE\n");

/*		for (k = 0; k <= tam; ++k)
			printf("%d ", string[k]);
		putchar('\n');*/

	}
	return 0;
}