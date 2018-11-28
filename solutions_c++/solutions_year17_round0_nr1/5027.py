// Errachete - A: Oversized Pancake Flipper

#include <iostream>
#include <fstream>
#include <string>

std::ifstream in("datos.in");
std::ofstream out("sol.txt");

void resolver(int const& caso)
{

	std::string pancakes = "";
	int flipper = 0, number = 0;
	bool possible = true;
	in >> pancakes >> flipper;

	for (int i = 0; i < pancakes.size(); ++i)
	{
		if (pancakes[i] == '-')
		{
			int j = 0;
			while (j + i < pancakes.size() && j < flipper)
			{
				pancakes[j + i] == '-' ? pancakes[j + i] = '+' : pancakes[j + i] = '-';
				++j;
			}
			if (j + i >= pancakes.size() && j < flipper)
			{
				possible = false;
			}
			++number;
		}
	}

	out << "Case #" << caso << ": ";
	possible ? out << number << '\n' : out << "IMPOSSIBLE\n";
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