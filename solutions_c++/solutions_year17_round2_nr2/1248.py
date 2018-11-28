#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <utility>
#include <map>
#include <cmath>
#include <iomanip>

using namespace std;

int t;
char ar[1000];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>t;
	int n, r, o, y, g, b, v;
	for(int z=1; z<=t; z++)
	{
		cin>>n>>r>>o>>y>>g>>b>>v;
		int k=0;
		while(o)
		{
			ar[k++]='B';
			ar[k++]='O';
			ar[k++]='B';
			--o, b-=2;
		}
		while(g)
		{
			ar[k++]='R';
			ar[k++]='G';
			ar[k++]='R';
			--g, r-=2;
		}
		while(v)
		{
			ar[k++]='Y';
			ar[k++]='V';
			ar[k++]='Y';
			--v, y-=2;
		}
		while(k<n)
		{
			if(ar[k-1]=='B')
			{
				if(r>=y) ar[k++]='R', --r;
				else ar[k++]='Y', --y;
			}
			else if(ar[k-1]=='R')
			{
				if(b>=y) ar[k++]='B', --b;
				else ar[k++]='Y', --y;
			}
			else
			{
				if(b>=r) ar[k++]='B', --b;
				else ar[k++]='R', --r;
			}
		}
		cout<<"Case #"<<z<<": ";
		if(ar[n-1]!=ar[0] && r>=0 && b>=0 && y>=0)
		{
			for(int i=0; i<n; i++) cout<<ar[i];
			cout<<endl;
		}
		else cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}