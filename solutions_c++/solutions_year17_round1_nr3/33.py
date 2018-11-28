#include <iostream>
#include <algorithm>
#include <fstream>
#include <map>
#include <cstdio>
using namespace std;

map<pair<pair<int,int>,pair<int,int> >,long long> dp;

int hd,ad,hk,ak,B,D;

long long gdp(int i,int j,int k,int l)
{
	if(dp.find(make_pair(make_pair(i,j),make_pair(k,l)))!=dp.end())
		return dp[make_pair(make_pair(i,j),make_pair(k,l))];
	//cout << i << ' ' << j << ' ' << k << ' ' << l << '\n';
	long long c;
	if(i==0) c = 1000000000000000LL;
	else if(k==0) c = 0;
	else if(j>=k) c = 1;
	else c = 1+min(min(gdp(max(0,i-l),j,max(0,k-j),l),((min(100,j+B)>j)?gdp(max(0,i-l),min(100,j+B),k,l):1000000000000000LL)),min(((max(0,hd-l)>i)?gdp(max(0,hd-l),j,k,l):1000000000000000LL),((max(0,l-D)<l)?gdp(max(0,i-max(0,l-D)),j,k,max(0,l-D)):1000000000000000LL)));
	dp[make_pair(make_pair(i,j),make_pair(k,l))] = c;
	//cout << i << ' ' << j << ' ' << k << ' ' << l << ": " << c << '\n';
	return c;
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		cerr << i << '\n';
		dp.clear();
		cin >> hd >> ad >> hk >> ak >> B >> D;
		long long v = gdp(hd,ad,hk,ak);
		cout << "Case #" << i << ": ";
		if(v>=1000000000000000LL) cout << "IMPOSSIBLE\n";
		else cout << v << '\n';
	}
}