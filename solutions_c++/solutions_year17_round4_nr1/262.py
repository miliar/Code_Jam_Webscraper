#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<stack>
#include<cstdio>
#include<cmath>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> P;
typedef pair<int,P> P1;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define rep(i,x) for(int i=0;i<x;i++)
#define rep1(i,x) for(int i=1;i<=x;i++)
#define rrep(i,x) for(int i=x-1;i>=0;i--)
#define rrep1(i,x) for(int i=x;i>0;i--)
#define sor(v) sort(v.begin(),v.end())
#define rev(s) reverse(s.begin(),s.end())
#define lb(vec,a) lower_bound(vec.begin(),vec.end(),a)
#define ub(vec,a) upper_bound(vec.begin(),vec.end(),a)
#define uniq(vec) vec.erase(unique(vec.begin(),vec.end()),vec.end())
#define mp1(a,b,c) P1(a,P(b,c))

const int INF=1000000000;
const int dir_4[4][2]={{1,0},{0,1},{-1,0},{0,-1}};
const int dir_8[8][2]={{1,0},{1,1},{0,1},{-1,1},{-1,0},{-1,-1},{0,-1},{1,-1}};

int f(int a,int b,int c){
	if(a <= c){
		return a+b/2;
	}
	int ret = c;
	a -= c;
	ret += max(a/4+b/2,1+(a-2)/4+(b-1)/2);
	return ret;
}

int main(){
	int T;
	scanf("%d",&T);
	rep1(ppp,T){
		printf("Case #%d: ",ppp);
		
		int n,p;
		int g[102];
		scanf("%d%d",&n,&p);
		rep(i,n)scanf("%d",&g[i]);
		
		int sum = 0;
		int cnt[4] = {};
		rep(i,n){
			cnt[g[i]%p] ++;
			sum += g[i];
		}
		
		int ans = cnt[0];
		if(p == 2){
			ans += cnt[1]/2;
		}
		if(p == 3){
			ans += min(cnt[1],cnt[2]);
			ans += abs(cnt[1]-cnt[2])/3;
		}
		if(p == 4){
			ans += max(f(cnt[1],cnt[2],cnt[3]),f(cnt[3],cnt[2],cnt[1]));
		}
		if(sum%p != 0)ans ++;
		
		printf("%d\n",ans);
	}
}

