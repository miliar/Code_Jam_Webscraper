#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void pancakes(int start, int K, int X, int &maior, int &menor);
int insere(string &stalls, int K);

//------------------------------------

void pancakes(int start, int K, int X, int &maior, int &menor)
{
	//INICIA STRING STALLS
	string stalls = "+";
	for (int i = 0; i < start; i++)
		stalls = stalls + "-";
	stalls = stalls + "+";
	//--------------------
	int index = insere(stalls, K);	//DEVOLVE O INDEX ONDE FOI INSERIDO
	int esquerda = 0;

	//PROCURA À ESQUERDA
	int aux = index - 1;
	while (stalls[aux] == '-')
	{
		esquerda++;
		aux--;
	}


	//PROCURA À DIREITA
	int direita = 0;
	aux = index + 1;
	while (stalls[aux] == '-')
	{
		direita++;
		aux++;
	}


	//RETURNS
	if (direita > esquerda)
	{
		maior = direita;
		menor = esquerda;
	}
	else
	{
		maior = esquerda;
		menor = direita;
	
	}
}

int insere(string &stalls, int K)
{
	int cenas;

	//CONTA MAXIMO VAZIOS SEGUIDOS
	int contador = 0;
	int max = 0;

	for (int i = 0; i < stalls.length(); i++)
		if (stalls[i] == '-')
			contador++;
		else
		{
			if (max < contador)
				max = contador;
			contador = 0;
		}

	int index = 0;
	for (int i = 0; i < stalls.length(); i++)
	{
		contador = 0;
		if (stalls[i] == '-')
		{
			for (int x = i; x < stalls.length(); x++)
			{
				if (stalls[x] != '-')
					break;
				contador++;
			}
			if (contador == max)
			{
				cenas = i + contador / 2;

				stalls[cenas] = '+';
				i = i + contador;
				break;
			}
		}
	}

	if((K-1)==0)
		return cenas;
	insere(stalls, K-1);
}


int main()
{
	std::string name = "C-small-1-attempt0";
	std::ifstream fin(name + ".in");
	std::ofstream fout(name + ".out");
	
	string cenas;
	int S, K, total, maior, menor,i;
	fin >> total;
	
	for (int X = 1; X <= total; X++)
	{
		fin >> S;
		fin >> K;
		if (S == K)
		{
			menor = 0;
			maior = 0;
		}
		else
			pancakes(S, K, X, maior, menor);
		
		cout << "Case #" << X << ": " << maior << " " << menor << endl;
		fout << "Case #" << X << ": " << maior << " " << menor << endl;
	}
	system("pause");
	return 0;
}