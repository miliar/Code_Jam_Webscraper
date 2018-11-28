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
typedef pair<ll,ll> P;
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
		
		ll n,k;
		cin >> n >> k;
		k --;
		
		priority_queue<P> que;
		que.push(P(n,1));
		
		while(k > 0){
			P p = que.top(); que.pop();
			while(que.size()>0){
				if(que.top().fr != p.fr)break;
				p.sc += que.top().sc;
				que.pop();
			}
			ll x = min(k,p.sc);
			que.push(P(p.fr/2,x));
			que.push(P((p.fr-1)/2,x));
			if(p.sc>x)que.push(P(p.fr,p.sc-x));
			k -= x;
		}
		
		printf("%lld %lld\n",que.top().fr/2,(que.top().fr-1)/2);
	}
}

