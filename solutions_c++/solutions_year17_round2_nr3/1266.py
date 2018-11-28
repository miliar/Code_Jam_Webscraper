#include <bits/stdc++.h>
using namespace std;

#define fr(i,a,b) for(int i = a; i < (b); i++) 
#define fi first
#define se second
#define pb push_back
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d %d", &a, &b)
#define sc3(a,b,c) scanf("%d %d %d", &a, &b)
#define pri(a) printf("%d\n", a)
#define mp make_pair
#define DESYNC ios_base::sync_with_stdio(false)

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef long long int ll;

const int INF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const int MOD = 1000000007;
const double PI = acos(-1);

int main(){
	int t, n, q, s, e;
	int dist[100][100];
	int range[100];
	int speed[100];
	bool vis[100];
	double mini[100];
	
	cin>>t;
	fr(num,1,t+1){
		cin>>n>>q;
		
		fr(i,0,n){
			cin>>range[i]>>speed[i];
		}
		fr(i,0,n){
			fr(j,0,n){
				cin>>dist[i][j];
			}
		}
		printf("Case #%d: ", num);
		fr(z,0,q){
			cin>>s>>e;
			s--; e--;
			memset(vis, 0, sizeof vis);
			mini[0] = 0;
			fr(i,0,n){
				double rng = range[i];
				double spd = speed[i];
				double mom = mini[i];
				fr(j,i,n){
					if(!vis[j]){
						vis[j] = 1;
						mini[j] = mom;
					}
					else{
						mini[j] = min(mini[j], mom); 
					}
					rng -= dist[j][j+1];
					mom += dist[j][j+1]/spd;
					if(rng < 0) break;
				}
			}
			printf("%.6lf\n", mini[e]);
		}
	}
}
