#include <bits/stdc++.h>
using namespace std;
const int N=55;
const int NN=1005;

int t,n,p,a[N],b[N][N];
int res[NN][NN],dist[NN];
int f,pre[NN];
queue<int> q;
vector<int> adj[NN];
map<int,vector<int>> mp[2];
bool valid[N][N];

void augment(int pos, int mx){
	if (!pos) f=mx;
	else if (pre[pos]!=-1){
		augment(pre[pos],
		min(mx,res[pre[pos]][pos]));
		res[pre[pos]][pos]-=f;
		res[pos][pre[pos]]+=f;
	}
}

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	cin >> t;
	for (int tc=1;tc<=t;tc++){
		cout << "Case #" << tc << ": ";
		cin >> n >> p;
		for (int i=1;i<=n;i++){
			cin >> a[i];
		}
		for (int i=0;i<=n*p+1;i++){
			adj[i].clear();
		}
		memset(valid,0,sizeof(valid));
		for (int i=1;i<=n;i++){
			mp[i&1].clear();
			for (int j=1;j<=p;j++){
				cin >> b[i][j];
				for (int k=(10*b[i][j]+11*a[i]-1)/(11*a[i]);
				k<=10*b[i][j]/(9*a[i]);k++){
					valid[i][j]=1;
					if (k){
						mp[i&1][k].push_back(j);
						if (i>1){
							for (int &x : mp[!(i&1)][k]){
								adj[(i-2)*p+x].push_back
								((i-1)*p+j);
								adj[(i-1)*p+j].push_back
								((i-2)*p+x);
								res[(i-2)*p+x][(i-1)*p+j]=1;
							}
						}
					}
				}
			}
		}
		for (int i=1;i<=p;i++){
			if (valid[1][i]){
				adj[0].push_back(i);
				adj[i].push_back(0);
				res[0][i]=1;
			}
			if (valid[n][i]){
				adj[(n-1)*p+i].push_back(n*p+1);
				adj[n*p+1].push_back((n-1)*p+i);
				res[(n-1)*p+i][n*p+1]=1;
			}
		}
		int mf=0;
		do{
			f=0;
			for (int i=1;i<=n*p+1;i++){
				pre[i]=-1;
				dist[i]=INT_MAX;
			}
			q.push(0);
			while (!q.empty()){
				int now=q.front();
				q.pop();
				for (int &nxt : adj[now]){
					if (dist[now]+1<dist[nxt]&&
					res[now][nxt]>0){
						dist[nxt]=dist[now]+1;
						q.push(nxt);
						pre[nxt]=now;
					}
				}
			}
			augment(n*p+1,INT_MAX);
			mf+=f;
		}while (f);
		cout << mf << "\n";
	}
}
