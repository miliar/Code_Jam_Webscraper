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


int cases,n;
char c,s[30];



int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	std::ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		cin>>(s+1);
		n=strlen(s+1);
		c='t';
		for(int i=1;i<n;i++)
		{
			if(s[i]>s[i+1])
			{
				c=s[i];
				break;
			}
		}
		cout<<"Case #"<<kase<<": ";
		if(c=='t')cout<<(s+1)<<"\n";
		else if(c=='1')
		{
			for(int i=1;i<n;i++)cout<<'9';
			cout<<"\n";
		}
		else
		{
			for(int i=1;i<n;i++)
			{
				if(s[i]==c)
				{
					s[i]--;
					for(int j=i+1;j<=n;j++)s[j]='9';
					break;
				}
			}
			cout<<(s+1)<<"\n";
		}
	}
	return 0;
}