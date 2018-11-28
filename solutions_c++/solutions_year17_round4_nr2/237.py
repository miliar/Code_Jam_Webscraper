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

int main(){
	int T;
	scanf("%d",&T);
	rep1(ppp,T){
		printf("Case #%d: ",ppp);
		
		int n,c,m;
		int p[1002],b[1002];
		scanf("%d%d%d",&n,&c,&m);
		rep(i,m)scanf("%d%d",&p[i],&b[i]);
		
		int cnt_p[1002] = {};
		int cnt_b[1002] = {};
		rep(i,m){
			cnt_p[p[i]] ++;
			cnt_b[b[i]] ++;
		}
		
		int sum[1002] = {};
		rep1(i,n){
			sum[i] = sum[i-1] + cnt_p[i];
		}
		
		int y = 0;
		rep1(i,c)y = max ( y , cnt_b[i] );
		rep1(i,n){
			y = max ( y , (sum[i]+i-1)/i );
		}
		int z = 0;
		rep1(i,n){
			z += max ( 0 , cnt_p[i]-y );
		}
		
		printf("%d %d\n",y,z);
	}
}

