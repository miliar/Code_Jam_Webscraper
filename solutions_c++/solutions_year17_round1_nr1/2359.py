#include<iostream>
#include<cstdio>
#include<string>
using namespace std;


void mostrar(char cuadricula[25][25],int filas, int columnas)
{
	for(int i = 0;i<filas;i++)
	{
		for(int j = 0;j<columnas;j++)
		{
			if(cuadricula[i][j]!= ' ')
			{
				cout << cuadricula[i][j];
			}
		}
		cout << "" << endl;
	}
}
void resolver(char cuadricula[25][25])
{
	char ultimaLetra = ' ';
	int i;
	int j;
	for(i = 0;i<25;i++)
	{
		for(j = 0;j<25;j++)
		{
			//RESUELVE LOS ? A DERECHA 
			if(cuadricula[i][j] == '?')
			{
				if(ultimaLetra != ' ')
				{
					cuadricula[i][j] = ultimaLetra;
				}else{
					int punteroi = i;
					int punteroj = j;
					while(punteroi < 25 && ultimaLetra == ' ')
					{
						if(cuadricula[punteroi][punteroj]  != ' ')
						{
							ultimaLetra = cuadricula[punteroi][punteroj];
						}
					}
					if(ultimaLetra!=' ')
					{
						while(punteroj>=j)
						{
							cuadricula[punteroi][punteroj] = ultimaLetra;
							punteroj--;
						}
					}
				}
			}else{
				ultimaLetra = cuadricula[i][j];
			}
			//RESUELVE A DERECHA
		}
		 ultimaLetra = ' ';
		
	}
	

  ultimaLetra = ' ';
	for(i = 24;i>=0;i--)
	{
		for(j = 24;j>=0;j--)
		{
			//RESUELVE LOS ? A IZQUIERDA 
			if(cuadricula[i][j] == '?')
			{
				if(ultimaLetra != ' ')
				{
					cuadricula[i][j] = ultimaLetra;
				}else{
					int punteroi = i;
					int punteroj = j;
					while(punteroi > 0 && ultimaLetra == ' ')
					{
						if(cuadricula[punteroi][punteroj]  != ' ')
						{
							ultimaLetra = cuadricula[punteroi][punteroj];
						}
					}
					if(ultimaLetra!=' ')
					{
						while(punteroj<=j)
						{
							cuadricula[punteroi][punteroj] = ultimaLetra;
							punteroj++;
						}
					}
				}
			}else{
				ultimaLetra = cuadricula[i][j];
			}
			//RESUELVE A IZQUIERDA
		}
		 ultimaLetra = ' ';
	}
	

	
	 ultimaLetra = ' ';
	for(j = 0;j<25;j++)
	{
		for(i = 0;i<25;i++)
		{
			//RESUELVE LOS ? ABAJO 
			if(cuadricula[i][j] == '?')
			{
				if(ultimaLetra != ' ')
				{
					cuadricula[i][j] = ultimaLetra;
				}else{
					int punteroi = i;
					int punteroj = j;
					while(punteroi < 25 && ultimaLetra == ' ')
					{
						if(cuadricula[punteroi][punteroj]  != ' ')
						{
							ultimaLetra = cuadricula[punteroi][punteroj];
						}
						//punteroi++;
					}
					if(ultimaLetra!=' ')
					{
						while(punteroi>=i)
						{
							
							cuadricula[punteroi][punteroj] = ultimaLetra;
							punteroi--;
						}
					}
				}
			}else{
				ultimaLetra = cuadricula[i][j];
			}
			//RESUELVE ABAJO
		}
		 ultimaLetra = ' ';
	}
	


	 ultimaLetra = ' ';
	for(j = 24;j>=0;j--)
	{
		for(i = 24;i>=0;i--)
		{
			//RESUELVE LOS ? ARRIBA 
			if(cuadricula[i][j] == '?')
			{
				if(ultimaLetra != ' ')
				{
					cuadricula[i][j] = ultimaLetra;
				}else{
					int punteroi = i;
					int punteroj = j;
					while(punteroi >0 && ultimaLetra == ' ')
					{
						if(cuadricula[punteroi][punteroj]  != ' ')
						{
							ultimaLetra = cuadricula[punteroi][punteroj];
						}
						//punteroi++;
					}
					if(ultimaLetra!=' ')
					{
						while(punteroi<=i)
						{
							
							cuadricula[punteroi][punteroj] = ultimaLetra;
							punteroi++;
						}
					}
				}
			}else{
				ultimaLetra = cuadricula[i][j];
			}
			//RESUELVE ARRIBA
		}
		 ultimaLetra = ' ';
	}
	

}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);


	int T;
	cin >> T;

	char cuadricula[25][25];
	

	int filas;
	int columnas;

	

	char caracterIngresado;

	for(int t = 1;t<=T;t++)
	{
		for(int r = 0;r<25;r++)
		{
			for(int s = 0;s<25;s++)
			{
				cuadricula[r][s] = ' ';
			}
		}
		cin >> filas;
		cin >> columnas;
		for(int r = 0;r<filas;r++)
		{
			for(int s = 0;s<columnas;s++)
			{
				cin >> caracterIngresado;
				cuadricula[r][s] = caracterIngresado;
			
				
			}
		}
		resolver(cuadricula);
		cout << "Case #" << t << ":" << endl; 
		mostrar(cuadricula,filas,columnas);
	}




	return 0;
}