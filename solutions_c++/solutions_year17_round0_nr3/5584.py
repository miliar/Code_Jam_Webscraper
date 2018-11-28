#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;
int main()
{
	ifstream istream("C-small-1-attempt0.in");
	ofstream ostream("C-small-1-attempt0.out");

	int T;
	istream >> T;

	int N, K;
	vector<int> cnt0;
	for (int i = 0; i < T; ++i)
	{
		cnt0.clear();
		istream >> N >> K;
		cnt0.emplace_back(N);

		for (int j = 0; j < K; ++j)
		{
			sort(cnt0.begin(), cnt0.end());
			int maxNum0 = cnt0.back();
			cnt0.pop_back();
			cnt0.emplace_back((maxNum0 - 1) / 2);
			cnt0.emplace_back(maxNum0 - (maxNum0 + 1) / 2);
		}

		int maxlast = cnt0.back();
		cnt0.pop_back();
		int minlast = cnt0.back();
		cnt0.pop_back();
		ostream << "Case #" << i + 1 << ": " << maxlast << " " << minlast << endl;

	}
	istream.close();
	ostream.close();
}
