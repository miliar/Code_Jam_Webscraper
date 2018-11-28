#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<queue>
#include<vector>
#include<cstdio>
#include<iomanip>

using namespace std;

long long n, destination;
long long initialP[1001]; 
long long maxS[1001];

bool satisfy(long double curTime)
{
	for (int i = 0; i < n; i++)
	{
		if (initialP[i] + curTime * maxS[i] < destination)
			return 0;
	}
	return 1;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	long double resTime;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> destination >> n;
		resTime = 0;
		for (int j = 0; j < n; j++)
		{
			cin >> initialP[j] >> maxS[j];
			resTime = max(resTime, ((long double)(destination - initialP[j])) / (long double)maxS[j]);
		}
		
		cout << "Case #" << i << ": ";
		cout << setprecision(6) << fixed;
		cout << destination / resTime << endl;
	}
	return 0;
}
