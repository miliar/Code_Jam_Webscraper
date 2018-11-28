
#include <iostream>
#include <string>
#include <cmath>
#include <bitset>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;
double eps = 1e-15;

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		int N, C, M;
		cin >> N >> C >> M;
		int t[2][1000];
		int count0 = 0, count1 = 0;
		for (int i = 0; i < 1000; i++)
		{
			t[0][i] = 0;
			t[1][i] = 0;
		}
		for (int i = 0; i < M; i++)
		{
			int a, b;
			cin >> a >> b;
			if (b == 2)
			{
				count1++;
				t[1][a - 1]++;
			}
			else
			{
				count0++;
				t[0][a - 1]++;
			}
		}
		int numRides = max(count0, count1);
		while (true)
		{
			bool success = true;
			int sum = 0;
			for (int i = 0; i < N; i++)
			{
				sum += t[0][i] + t[1][i];
				if (sum > numRides*(i + 1))
				{
					success = false;
					numRides++;
					break;
				}
			}
			if (success) break;
		}
		int prom = 0;
		for (int i = 0; i < N; i++)
		{
			if (t[0][i] + t[1][i] > numRides)
			{
				prom += t[0][i] + t[1][i] - numRides;
				break;
			}
		}
		cout << "Case #" << tc << ": " << numRides << " " << prom << endl;
	}

}