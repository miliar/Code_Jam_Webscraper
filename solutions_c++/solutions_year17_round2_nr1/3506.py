#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
using namespace std;


int main()
{
	std::string name = "A-large";
	std::ifstream fin(name + ".in");
	std::ofstream fout(name + ".out");
	int caso = 1;

	double D;
	int N;
	int total;
	double Ki;
	double Si;
	double tempoMinimo=0;

	fin >> total;

	for (int t = 1; t <= total; t++)
	{
		fin >> D;
		fin >> N;

		tempoMinimo = 0;
		for (int i = 0; i < N; i++)
		{
			fin >> Ki;
			fin >> Si;
			if (((D - Ki) / (Si)) > tempoMinimo)
				tempoMinimo = ((D - Ki) / (Si));
		}

		double cenas = D / tempoMinimo;

		fout << "Case #" << t << ": " << fixed << setprecision(6) << cenas  << endl;

	}
	return 0;
}