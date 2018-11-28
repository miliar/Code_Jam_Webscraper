/* ***********************************************
Author        :yuanzhaolin
Created Time  :2017/4/23 0:45:55
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
int a[10];
int n;
vector<string> v[100];
string ans;
bool res;
char c[6]={'R','O','Y','G','B','V'};
int t[100]={0,2,4};
int d[100]={3,5,1};
vector<string> tmp;
bool cmp(vector<string> v1,vector<string> v2)
{
	return v1.size()>v2.size();
}
void solve()
{
	res=true;
	for(int i=0;i<3;i++)
	{
		if(a[t[i]]<a[d[i]]) 
		{
			res=false;
			return ;
		}
		if(a[t[i]]==0) continue;
		if(a[t[i]]==a[d[i]])
		{
			if(a[t[i]]+a[d[i]]==n)	
			{
				for(int j=0;j<a[t[i]];j++)
				{
					ans+=c[t[i]];
					ans+=c[d[i]];
				}
				return ;
			}
			else
			{
				res=false;
				return ;
			}
		}
		string s="";
		s+=c[t[i]];
		for(int j=0;j<a[d[i]];j++)
		{
			s+=c[d[i]];
			s+=c[t[i]];
		}
		v[i].push_back(s);
		for(int j=0;j<a[t[i]]-1-a[d[i]];j++)
		{
			s="";
			s+=c[t[i]];
			v[i].push_back(s);
		}
	}
	sort(v,v+3,cmp);
	int sum=v[0].size()+v[1].size()+v[2].size();
	if(v[0].size()*2>sum) 
	{
		res=false;
		return ;
	}
	int num1=v[0].size()-v[1].size();
	for(int i=0;i<num1;i++)
	{
		ans+=v[0][i];
		ans+=v[2][i];
	}
	for(int i=num1;i<v[2].size();i++)
	{
		ans+=v[0][i];
		ans+=v[1][i-num1];
		ans+=v[2][i];
	}
	for(int i=v[2].size();i<v[0].size();i++)
	{
		ans+=v[0][i];
		ans+=v[1][i-num1];
	}
	return ;
}
int main()
{
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
   	int T; 
   	cin>>T;
   	for(int ca=1;ca<=T;ca++)
	{
		cin>>n;
		ans="";
		for(int i=0;i<6;i++) 
		{
			cin>>a[i];
			v[i].clear();
		}
		solve();				
		printf("Case #%d: ",ca);
		if(!res) printf("IMPOSSIBLE\n");
		else cout<<ans<<endl;
	}
    return 0;
}
