#include<bits/stdc++.h>
using namespace std;
#define int long long

void solve(int input_num){
	int n;
	cin >> n;
	while(n > 1){
		string str = to_string(n);
		string tmp = str;
		sort(tmp.begin(), tmp.end());
		if(str == tmp)break;
		n--;
	}
	
	cout << "Case #" << input_num << ": " << n << endl;
}

signed main(){
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++){
		solve(i);
	}
}