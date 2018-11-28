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
#define SIZE 1009
#define vi vector<int>
#define pii pair<int,int>
#define endl '\n'
#define db long double
const db PI=  3.14159265358979323846264;


db R[SIZE],H[SIZE], crs[SIZE];

int cmp(int a, int b){
	return R[a]> R[b];
}

int main(){
//	#ifdef ONLINE_JUDGE
//	freopen("a.in", "r" , stdin);
//	freopen("a.out", "w", stdout);
//      cin.tie(false); cout.tie(false);	
//	#endif
	ios::sync_with_stdio(false);
	int t,idx[1009];
	cin>>t;
	rep(t1, t){
		int n, k;
		multiset<db > areas;
		db ans= 0;
		cin>>n>>k;
		int max1=0;
//		k--;
		rep(i,n){
			cin>>R[i]>>H[i];
			crs[i] = PI*2*R[i]*H[i];
			areas.insert(crs[i]);
			idx[i] = i;
		}
		sort(idx, idx+n, cmp);
		
		for(int i =0; i< n-k+1; i++){
			db now = PI* R[idx[i]]*R[idx[i]]+ crs[idx[i]];
		//	cout<<idx[i]<<' '<<now<<endl;
			areas.erase(areas.find(crs[idx[i]]));
			int cnt=0;
			for( multiset<db > :: iterator it = areas.end(); cnt!= k-1; cnt++){
				it--;
				now+= *it;
			}
			ans = max(now,ans);
		}

		
		cout<<"Case #"<<t1+1<<": "<<setprecision(9)<<fixed<<ans<<endl;
	}


						

	return 0;
};
