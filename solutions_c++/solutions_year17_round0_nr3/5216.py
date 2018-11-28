// Errachete - B: Tidy Numbers

#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>

using llint = long long int;
struct aux
{
	llint L;
	llint R;
};
struct comp
{
	bool operator()(aux const& elem1, aux const& elem2)
	{
		if (std::min(elem1.L, elem1.R) > std::min(elem2.L, elem2.R))
		{
			return true;
		}
		else if (std::min(elem1.L, elem1.R) == std::min(elem2.L, elem2.R))
		{
			if (std::max(elem1.L, elem1.R) > std::max(elem2.L, elem2.R))
			{
				return true;
			}
		}
		return false;
	}
};

std::ifstream in("datos.in");
std::ofstream out("sol.txt");

void introducir(std::map< aux, llint, comp > & pq, llint num, llint times)
{
	llint L, R;

	if (num > 0)
		--num;
	L = num / 2;
	R = num - L;
	
	if (!pq.count({ L, R}))
		pq.insert({ { L, R }, times });
	else{
		pq[{L, R}] += times;
	}
}

void resolver(int const& caso)
{
	llint tam = 0, personas = 0;
	in >> tam >> personas;

	std::map< aux, llint, comp> data;
	introducir(data, tam, 1);

	std::pair< aux, llint > elem;
	while (personas > 0)
	{
		elem = *data.begin();
		data.erase(elem.first);
		if (elem.first.L == elem.first.R)
		{
			introducir(data, elem.first.L, elem.second * 2);
			personas -= elem.second;
		}
		else
		{
			introducir(data, elem.first.L, elem.second);
			introducir(data, elem.first.R, elem.second);
			personas -= elem.second;
		}
	}

	out << "Case #" << caso << ": " << std::max(elem.first.L, elem.first.R) << ' ' << std::min(elem.first.L, elem.first.R) << '\n';
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