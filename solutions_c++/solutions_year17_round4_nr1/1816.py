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

inline int gif(int a, int b){
	int ret = a/b;
	if(a%b)ret++;
	return ret;
}
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
		int n,p,s,a=0,b=0,c=0,d=0;
		cin>>n>>p;
		if(p==2){
			rep(i,n){
				cin>>s;
				if(s%2)b++;
				else a++;
			}

		cout<<"Case #"<<t1+1<<": ";
			cout<<a+gif(b,2)<<endl;
		}
		if(p==3){
			rep(i,n){
				cin>>s;
				if(s%3 ==0){
					a++;
				}
				else if(s%3==1)b++;
				else c++;
			}
			int ans = a;
			int e = max(b,c)- min(b,c);
			ans+= min(b,c) + gif(e,3);
		
		cout<<"Case #"<<t1+1<<": "<<ans<<endl;
		}
		if(p==4){
			rep(i,n){
				cin>>s;
				s = s%4;
				if(s==0)a++;
				else if(s==1)b++;
				else if(s==2)c++;
				else d++;
			}
			int ans = a;
			ans+= min(b,d);
			int e = max(b,d)- min(b,d);
			int f = min(e/2,c),rem13 = e-2*(e/2);
			ans+= f;
			if(e/2 > c){
				ans += gif(rem13+(e/2)-f,4);
			}
			else if(e/2 < c){
				ans += gif(c-f,2);
				if((c-f)%2==0)ans+= rem13;
			}
			else {
				ans+= rem13;
			}
	
		cout<<"Case #"<<t1+1<<": "<<ans<<endl;
		}
	}


	return 0;
};
