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
#define Rep(i,j,k) for(int i=j;i>k;i--)
#define rep_(i,j,k) for(k::iterator i=j.begin();i!=j.end();i++)
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

void pp(int T)
{
	int n,p,g[4]={0},G,ans;
	cin>>n>>p;
	rep(i,0,n)
	{
		cin>>G;
		g[G%p]++;
	}
	switch(p)
	{
		case 2: ans=g[0]+(g[1]+1)/2;break;
		case 3: ans=g[0]+min(g[1],g[2])+(abs(g[1]-g[2])+2)/3;break;
		case 4: ans=g[0]+min(g[1],g[3])+(abs(g[1]-g[3])+2*g[2]+3)/4;break;
	}
	cout << "case #" << T << ": " << ans << endl;
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
