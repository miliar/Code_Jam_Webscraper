#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

unsigned long int res = 0;

bool dfs(vector<int> &digs, int pos, bool flag) {
	if(pos >= digs.size()){
		return true;
	}
	
	if(flag){
		res = res*10 + 9;
		return dfs(digs, pos+1, flag);
	}
	
	for(int sub = 0; sub <= 1 && (digs[pos] - sub >= 0); sub++){
		int prev_dig = res%10;
		res = res*10 + digs[pos] - sub;
		if(prev_dig <= (digs[pos]-sub) && dfs(digs, pos+1, (sub==1))){
			return true;
		}
		res = res/10;
	}

	return false;
}

int main(){
	unsigned long int N;
	int t;
	cin >> t;
	for(int z = 1; z <= t; z++){
		res = 0;
		cout << "Case #" << z << ": ";
		cin >> N;
		vector<int> digs;
		while(N){
			digs.push_back(N%10);
			N /= 10;
		}
		reverse(digs.begin(), digs.end());
		if(dfs(digs, 0, 0)){
			cout << res << endl;
		}
	}

	return 0;
}
