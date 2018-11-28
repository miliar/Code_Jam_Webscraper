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
		
		int n,p;
		int r[52];
		int q[52][52];
		scanf("%d%d",&n,&p);
		rep(i,n)scanf("%d",&r[i]);
		rep(i,n)rep(j,p){
			scanf("%d",&q[i][j]);
		}
		
		priority_queue<P> que[52];
		rep(i,n){
			rep(j,p){
				int x = (q[i][j]*10+r[i]*11-1)/(r[i]*11);
				int y = q[i][j]*10/(r[i]*9);
				if(x <= y)que[i].push(P(y,x));
				//cout << x << " " << y << endl;
			}
		}
		
		int ret = 0;
		while(1){
			int a = 0 , b = 1000000000 , c = -1;
			bool t = false;
			rep(i,n){
				if(que[i].empty()){
					t = true;
					break;
				}
				if(a < que[i].top().sc){
					a = que[i].top().sc;
					c = i;
				}
				if(b > que[i].top().fr){
					b = que[i].top().fr;
				}
			}
			if(t)break;
			if(a <= b){
				ret ++;
				rep(i,n)que[i].pop();
			}
			else{
				que[c].pop();
			}
		}
		printf("%d\n",ret);
	}
}
