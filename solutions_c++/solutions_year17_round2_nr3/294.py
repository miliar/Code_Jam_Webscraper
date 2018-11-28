#include <bits/stdc++.h>
using namespace std;
const int N = 105;
const long long inf=1e17+17;
const double eps=1e-7;
int t;
int n , q;
int e[N] , s[N];
long long d[N][N];
double dist[N];
priority_queue < pair < double , int > > pq;
void solve(int a,int b){
	while(!pq.empty()){
		pq.pop();
	}
	for(int i =1; i<= n ;++i){
		dist[i]=inf;
	}
	dist[a] = 0;
	pq.push({0 , a});
	while(!pq.empty()){
		int node = pq.top().second;
		double cost = -pq.top().first;
		pq.pop();
		for(int i =1 ; i <= n; ++i){
			if(d[node][i] <= e[node]){
				double weight = cost + (1.0 * d[node][i] / s[node]);
				if(dist[i]>weight+eps){
					dist[i]=weight;
					pq.push({-weight , i});
				}
			}
		}
	}
	printf(" %.6lf" , dist[b]);
}
int main(){
	cin>>t;
	for(int tc= 1; tc <= t; ++tc){
		cout << "Case #" << tc <<":";
		cin >>n >>q;
		for(int i = 1; i <= n ; ++i){
			cin>>e[i] >> s[i];
		}
		for(int i = 1 ; i <= n ; ++i){
			for(int j = 1 ; j <= n ; ++j){
				cin >> d[i][j];
				if(d[i][j]==-1){
					d[i][j]=inf;
				}
			}
		}
		for(int k=1;k<=n;++k){
			for(int i = 1; i <= n ; ++i){
				for(int j = 1 ; j <= n ; ++j){
					d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
				}
			}
		}
		while(q--){
			int a ,b;
			cin>>a>>b;
			solve(a,b);
		}
		cout<<endl;
	}
}