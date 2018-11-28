#include<iostream>
#include<algorithm>
#include<queue>
#include<cmath>
using namespace std;
int n,p,t;
int r[51];
vector<double>q[51];
int ptr[51];
int main(){
	ios::sync_with_stdio(false);
	//freopen("infile.in","r",stdin);
	//freopen("outfile.txt","w",stdout);
	cin >> t;
	for(int u=1; u<=t ;u++){
		cin >> n >> p;
		for(int i=1; i<=n ;i++) cin >> r[i];
		for(int i=1; i<=n ;i++){
			q[i].clear();
			q[i].push_back(0);
			for(int j=1; j<=p ;j++){
				q[i].push_back(0);
				cin >> q[i][j];
				q[i][j]/=r[i];
			}
			sort(q[i].begin()+1,q[i].end());
			ptr[i]=p;
		}
		int ans=0;
		for(int i=n*p; i>0 ;i--){
			double mini=2e9,maxi=0;
			int maxn,minn;
			for(int j=1; j<=n ;j++){
				if(q[j][ptr[j]]>maxi){
					maxi=q[j][ptr[j]];
					maxn=j;
				}
				if(q[j][ptr[j]]<mini){
					mini=q[j][ptr[j]];
					minn=j;
				}
			}
			if(floor(mini/9*10)>=ceil(maxi/11*10)){
				ans++;
				bool ok=true;
				for(int j=1; j<=n ;j++){
					ptr[j]--;
					if(ptr[j]==0) ok=false;
				}
				if(!ok) break;
			}
			else{
				ptr[maxn]--;
				if(ptr[maxn]==0) break;
			}
		}
		cout << "Case #" << u << ": " << ans << '\n';
	}
}
