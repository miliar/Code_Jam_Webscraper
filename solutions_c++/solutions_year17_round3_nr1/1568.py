#include <iostream>
#include <algorithm>
#include <vector>
#define PI 3.14159265358979
using namespace std;

int T, N, K, R, H;
vector<pair<double, double>> cake;
double total, cache[1000][1000];

bool cmp(pair<int, int> left, pair<int, int> right)
{
	if (left.first < right.first)
		return false;
	else if (left.first == right.first)
		return (left.second > right.second);
	else
		return true;
}

double sideSyrup(int index, int nextCake)
{
	if (nextCake == 0 || index == N)
		return 0;

	double &ret = cache[index][nextCake];
	if (ret != -1)
		return ret;

	double in, out;
	in = sideSyrup(index + 1, nextCake - 1) + 2 * PI * cake[index].first * cake[index].second;
	out = sideSyrup(index + 1, nextCake);

	ret = max(in, out);
	return ret;
}

int main()
{
	cin >> T;
	for (int testCase = 1; testCase <= T; testCase++)
	{
		cake.clear();
		total = 0;
		for (int i = 0; i < 1000; i++)
			for (int j = 0; j < 1000; j++)
				cache[i][j] = -1;

		cin >> N >> K;
		for (int i = 0; i < N; i++)
		{
			cin >> R >> H;
			cake.push_back(make_pair(R, H));
		}

		sort(cake.begin(), cake.end(), cmp);

		for (int i = 0; i <= N - K; i++)
			total = max(total, PI * cake[i].first * cake[i].first + 2 * PI * cake[i].first * cake[i].second + sideSyrup(i + 1, K - 1));

		cout.setf(ios::showpoint);
		cout << fixed;
		cout.precision(7);
		cout << "Case #" << testCase << ": " << total << endl;
	}

	return 0;
}