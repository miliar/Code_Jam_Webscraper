// Code Jam 1B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <set>
#include <iostream>
#include <functional>
#include <iomanip>
#include <sstream>
#include <string>

using namespace std;

typedef pair<double, double> pdd;

string toString(const double& n)
{
	stringstream ss;

	ss << scientific << setprecision(17) << n;

	string str;

	ss >> str;

	return str;
}

bool replace(std::string& str, const std::string& from, const std::string& to) {
	size_t start_pos = str.find(from);
	if (start_pos == std::string::npos)
		return false;
	str.replace(start_pos, from.length(), to);
	return true;
}


string format(const double& n)
{
	string s = toString(n);
	if (s.find('.') == string::npos)
	{
		s.append(".");
	}
	replace(s, "e+0", "e");
	replace(s, "e+", "e");
	return s;
}

struct horse
{
	int K, S;

	bool operator>(const horse& h) const
	{
		return K > h.K;
	}
};

pdd poi(const horse& h1, const horse& h2)
{
	double det =(double) (h2.S - h1.S);
	return make_pair(
		((-1.0 * -h2.K) - (-1.0 * -h1.K)) / det,
		((h1.S * -h2.K) - (h2.S * -h1.K)) / det
	);


}

int main()
{
	ifstream in("A-small-attempt2.in");
	ofstream out;
	out.open("out.txt");

	int T;

	in >> T;

	for (int i = 0; i < T; i++)
	{
		int D, N;

		in >> D >> N;

		out << "Case #" << (i + 1) << ": ";

		set<horse, greater<horse>> horses;

		for (int j = 0; j < N; j++)
		{
			int k, s;

			in >> k >> s;

			horses.insert({ k, s });
		}

		while (horses.size() > 1)
		{
			set<horse, greater<horse>>::const_iterator h1 = horses.begin();
			set<horse, greater<horse>>::const_iterator h2 = ++horses.begin();
			pdd p = poi(*h1, *h2);

			cout << p.second << "\n";

			if (p.second > D)
			{
				horses.erase(h1);
			}
			else if (p.second >= (*h1).K)
			{
				horses.erase(h2);
			}
			else
			{
				horses.erase(h1);
			}
		}
		double t = (D - (*horses.begin()).K) / (double)((*horses.begin()).S);
		out << format(D / t) << "\n";
	}

	in.close();
	out.close();

    return 0;
}

