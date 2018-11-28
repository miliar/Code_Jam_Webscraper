#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int testCount;

pair<long long, long long> stallsDistance(long long total, long long people)
{

	if (people == 1)
	{
		return make_pair(total / 2, (total - 1) / 2);
	}
	if (people % 2 == 0)
		return stallsDistance(total / 2, people / 2);
	return stallsDistance((total - 1) / 2, (people - 1) / 2);
}
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);	
	cin >> testCount;
	for (int testNumber = 1; testNumber <= testCount; testNumber++)
	{
		long long n, k;
		cin >> n >>	k;
		auto ans = stallsDistance(n, k);
		printf("Case #%d: %lld %lld\n", testNumber, ans.first, ans.second);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
