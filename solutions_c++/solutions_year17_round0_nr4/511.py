#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <limits.h>
#include <algorithm>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <string>
#include <string.h>
#include <sstream>
#include <ctime>

using namespace std;

#define eps 1e-12
#define pi 3.14159265358979323846
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define bgn begin
#define ll long long
#define ld long double
#define ull unsigned long long
#define ii pair<ll,ll>;


const int N=110;
int cases,n,m,r,c,idx,z;
char typ;
bool b[N];



int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	std::ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		cout<<"Case #"<<kase<<": ";
		cin>>n>>m;
		if(n==1)
		{
			typ='.';
			if(m)cin>>typ>>r>>c;
			cout<<"2 ";
			if(typ=='o')cout<<"0\n";
			else
			{
				cout<<"1\n"<<"o 1 1\n";
			}
			continue;
		}
		for(int i=1;i<=n;i++)b[i]=0;
		idx=-1;
		for(int i=1;i<=m;i++)
		{
			cin>>typ>>r>>c;
			if(typ=='+')b[c]=1;
			else
			{
				if(typ=='o')b[c]=1;
				idx=c;
			}
		}
		if(idx==-1)
		{
			idx=1;
			b[1]=0;
		}
		z=2*n-3;
		for(int i=1;i<=n;i++)
		{
			if(!b[i])z++;
		}
		cout<<3*n-2<<" "<<z<<"\n";
		for(int i=1;i<=n;i++)
		{
			if(!b[i])
			{
				if(i==idx)cout<<"o ";
				else cout<<"+ ";
				cout<<"1 "<<i<<"\n";
			}
		}
		for(int i=2;i<=n;i++)
		{
			cout<<"x "<<i<<" ";
			if(i==idx)cout<<"1\n";
			else cout<<i<<"\n";
		}
		for(int i=2;i<n;i++)
		{
			cout<<"+ "<<n<<" "<<i<<"\n";
		}
	}
	return 0;
}