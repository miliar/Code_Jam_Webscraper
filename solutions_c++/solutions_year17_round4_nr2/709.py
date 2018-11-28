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
	int n,c,m,p[1005]={0},b[1005]={0},r=0,a=0; //round, ans
	cin >>n>>c>>m;
	rep(i,0,m)
	{
		int x,y;
		cin>>x>>y;
		p[x]++;
		b[y]++;
	}
	rep(i,0,c+1)
		r=max(r,b[i]);
	rep(i,1,n+1)
	{
		int j=0;
		j+=p[i];
		r=max(r,(j-1)/i+1);
	}
	rep(i,1,n+1)
		a+=max(0,p[i]-r);
	cout << "case #" << T << ": " << r<<' '<<a<<endl;
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
