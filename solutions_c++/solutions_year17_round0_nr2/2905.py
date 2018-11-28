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

long long fixStep(long long n)
{
	vector<int> d;
	long long m = n;
	while (n > 0)
		d.push_back(n % 10), n /= 10;
	reverse(d.begin(), d.end());
	int i = 0;
	while (i + 1 < d.size() && d[i] <= d[i + 1])
		i++;
	if (i < d.size() - 1)
	{
		d[i]--;
		for (int j = i + 1; j < d.size(); j++)
			d[j] = 9;
		for (int c : d)
		{
			n *= 10;
			n += c;
		}
		return fixStep(n);
	}
	return m;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);	
	cin >> testCount;
	for (int testNumber = 1; testNumber <= testCount; testNumber++)
	{
		long long n, m;
		cin >> n;
		printf("Case #%d: %lld\n", testNumber, fixStep(n));		
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
