#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main(){
	long long T;
	cin >> T;
	for (long long t = 0; t < T; t++){
		if (t != 0) cout << endl;
		long long N;
		cin >> N;
		vector<long long> digs(0);
		while (N > 0){
			digs.push_back(N % 10);
			N /= 10;
		}
		vector<long long> ans(0);
		long long first=-1;
		for (long long i = digs.size() - 1; i > 0; i--){
			if (digs[i] > digs[i - 1]){
				first = i;
				break;
			}
		}
		if (first != -1){
			while (first < digs.size()-1 && digs[first] == digs[first + 1]){ first++; }
		}
		long long ask = 0;
		for (long long i = digs.size() - 1; i >= 0; i--){
			if (i == first){
				ans.push_back(digs[i] - 1);
				continue;
			}
			if (i<first){
				ans.push_back(9);
				continue;
			}
			ans.push_back(digs[i]);
			ask = 1;
		}
		long long ANS = 0;
		for (long long i = 0; i <ans.size(); i++){
			ANS *= 10;
			ANS += ans[i];
		}
		cout << "Case #" << t + 1 << ": " << ANS;
	}
}