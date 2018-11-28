#include<bits/stdc++.h>
using namespace std;
#define err(x) cout<<#x<<"= "<<x<<endl;
#define FOR(i,a,b) for(int i =a; i< b; ++i)
#define rep(i,n) FOR(i,0,n)
#define pb push_back
#define INF 1000000000
#define TRVI(it,it1,it2) for(vi::iterator it = it1; it!= it2; it++)
#define ff first
#define ss second
#define mp make_pair
#define pq priority_queue<int, vector<int>, greater<int> >
#define ll long long
const ll PR = 1000000009;
#define SIZE 1
#define vi vector<int>
#define pii pair<int,int>
#define endl '\n'
#define db long double

int main(){
//	#ifdef ONLINE_JUDGE
//	freopen("a.in", "r" , stdin);
//	freopen("a.out", "w", stdout);
//      cin.tie(false); cout.tie(false);	
//	#endif
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	rep(t1,t){
		ll n;db D,K[1009],S[1009];
		db ans =1e18; 
		cin>>D>>n;
		rep(i,n){
			cin>>K[i]>>S[i];
			ans = min(ans, (D/(D-K[i]))*S[i]);
		}
		cout<<"Case #"<<t1+1<<": "<<fixed<<ans<<endl;
	}


	return 0;
};
