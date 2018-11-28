#include <bits/stdc++.h>
#define fr(a,b,c) for(int a=b;a<c;a++)
#define X first
#define Y second
#define pb push_back
using namespace std;
typedef long long ll;
typedef pair<ll,int> pii;
typedef pair<double,int> pdi;
int arr[105][105];
int md[105],sp[105];
double mincost[105],edges[105][105];ll dist[105];
int main(){
int t;cin>>t;
	fr(T,1,t+1){
		int n,q;
		cin>>n>>q;
		fr(i,0,n){
			cin>>md[i]>>sp[i];
		}
		fr(i,0,n)fr(j,0,n){
			cin>>arr[i][j];
			edges[i][j]=1e50;
		}
		
		fr(i,0,n){
			fr(j,0,n)dist[j]=1e15;
			dist[i]=0;
			priority_queue<pair<ll,int>,vector<pii>,greater<pii> > pq;
			pq.push(pii(0,i));
			while(!pq.empty()){
				pii tp=pq.top();
				pq.pop();
				fr(j,0,n){
					if(~arr[tp.Y][j]){
						if(dist[j]>arr[tp.Y][j]+tp.X){
							dist[j]=arr[tp.Y][j]+tp.X;
							pq.push(pii(dist[j],j));
						}
					}	
				}
			}
			fr(j,0,n)if(dist[j]<=md[i])edges[i][j]=dist[j]/double(sp[i]);	
		}
		cout.precision(6);
		cout<<"Case #"<<T<<":";
		fr(Q,0,q){
			int a,b;
			cin>>a>>b;a--;b--;
			fr(j,0,n)mincost[j]=1e50;
			mincost[a]=0;
			priority_queue<pdi,vector<pdi>,greater<pdi> > pq;
			pq.push(pdi(0,a));
			while(!pq.empty()){
				pdi tp=pq.top();
				pq.pop();
				fr(j,0,n){
					if(mincost[j]>edges[tp.Y][j]+tp.X){
						mincost[j]=edges[tp.Y][j]+tp.X;
						pq.push(pdi(mincost[j],j));
					}
				}
			}
			cout<<fixed<<" "<<mincost[b];
		}
		cout<<endl;
	}
}

