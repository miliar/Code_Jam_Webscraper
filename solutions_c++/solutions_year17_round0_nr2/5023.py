// Errachete - B: Tidy Numbers

#include <iostream>
#include <fstream>
#include <string>
#include <stack>

using llint = long long int;

std::ifstream in("datos.in");
std::ofstream out("sol.txt");

std::string resta(std::string str)
{
	std::stack< char > pila;
	std::string aux = "";
	while (!str.empty())
	{
		if (str.back() == '0')
		{
			pila.push('9');
			str.pop_back();
		}
		else
		{
			if (str.back() != '1')
				pila.push(char(int(str.back()) - 1));
			str.pop_back();
			aux = str;
			str.clear();
		}
	}
	while (!pila.empty())
	{
		aux.push_back(pila.top());
		pila.pop();
	}

	return aux;
}

void fillWith0(std::string & str, int i, int tam) 
{
	for (; i < tam; ++i)
	{
		str.push_back('0');
	}
}

void resolver(int const& caso)
{
	
	bool tidy = false;
	std::string N = "", sol = "";
	in >> N;

	while (!tidy)
	{
		tidy = true;
		int i = 0;
		sol = N[0];
		for (; i < N.size() - 1 && tidy; ++i)
		{
			N[i] <= N[i + 1] ? sol.push_back(N[i + 1]) : tidy = false;
		}
		if (!tidy)
		{
			fillWith0(sol, i, N.size());
			N = sol;
			N = resta(N);
		}
	}

	out << "Case #" << caso << ": " << sol << '\n';
}

int main()
{

	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);

	int numCasos = 0;
	in >> numCasos;
	for (int i = 1; i <= numCasos; ++i)
	{
		resolver(i);
		std::cout << i << '\n';
	}

	system("PAUSE");
	return 0;
}