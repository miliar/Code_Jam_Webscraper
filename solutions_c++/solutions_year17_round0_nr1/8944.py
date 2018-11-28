#include<bits/stdc++.h>

#define pii pair<int,int>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define pf push_front
#define pb2 pop_back
#define pf2 pop_front
#define line printf("\n")
#define pq priority_queue
#define rep(k,i,j) for(int k = (int)i;k<(int)j;k++)
#define repd(k,i,j) for(int k = (int)i;k>=(int)j;k--)
#define ll long long

using namespace std;

double EPS = 1e-9;
int INF = 1e9+7;;
long long INFLL = 1e17;
double pi = acos(-1);
int dirx[8] = {-1,0,0,1,-1,-1,1,1};
int diry[8] = {0,1,-1,0,-1,1,-1,1};

inline void OPEN (string s) {
  freopen ((s + ".in").c_str (), "r", stdin);
  freopen ((s + ".out").c_str (), "w", stdout);
}

//end of template

int t;
string s;
int m;
int main(){
	cin>>t;
	
	rep(tt,1,t+1){
		cin>>s>>m;
		
		int bisa = 1;
		int ret = 0;
		rep(k,0,s.size()){
			if(s[k]=='-'){
				if(k+m-1<=s.size()-1){
					ret++;
					rep(i,0,m)s[k+i] = (s[k+i]=='-')?'+':'-';
				}
				else bisa = 0;
			}
		}
		
		if(bisa)printf("Case #%d: %d\n",tt,ret);
		else printf("Case #%d: IMPOSSIBLE\n",tt);
	}
	return 0;
}
