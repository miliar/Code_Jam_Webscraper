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

int main(){
//	#ifdef ONLINE_JUDGE
//	freopen("a.in", "r" , stdin);
//	freopen("a.out", "w", stdout);
//      cin.tie(false); cout.tie(false);	
//	#endif
	ios::sync_with_stdio(false);
	char A[2000];
	int n,t,k,ans=1;
	cin>>t;
	rep(t1,t){
		cin>>A>>k;
		n = strlen(A);
		ans = 1;
		int cnt= 0;
		rep(i,n-k+1){
			if(A[i] == '-'){
				for(int j = i; j<k+i; j++){
					if(A[j]=='+')A[j] = '-';
					else A[j] = '+';
				}
				cnt++;
			}
		}
		rep(i,n)
			if(A[i] == '-')ans=0;
		cout<<"Case #"<<t1+1<<": ";
		if(ans)cout<<cnt<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}


	return 0;
};
