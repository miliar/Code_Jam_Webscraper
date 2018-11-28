#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>

using namespace std;
ofstream out("tidynumbers.out");
ifstream in("tidynumbers.in");


string convertToString(long long nr)
{
	stringstream ss;
	ss << nr;
	string str = ss.str();
	return str;
}

int isTidyNumber(long long  n)
{
	string nr = to_string(n);
	for (int i = 1; i < nr.length(); i++)
	{
		if (nr[i] < nr[i - 1])
		{
			return (int)nr.length() - i - 1;
		}
	}
	return -1;
}

int main()
{
	int T;
	in >> T;
	for (int test = 1; test <= T; ++test)
	{
		long long n;
		in >> n;
		out << "Case " << "#" << test << ":" << " ";

		int index = isTidyNumber(n);
		while (index != -1)
		{
			long long power = pow(10, index);
			long long rest = power - 1;
			n /= power;
			n *= power;
			n -= power;
			n += rest;
			index = isTidyNumber(n);
		}

		out << n << "\n";

	}


	return 0;
}
