#include <iostream>
#include <vector>
#include <algorithm>
#define int long long
using namespace std;

signed main(){
	int t,n;
	cin >> t;
	for(int a = 0;a < t;a++){
		vector<int> num;
		cin >> n;
		int ma = 0,res = 0,pow = 1;
		while(n){
			num.push_back(n % 10);
			n /= 10;
		}
		for(int i = 0;i < num.size() - 1;i++){
			if(num[i] < num[i + 1]){
				num[i + 1]--;
				num[i] = 9;
			}
		}
		for(int i = num.size() - 1;i >= 0;i--){
			ma = max(ma,num[i]);
			num[i] = ma;
		}
		for(int i = 0;i < num.size();i++){
			res += pow * num[i];
			pow *= 10;
		}
		cout << "Case #" + to_string(a + 1) + ": " + to_string(res) << endl;
	}
	return 0;
}