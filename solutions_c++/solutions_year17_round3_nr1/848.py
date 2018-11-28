#include<iostream>
#include<algorithm>
#include<queue>
#include<cmath>
#include<iomanip>
using namespace std;
typedef long long ll;
int n,k,T;
priority_queue<ll,vector<ll>,greater<ll> >pq;
pair<ll,ll>a[1001];
long double pi=3.141592653589793238;
int main(){
	ios::sync_with_stdio(false);
	//freopen("infile.in","r",stdin);
	//freopen("outfile.txt","w",stdout);
	cin >> T;
	for(int t=1; t<=T ;t++){
		cin >> n >> k;
		for(int i=1; i<=n ;i++){
			cin >> a[i].first >> a[i].second;
		}
		sort(a+1,a+n+1);
		long long maxi=0,th=0;
		for(int i=1; i<=n ;i++){
			if(i<k){
				pq.push(a[i].second*a[i].first*2);
				th+=a[i].second*a[i].first*2;
				continue;
			}
			maxi=max(maxi,th+a[i].second*a[i].first*2+a[i].first*a[i].first);
			th+=a[i].second*a[i].first*2;
			pq.push(a[i].second*a[i].first*2);
			th-=pq.top();
			pq.pop();
		}
		while(!pq.empty()) pq.pop();
		cout << "Case #" << t << ": " << setprecision(25) << pi*maxi << '\n';
	}
}
