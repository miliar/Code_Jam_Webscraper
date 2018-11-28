#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl '\n'
typedef long long ll;
using namespace std;

int main(){
	// ios_base::sync_with_stdio(false);
	// cin.tie(0);
	int T;
	cin>>T;
	for (int tc=0; tc<T; tc++){
		ll N,K;
		cin>>N>>K;
		set<ll,greater<ll>> intervals;
		unordered_map<ll,ll> freq;
		freq[N+2]=1;
		intervals.insert(N+2);
		while(K>1){
			ll next=*intervals.begin();
			ll curFreq=freq[next];
			// cout<<"p"<<next<<" "<<curFreq<<" "<<K<<endl;
			if(K<=curFreq){
				// cout<<"break "<<curFreq<<" "<<K<<endl;
				break;
			} else{
				intervals.erase(intervals.begin());
				ll mid=(next+1)/2;
				ll i1=next-mid+1;
				ll i2=mid;
				K-=curFreq;
				intervals.insert(i1);
				intervals.insert(i2);
				freq[i1]+=curFreq;
				freq[i2]+=curFreq;
				freq[next]=0;
			}
		}
		ll final=*intervals.begin();
		// cout<<final<<endl;
		ll fmid=(final+1)/2;
		ll f1=fmid-2;
		ll f2=final-fmid-1;
		cout<<"Case #"<<tc+1<<": "<<max(f1,f2)<<" "<<min(f1,f2)<<endl;
	}
}