#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> sss;

int get()
{
	int max = -1;
	int maxp = -1;
	for (int i = 0; i < sss.size() - 1; ++i) 
	{
		int s1 = sss[i];
		int s2 = sss[i + 1];

		int d = (s2 - s1);

		if (d > max) 
		{
			max = d;
			maxp = s1 + d/2;
		}
	}
	return maxp;
}

int geti(int j) {
	for (int i = 0; i < sss.size(); ++i) {
		if (sss[i] == j)
			return i;
	}
	return -1;
}

int do_case(int n, int k, int cases)
{
	sss.push_back(0);
	sss.push_back(n + 1);

	for (int i = 0; i < k - 1; ++i) 
	{
		sss.push_back(get());
		sort(sss.begin(), sss.end());
	}

	int last = get();
	sss.push_back(last);
	sort(sss.begin(), sss.end());
	int lastIndex = geti(last);
	int l = sss[lastIndex - 1];
	int r = sss[lastIndex + 1];
	int ls = last - l - 1;
	int rs = r - last - 1;

	printf("Case #%d: %d %d\n", cases + 1, max(ls,rs), min(ls,rs));
	return 0;
}

int main()
{
	int T;
	int K, N;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		cin >> N;
		cin >> K;
		sss.clear();
		int r = do_case(N, K, i);
		//printf("%s %d\n", S.c_str(), s);
	}

	return 0;
}