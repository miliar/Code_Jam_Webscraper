#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <cstdio>
using namespace std;

int v[50][50];
int N,P;
int st[50];
long long req[50];
int plus[50];

void test(int tt)
{
	cin >> N >> P;
	long long mx = 0;
	for(int i=0;i<N;i++)
	{
		cin >> req[i];
		mx = max(mx,req[i]);
	}
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<P;j++)
			cin >> v[i][j];
		sort(v[i],v[i]+P);
	}
	for(int i=0;i<N;i++)
		st[i] = 0;
	int q = 1;
	int ans = 0;
	while(q*mx <= 1200000)
	{
		bool good = 1;
		bool cdone = 0;
		for(int i=0;i<N;i++)
			plus[i] = 0;
		for(int i=0;i<N;i++)
		{
			while(st[i]+plus[i] < P && v[i][st[i]+plus[i]]*100 < q*req[i]*90)
				plus[i]++;
			if(st[i]+plus[i] == P || v[i][st[i]+plus[i]]*100 > q*req[i]*110)
			{
				if(st[i]+plus[i]==P) cdone = 1;
				good = 0;
				break;
			}
			plus[i]++;
		}
		if(cdone) break;
		if(good)
		{
			ans++;
			for(int i=0;i<N;i++)
				st[i] += plus[i];
		}
		else
			q++;
	}
	cout << "Case #" << tt << ": " << ans << '\n';
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
		test(i);
}
