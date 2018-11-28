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


ll cases,n,k,pw[70],mx,c;



int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	std::ios::sync_with_stdio(false);
	cin.tie(0);
	pw[0]=1;
	for(int i=1;i<=62;i++)pw[i]=pw[i-1]*2;
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		cin>>n>>k;
		cout<<"Case #"<<kase<<": ";
		mx=n;
		c=1;
		for(int i=0;;i++)
		{
			if(k<=pw[i])
			{
				if(k>c)mx--;
				if(mx%2==1)cout<<(mx/2)<<" "<<(mx/2);
				else cout<<(mx/2)<<" "<<(mx/2)-1;
				cout<<"\n";
				break;
			}
			k-=pw[i];
			if(mx%2==1)c+=pw[i];
			mx/=2;
		}
	}
	return 0;
}