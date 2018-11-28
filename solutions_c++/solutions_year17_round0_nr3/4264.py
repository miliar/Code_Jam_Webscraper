#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <map>
using namespace std;
const int MAX_N=1050;
struct name
{
	long long n,r,l,ma,mi;
};
map <name,long long> och;
bool operator<(name a,name b)
{
	return a.mi>b.mi||a.mi==b.mi&&a.ma>b.ma||a.mi==b.mi&&a.ma==b.ma&&a.l<b.l||
		a.mi==b.mi&&a.ma==b.ma&&a.l==b.l&&a.r<b.r;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	long long t,n,k,p,a1,a2;
	cin>>p;
	for (int q=1;q<=p;q++)
	{
		cin>>n>>k;
		name a,b,c;
		a.n=n;
		a.l=(n-1)/2;
		a.r=n/2;
		a.ma=max(a.l,a.r);
		a.mi=min(a.l,a.r);
		och.clear();
		och[a]=1;
		for (int j=1;j<=k;j++)
		{
			a=och.begin()->first;
			if (j==k)
			{
				cout<<"Case #"<<q<<": "<<a.ma<<" "<<a.mi<<"\n";
			}
			och[a]--;
			if (och[a]==0)
			{
				och.erase(a);
			}
			b.n=a.l;
			b.l=(b.n-1)/2;
			b.r=b.n/2;
			b.ma=max(b.l,b.r);
			b.mi=min(b.l,b.r);
			och[b]++;
			b.n=a.r;
			b.l=(b.n-1)/2;
			b.r=b.n/2;
			b.ma=max(b.l,b.r);
			b.mi=min(b.l,b.r);
			och[b]++;
		}
	}
	return 0;
}