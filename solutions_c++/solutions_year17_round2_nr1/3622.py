// Errachete - Problema
#define NUM_CASOS
#include <vector>
#include <iomanip>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <utility>
using namespace std;

using lli = long long int;
using p = pair< lli, double >;

double last(vector< p > const& v, lli dest)
{
	double slowest = (dest - v[0].first) / (v[0].second);
	for (lli i = 0; i < v.size(); ++i)
	{
		if ((dest - v[i].first) / (v[i].second) > slowest)
			slowest = (dest - v[i].first) / (v[i].second);
	}
	return slowest;
}

double bs(double min, double max, double const ult, lli const dest)
{
	if (max - min <= 0.000001)
		return max;
	else
	{
		double med = (min + max) / 2;
		if (dest / med < ult)
		{
			return bs(min, med, ult, dest);
		}
		else
			return bs(med, max, ult, dest);
	}
}

#ifdef NUM_CASOS
void resuelveCaso(int i) 
{
	lli dest, numHors;
	cin >> dest >> numHors;
	vector< p > horses(numHors);
	for (auto & a : horses){
		cin >> a.first >> a.second;
	}

	double ult = last(horses, dest);

	double max = dest / ult;

	double sol = bs(1, max, ult, dest);

	cout << "Case #" << i << ": ";
	cout << fixed << setprecision(6) << sol << '\n';
}
#endif

#ifdef CENTINELA
bool resuelveCaso()
{
	if (centinela)
		return false;
	
	return true;
}
#endif

#ifdef INFINITA
bool resuelveCaso()
{
	if (!cin)
		return false;

	return true;
}
#endif



int main() {
	
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

#ifndef ONLINE_JUDGE
	ifstream in("datos.txt");
	auto cinbuf = std::cin.rdbuf(in.rdbuf());
	ofstream out("sol.txt");
	auto coutbuf = std::cout.rdbuf(out.rdbuf());
#endif 

#ifdef NUM_CASOS
	int numCasos;
	cin >> numCasos;
	for (int i = 1; i <= numCasos; ++i)
		resuelveCaso(i);
#endif

#ifdef CENTINELA
	while (resuelveCaso());
#endif

#ifdef INFINITA
	while (resuelveCaso());
#endif

#ifndef ONLINE_JUDGE
	std::cin.rdbuf(cinbuf);
	std::cout.rdbuf(coutbuf);
	cout << "Cuidado al subir el problema. La entrada esta redirigida.\n";
	system("PAUSE");
#endif

	return 0;
}