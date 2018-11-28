#include <bits/stdc++.h>

#define REP(i, n) for(int i = 0; i < n; i++)

using namespace std;




void testcase(int tcn){
	string s;
	cin >> s;
	int k = s.size();

	vector<int> n;
	n.resize(k);
	REP(i, k){
		n[i] = s[i] - '0';
	}

	bool changed = true;
	while(changed){
		changed = false;
		for(int i = 0; i < k-1; i++){
			if(n[i] > n[i+1]){
				changed = true;
				for(int j = i+1; j < k; j++)n[j] = 9;
				--n[i];
				while(n[i] == -1){
					n[i]=9;
					i--;
					--n[i];
				}
				break;
			}
		}

	}


	cout << "Case #"<<tcn<<": ";
	for(int i = 0; i < k; i++){
		if(i == 0 && n[i] == 0)continue;
		cout << n[i];
	}
	cout << endl;

}

int main(){
	int T;
	cin >> T;
	REP(i, T){
		testcase(i+1);
	}
	return 0;

}