#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <utility>

using namespace std;
typedef unsigned long long ll;

ll n, k, max_SS=0, min_SS=0, i;
vector< ll > vec;

//ll p[1000000000000000000+1];

void bs(ll left, ll right,ll v, ll lv){
	if(left > right) return;
	ll mid = (left+right)/2 ;

//	ll max_S, min_S; 
	if(v == k){
		max_SS = max(mid-left ,right-mid);
		min_SS = min(mid-left ,right-mid);
	}

	if(v%lv +2*lv == vec[i--]) bs(mid+1,right,v%lv +2*lv,lv*2);
	else bs(left,mid-1,v%lv +2*lv+lv,lv*2); 
//	cout << max_S << ' '<<min_S<<' '<<endl;
//	vec.push_back(make_pair(max_S,min_S));
//	push_heap (vec.begin(),vec.end());
//	
//	bs(mid+1,right);
//	bs(left,mid-1); 
}

bool comp(pair<ll,ll> a, pair<ll,ll> b){
	if(a.second > b.second) return true;
	else if(a.second == b.second) return a.first > b.first;
	else return false;
}



int main(){
	int t;
	cin >> t;
	for(int c = 1; c<=t;c++){
		cin >> n >> k;
		vec.clear();
		ll tmp = k, j = 1;
		while(tmp >= j){
			j *= 2;
		}
		j /= 2;
		vec.push_back(tmp);
		while(tmp != 1){
			tmp %= j;
			if(tmp < j/2){
				tmp += j/2;
			}
			j /= 2;
			vec.push_back(tmp);
//			cout << tmp << ' ';
		}
		i = vec.size() - 2;
		bs(1,n,1,1);

//		max_SS = vec[k-1].first; min_SS = vec[k-1].second;
		printf("Case #%d: %lld %lld\n",c,max_SS,min_SS);
	}
	
}
