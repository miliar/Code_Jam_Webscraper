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

bool chk(ll a){
	ll prev = 9;
	while(a){
		if(a%10 >prev)return 0;
		else prev = a%10;
		a/=10;
	}
	return 1;
}
ll solve(ll a){
	if(chk(a)){
		return a;
	}
	ll b=  a/10ll;
	b = solve(b-1);
//	if(!fl)b--;
//	fl = 1;
	return b*10ll +9ll;
}


int main(){
//	#ifdef ONLINE_JUDGE
//	freopen("a.in", "r" , stdin);
//	freopen("a.out", "w", stdout);
//      cin.tie(false); cout.tie(false);	
//	#endif
	ios::sync_with_stdio(false);
	ll t,n,ans;
	cin>>t;
	rep(t1,t){
		cin>>n;
		ans = solve(n);
		cout<<"Case #"<<t1+1<<": "<<ans<<endl;
	}


	return 0;
};
