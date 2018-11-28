#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <unordered_map>
#include <iomanip>
#include <map>

using namespace std;

int T;
long long D, N;

struct less_than_value
{
	inline bool operator() (const pair<long long, int>& p1, const pair<long long, int>& p2) const
	{
		return p1.second < p2.second;
	}
};

double solve(vector<pair<long long, int>> &h)
{
	long double time = 0;

	for(long long i = 0; i < N; ++i)
	{
		if(h[i].second*time + h[i].first<D)
			time = double(D - h[i].first) / double(h[i].second);
	}

	return time==0 ? 0 : double(D)/time;
}

int main()
{
	cout << fixed;
	cout << setprecision(6);
	cin >> T;

	for(int i = 0; i < T; ++i)
	{
		cin >> D >> N;
		vector<pair<long long, int>> h;

		for(long long j = 0; j < N; ++j)
		{
			long long Ki, Si;
			cin >> Ki >> Si;
			h.push_back(make_pair(Ki, Si));
		}

		sort(h.begin(), h.end(), less_than_value());

		
		cout << "Case #" << i + 1 << ": " << solve(h) << endl;
	}

	return 0;
}