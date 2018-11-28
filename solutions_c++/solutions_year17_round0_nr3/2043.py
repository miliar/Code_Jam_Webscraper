
#include <iostream>
#include <unordered_map>
#include <map>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pll;

map<ll,ll> len_num_map;

pair<ll,ll> lsmaxmin(ll L){
	return pair<ll,ll>((L-1)/2,L/2);
}

void add_to_map(ll a, ll b){
	len_num_map[a] += b;
}

pll ans(ll N, ll K){
	len_num_map.insert(pll(N,1));
	while(true){
		//for(auto it = len_num_map.begin(); it != len_num_map.end(); ++it){
			//cout << it->first << " " << it->second << endl;
		//}

		ll largest_len = len_num_map.rbegin()->first;
		ll largest_num = len_num_map.rbegin()->second;
	//cout << "largnum = "<< largest_num << " larglen = " << largest_len << endl;
	//cout << "K="<<K<<endl;
		
		if(K > largest_num){
			len_num_map.erase(largest_len);

			pll p = lsmaxmin(largest_len);

		//cout << "pf = " << p.first << " ps =  " << p.second << endl;

			add_to_map(p.first,largest_num);
			add_to_map(p.second,largest_num);

			K -= largest_num;
		}else{
			return lsmaxmin(largest_len);
		}
	}
}


int main(){
	int T;
	cin >> T;

	for(int tsc=0; tsc<T; tsc++){
		len_num_map.clear();
		ll N,K;
		cin >> N >> K;
		pll a = ans(N,K);
		cout << "Case #"<<tsc+1<<": "<<a.second<<" "<<a.first<<endl;
	}
}

