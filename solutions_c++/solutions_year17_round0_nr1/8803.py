#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int troca(string &, int &);
int verificaKSeguidas(string &, int &);
void flipespecial(string &, int , int &);
int VerificaInvertidas(string &);

//--------------------------------------------------

int troca(string &S, int &K)
{
	int contador = 0;
	while (verificaKSeguidas(S,K) != 0)
	{
		contador++;
		flipespecial(S,verificaKSeguidas(S, K), K);
	}


	int index = 0;
	int max = 0;
	while (max<1024)
	{
		index = VerificaInvertidas(S);
		if (index == -1)
			return contador;
		if (index < S.length() && index > (S.length()-K))
			index = S.length() - K;
		flipespecial(S, index, K);
		contador++;		
		max++;
	}
	return (-1);
}

int verificaKSeguidas(string &S, int &K)
{
	int aux;
	for (size_t  i = 0; i<S.length(); i++)
	{
		aux = 0;
		if (S[i] == '-')
		{
			size_t i2 = i;
			while ((i2<S.length()) && (S[i2] == '-'))
			{
				aux++;
				if (aux == K)
					return i;
				i2++;
			}
			i = i2;
		}
	}
	return false;
}

void flipespecial(string &S, int index, int &K)
{
	for (int i = index; i < index+K; i++)
	{
		if (S[i] == '-')
			S[i] = '+';
		else
			S[i] = '-';
	}
}

int VerificaInvertidas(string &S)
{
	for (size_t i = 0; i < S.length(); i++)
	{
		if (S[i] == '-')
			return i;
	}
	return -1;
}

int main()
{
	std::string name = "A-large";
	std::ifstream fin(name + ".in");
	std::ofstream fout(name + ".out");
	int caso = 1;

	int total;
	string S;
	int K;

	fin >> total;

	while (total>0)
	{
		fin >> S;
		fin >> K;

		int aux = troca(S, K);
		if (aux != -1)
		{
			fout << "Case #" << caso << ": " << aux << endl;
		}
		else
		{
			fout << "Case #" << caso << ": IMPOSSIBLE" << endl;
		}

		total--;
		caso++;
	}
	return 0;
}