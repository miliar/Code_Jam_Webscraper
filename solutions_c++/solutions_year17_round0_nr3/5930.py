#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define pb push_back
#define MP make_pair
const double EPS = (1e-7);
typedef long long ll;
int main() {
#ifndef ONLINE_JUDGE
	freopen("C-small-1-attempt7.in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int t;
	scanf("%d",&t);
	for(int i = 1 ; i <= t ; ++i){
		cout << "Case #"<<i<<": ";
		int n , k;
		scanf("%d %d",&n,&k);
		if(n == k){
			cout << 0 << " " << 0<<endl;
			continue;
		}
		bool arr[n+2]={0};
		arr[0]=arr[n+1]=1;
		for(int j = 0 ; j < k ; ++j){
			int mn=-1;
			vector<pair<int,int> >v;
			vector<int>index;
			for(int d = 1 ; d <= n ; ++d){
				if(arr[d] == 0){
					int L = 0 , R = 0;
					for(int m = d-1 ; m >= 0 ; --m){
						if(arr[m]==0)L++;
						else break;
					}
					for(int m = d+1 ; m <= n ; ++m){
						if(arr[m]==0)R++;
						else break;
					}
					mn=max(min(L,R),mn);
					v.pb(MP(L,R));
					index.pb(d);
				}
			}
			vector<pair<int,int> >v2;
			vector<int>index3;
			for(int m = 0 ; m < v.size() ; ++m){
				if(min(v[m].F,v[m].S)==mn){
					v2.pb(v[m]);
					index3.pb(index[m]);
				}
			}
			int ans1=0 , ans2=0;
			//cout << v2[0].S<<" "<< j <<" " <<v2.size()<< endl;
			if(v2.size() == 1){
				arr[index3[0]]=1;
				ans1 = v2[0].F;
				ans2 = v2[0].S;
			}
			else{
				vector<pair<int,int> >v3;
				vector<int>index2;
				int mx=0;
				for(int m = 0 ; m < v2.size() ; ++m)mx=max(max(v2[m].F,v2[m].S),mx);
				for(int m = 0 ; m < v2.size() ; ++m){
					if(max(v2[m].F,v2[m].S)==mx){
						v3.pb(v2[m]);
						index2.pb(index3[m]);
					}
				}
				arr[index2[0]]=1;
				ans1=v3[0].F;
				ans2=v3[0].S;
			}
			if(j == k-1){
				cout << max(ans1,ans2) << " " << min(ans1,ans2)<<endl;
			}
		}
	}
	return 0;
}
