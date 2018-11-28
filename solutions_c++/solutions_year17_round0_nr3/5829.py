#include <fstream>
#ifdef ONLINE_JUDGE
#define cin in
#define cout out
#endif
#include <algorithm>
#include <iostream>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <set>
#include <string>
#include <map>
#define M_PI 3.14159265358979323846
#include <cmath>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include <bitset>
#include <cfloat>
#include <queue>
#include <climits>
using namespace std;

const size_t MAX = 1000 + 1;

uint64_t gcd(uint64_t a, uint64_t b)
{
	return b ? gcd(b, a%b) : a;
}


int main(int argc, char *argv[])
{
	ios_base::sync_with_stdio(false);
	ifstream in("input.txt");
	ofstream out("output.txt");
	int64_t n, k, t;
	cin >> t;
	for (int32_t i = 1; i <= t; ++i)
	{
		priority_queue<pair<int64_t, int64_t>> bath;
		cin >> n >> k;
		int64_t minLen = INT64_MAX, maxLen = INT64_MIN;
		bath.push(make_pair(n, -1));
		for (int32_t j = 0; j < k; ++j)
		{
			pair<int64_t, int64_t> temp = bath.top();
			bath.pop();
			temp.second *= -1;
			int64_t newPlace = temp.second + temp.first / 2 - (temp.first % 2 == 0? 1: 0);
			int64_t leftStart = temp.second, rightStart = newPlace;
			int64_t leftLen = newPlace - temp.second, rightLen = temp.first - newPlace + temp.second - 1;
			bath.push(make_pair(leftLen, -leftStart));
			bath.push(make_pair(rightLen, -rightStart));
			if (j == k - 1) // last person
			{
				maxLen = max(leftLen, rightLen);
				minLen = min(leftLen, rightLen);
			}
		}
		cout << "Case #" << i << ": " 
			<< maxLen << " " << minLen << endl;
	}
	return 0;
}