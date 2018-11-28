#include <iostream>
#include <algorithm>
#include <fstream>

#define REP(i, n) for (int i = 0; i < n; ++i)
#define FOR(i, a, b) for (int i = a; i <= b; ++i)
#define FORD(i, a, b) for (int i = a; i >= b; --i)
#define M_PI 3.14159265358979323846

using namespace std;

struct pancake
{
	long long int radius;
	long long int height;
	long long int size;
};

bool cakePosition(pancake cake1, pancake cake2)
{
	if (cake1.size > cake2.size)
		return false;

	else if (cake1.size < cake2.size)
		return true;

	else
	{
		if (cake1.radius > cake2.radius)
			return false;

		return true;
	}
}


int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T;

	cin >> T;

	cout << fixed;
	cout.precision(9);

	REP(t, T)
	{
		int K, N;

		pancake *cakes;

		cin >> N >> K;

		cakes = new pancake[N + 1];

		FOR(i, 1, N)
		{
			cin >> cakes[i].radius >> cakes[i].height;
			cakes[i].size = cakes[i].radius * cakes[i].height * 2;
		}

		pancake temp;

		FOR(i, 1, N)
		{
			FOR(j, i + 1, N)
			{
				if (cakePosition(cakes[i], cakes[j]))
				{
					temp = cakes[i];
					cakes[i] = cakes[j];
					cakes[j] = temp;
				}
			}
		}
		
		double total = 0;
		long long int maxIndex = 0;

		FOR(i, 1, K)
		{
			if (maxIndex < cakes[i].radius)
				maxIndex = cakes[i].radius;

			total += cakes[i].size;
		}

		double temptotal = total - cakes[K].size;

		total += maxIndex * maxIndex;

		double maxtotal = total;

		FOR(i, K + 1, N)
		{
			total = cakes[i].size;

			long long int tempIndex = cakes[i].radius;

			FOR(j, 1, K - 1)
			{
				if (tempIndex < cakes[j].radius)
					tempIndex = cakes[j].radius;
			}

			total += temptotal + tempIndex * tempIndex;

			if (maxtotal < total)
				maxtotal = total;

		}
		maxtotal *= M_PI;

		cout << "Case #" << t + 1 << ": " << maxtotal << endl;

		delete cakes;
	}

	return 0;
}