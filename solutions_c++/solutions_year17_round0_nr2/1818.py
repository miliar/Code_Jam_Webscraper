/* ***********************************************
Author        :yuanzhaolin
Created Time  :2017/4/8 22:03:15
File Name     :b.cpp
************************************************ */

#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <utility>
using namespace std;
#define repp(i,a,b) for(int i=a;i<=b;i++)
#define rep(i,a) for(int i=0;i<a;i++)
#define REP(i,a) for(int i=1;i<=a;i++)
#define per(i,a,b) for(int i=a-1;i>=b;i--)
#define foreach(i,a) for(int i=head[a];i>=0;i=ee[i].next)
#define Foreach(i,a) for(__typeof((a).begin())i=(a).begin();i!=(a).end();i++)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define mp make_pair
#define m0(x) memset(x,0,sizeof(x))
#define mff(x) memset(x,0xff,sizeof(x))
#define fi first
#define se second
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define SZ(x) ((int)(x).size())
#define sqr(x) ((x)*(x))
#define C1(x) cout<<x<<endl
#define C2(x,y) cout<<x<<" "<<y<<endl
#define C3(x,y,z) cout<<x<<" "<<y<<" "<<z<<endl
typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< pair<int,int> > VPII;
const ll mod=(ll)1e9+7;
const ll maxn=(ll)1e5+7;
const ll maxe=(ll)1e6+7;
const ll INF=(ll)1e9+7;
const double PI=acos(-1);
int dx[4]={0,0,1,-1};
int dy[4]={-1,1,0,0};
int n;
int a[maxn];
string s;
bool isok()
{
	for(int i=0;i<n-1;i++)
	{
		if(a[i]>a[i+1]) return false;
	}
	return true;
}
void solve()
{
	s=s+"0";
	for(int t=n;t>=0;t--)
	{
		a[t]=s[t]-'0'-1;
		for(int i=t+1;i<n;i++)
			a[i]=9;
		for(int i=0;i<t;i++)
			a[i]=s[i]-'0';
		if(isok()) return ;
	}
}
int main()
{
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int T;	    
	cin>>T;
	for(int ca=1;ca<=T;ca++)
	{
		cin>>s;
		n=s.length();
		solve();
		printf("Case #%d: ",ca);
		if(a[0]!=0) cout<<a[0];
		for(int i=1;i<n;i++) cout<<a[i];
		cout<<endl;
	}
    return 0;
}
