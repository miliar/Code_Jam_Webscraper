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
	pii a[55][55];
	int b[1005],l[55]={0},r[55],B=0,n,p,ans=0;//location
	cin >> n >> p;
	rep(i,0,n)
		cin>>r[i];
	rep(i,0,n)
		rep(j,0,p)
		{
			int x;
			cin >> x;
			a[i][j].X=(10*x-1)/(11*r[i])+1;
			a[i][j].Y=(10*x)/(9*r[i]);
			b[B++]=a[i][j].X;
		}
	rep(i,0,n) sort(a[i],a[i]+p),a[i][p].X=a[i][p].Y=1e7;
	p++;
	sort(b,b+B);b[B]=1e7;
	rep(k,0,B)
	{
		rep(i,0,n)
		{
			while (a[i][l[i]].Y<b[k]) l[i]++;
			if (a[i][l[i]].X>b[k]) goto loc_1;
		}
		rep(i,0,n)
			l[i]++;
		ans+=1;
loc_1:;
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
