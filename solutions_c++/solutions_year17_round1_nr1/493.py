using namespace std;
#include <cstdlib>
#include <iomanip>
#include <utility>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
#define X first
#define Y second
#define MP make_pair
#define PB push_back
#define rep(i,j,k) for(int i=j;i<k;i++)
#define rep_(i,j,k) for(k::iterator i=j.begin();i!=j.end();i++)
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

void pp(int T)
{
	cout << "case #" << T << ": " << endl;
	int r,c,e[25]={0};
	char a[25][25];
	cin >>r>>c;
	rep(i,0,r)
	{
		rep(j,0,c)
		{
			cin>>a[i][j];
			if (a[i][j]!='?'&&e[i]==0) e[i]=1,a[i][0]=a[i][j];
		}
		if (e[i])
		{
			rep(j,1,c)
				if (a[i][j]=='?') a[i][j]=a[i][j-1];
			if (a[0][0]=='?')
			{
				rep(j,0,c) a[0][j]=a[i][j];
				e[0]=1;
			}
		}
	}
	rep(i,0,r)
	{
		rep(j,0,c)
			cout << ((e[i]==0)?a[i][j]=a[i-1][j]:a[i][j]);
		cout << endl;
	}
}

int main()
{
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	int TT;
	cin >> TT;
	rep(T,1,TT+1) pp(T);
	return 0;
}

/*
Usage:
	cin >> n;  rep(i,0,n);
	set<int> s;rep_(i,s,set<int>);
*/
