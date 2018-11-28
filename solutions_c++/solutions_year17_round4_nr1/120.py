#include<stdio.h>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
map<vector<int>, int>ma;
int calc(vector<int>v, int n)
{
	if (ma.count(v))return ma[v];
	int maxi = 0;
	for (int i = 0; i < v.size(); i++)
	{
		if (v[i] != 0)
		{
			v[i]--;
			maxi = max(maxi, calc(v, (n + i) % v.size()) + (n == 0));
			v[i]++;
		}
	}
	return ma[v] = maxi;
}
int main()
{
	freopen("a-large.in", "r", stdin);
	freopen("outl.txt", "wb", stdout);
	int data;
	scanf("%d", &data);
	for (int p = 1; p <= data; p++)
	{
		int num, gen;
		scanf("%d%d", &num, &gen);
		ma.clear();
		vector<int>v;
		v.resize(gen);
		for (int i = 0; i < num; i++)
		{
			int z;
			scanf("%d", &z);
			v[z%gen]++;
		}
		printf("Case #%d: %d\n", p, calc(v, 0));
	}
}