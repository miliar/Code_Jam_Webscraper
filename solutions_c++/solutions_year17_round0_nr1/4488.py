//IIT Kanpur FacelessMen India
#pragma GCC optimize("O3")
#include <bits/stdc++.h>
#include <cstring>
#include <cstdio>
#include <iostream>
using namespace std;
typedef long long ll;
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define X first
#define Y second
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define FILL(a,x) memset(a,x,sizeof(a))
#define foreach( gg,itit )  for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define mp make_pair
#define pb push_back
#define all(s) s.begin(),s.end()
#define present(c,x) ((c).find(x) != (c).end())
const double EPS = 1e-8;
const int mod = 1e9+7;
const int N = 1e6+10;
const ll INF = 1e18;
#ifdef DEBUG
#define dprintf(fmt,...) fprintf(stderr,fmt,__VA_ARGS__)
#else
#define dprintf(fmt,...)
#endif
bool alertate(vector<int> b)
{
	return true;
}
void display(vector<int> n)
{
	int i;
	for(i=0;i<n.size();i++)
	{
		cout<<n[i];
	}
	cout<<"\n";
}
int getAns(vector<int> b,int k)
{
	int n=b.size();
	int i=0;
	int ans=0;
	//if(alertate(b))
	//	return -1;
	while(i!=n)
	{
		//cout<<"i"<<":"<<i<<"\n";
		//display(b);
		if(b[i]==1)
			i++;
		else
		{
			//cout<<"i"<<":"<<i<<"\n";
			ans++;
			int j;
			if(i+k>n)
				return -1;
			for(j=0;j<k;j++)
			{
				if(b[j+i]==1)
					b[j+i]=0;
				else 
					b[j+i]=1;
			}
			i++;
		}
	}
	//display(b);
	return ans;
}
int main()
{ 
	int t;
	cin >> t;
	int i;
	for(i=0;i<t;i++)
	{
		string s;
		cin >> s;
		vector<int> bin;
		int j;
		for(j=0;j<s.size();j++)
		{
			if(s.at(j)=='-')
			{
				bin.push_back(0);
			}
			else
			{
				bin.push_back(1);
			}
		}
		int k;
		cin >> k;
		cout<<"Case #"<<(i+1)<<": ";
		int temp=getAns(bin,k);
		if(temp==-1)
			cout<<"IMPOSSIBLE";
		else
			cout<<temp;
		cout<<"\n";
	}
	return 0;
}
