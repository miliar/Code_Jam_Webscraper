#include <iostream>
#include <map>
#define int long long
using namespace std;

map<int,int> cnt;

signed main(){
	int n,t,k;
	cin >> t;
	for(int a = 0;a < t;a++){
		int sum = 0;
		cin >> n >> k;
		cnt.clear();
		cnt[n] = 1;
		for(auto it = cnt.rbegin();it != cnt.rend();it++){
			int a = it->first,b = it->second;
			cnt[(a - 1) / 2] += b;
			cnt[a / 2] += b;
		}
		for(auto it = cnt.rbegin();it != cnt.rend();it++) {
			sum += it->second;
			if(sum >= k){
				cout << "Case #" + to_string(a + 1) + ": " + to_string(it->first / 2) + " " + to_string((it->first - 1) / 2) << endl;
				break;
			}
		}
	}
	return 0;
}