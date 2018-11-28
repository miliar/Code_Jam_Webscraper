#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool verifica(int Num) {
	//EXCESSÃO POR CAUSA DA INVERSÃO!!!!!!!!!!!!!!!!!!!!!!!!!!
	if (Num % 10 == 0)
		return false;

	bool tab[10] = { 0,0,0,0,0,0,0,0,0,0 };
	int resto;

	bool flag = 0;

	//INVERTE O NUMERO
	int ret = 0;
	int i = 1;

	while (i <= Num)
	{
		ret *= 10;
		ret += (Num % (i * 10) - Num%i) / i;
		i *= 10;
	}
	Num = ret;
	//PARA DE INVERTER

	while (true)
	{
		resto = Num % 10;
		Num = Num / 10;

		if (tab[resto] == true)
			return false;
		else
		{
			for (int i = 0; i<resto; i++)
			{
				if (tab[i] == false)
					tab[i] = true;
			}
		}

		if (Num == 0)
			return true;
	}
}

int Tatiana(int N)
{
	int ultimo;
	int Atual = 1;
	while (Atual <= N)
	{
		if (verifica(Atual))
			ultimo = Atual;
		Atual++;
	}

	return ultimo;
}

int main()
{
	std::string name = "B-small-attempt1";
	std::ifstream fin(name + ".in");
	std::ofstream fout(name + ".out");

	int N;
	int aux;

	fin >> N;

	for (int i = 1; i<=N; i++)
	{
		fin >> aux;
		fout << "Case #" << i << ": " << Tatiana(aux) << endl;
	}
	return 0;
}