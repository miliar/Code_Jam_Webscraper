#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <cassert>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
typedef pair<int,P> P1;
typedef pair<P,P> P2;
#define pu push
#define pb push_back
#define mp make_pair
#define eps 1e-7
#define INF 1000000000
#define fi first
#define sc second
#define rep(i,x) for(int i=0;i<x;i++)
#define SORT(x) sort(x.begin(),x.end())
#define ERASE(x) x.erase(unique(x.begin(),x.end()),x.end())
#define POSL(x,v) (lower_bound(x.begin(),x.end(),v)-x.begin())
#define POSU(x,v) (upper_bound(x.begin(),x.end(),v)-x.begin())
int t;
int main()
{
	cin >> t;
	for(int r=1;r<=t;r++){
		int n,m; cin >> n >> m;
		string f[26],g[26];
		for(int i=0;i<n;i++){
			cin >> f[i]; g[i] = f[i];
		}
		vector<int>vi;
		vector<P>pos;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(f[i][j] != '?'){
					pos.pb(mp(i,j));
				}
			}
		}
		SORT(pos);
		int prev = -1,prev2 = -1;
		for(int i=0;i<pos.size();i++){
			if(i != pos.size()-1 && pos[i].fi == pos[i+1].fi){
				int x = n;
				for(int j=i+2;j<pos.size();j++){
					if(pos[j].fi != pos[i].fi){
						x = pos[j].fi; break;
					}
				}
				for(int j=prev+1;j<x;j++){
					for(int k=prev2+1;k<pos[i+1].sc;k++){
						f[j][k] = f[pos[i].fi][pos[i].sc];
					}
				}
				prev2 = pos[i+1].sc-1;
			}
			else{
				int x = (i!=pos.size()-1)?pos[i+1].fi:n;
				for(int j=prev+1;j<x;j++){
					for(int k=prev2+1;k<m;k++){
						f[j][k] = f[pos[i].fi][pos[i].sc];
					}
				}
				prev = pos[i+1].fi-1; prev2 = -1;
			}
		}
		printf("Case #%d:\n",r);
		for(int i=0;i<n;i++) cout << f[i] << endl;
		
		//CHECK
		for(int i=0;i<n;i++) for(int j=0;j<m;j++) if(g[i][j]!='?' && f[i][j] != g[i][j]) return 1;
		int a[30],b[30],c[30],d[30],e[30]={};
		for(int i=0;i<30;i++){
			a[i] = c[i] = INF;
			b[i] = d[i] = -INF;
		}
		for(int i=0;i<n;i++) for(int j=0;j<m;j++){
			int w = f[i][j]-'A'; e[w]++;
			a[w] = min(a[w],i); b[w] = max(b[w],i);
			c[w] = min(c[w],j); d[w] = max(d[w],j);
		}
		for(int i=0;i<26;i++){
			if(!e[i]) continue;
			if(e[i] != (b[i]-a[i]+1)*(d[i]-c[i]+1)) return 1;
		}
	}
}