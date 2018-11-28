#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main() {
    int T;
    int ans;
    cin >> T;
    for (int t = 0 ; t < T; ++t) {
	int K;
	string state_s;
	vector<int> state_i;
	cin >> state_s >> K;
	for (int i = 0; i < state_s.size(); ++i) {
	    state_i.push_back(state_s[i]=='+'?1:0);
	}
#if 0
	cout << state_s << endl;
	for (int i = 0; i < state_i.size(); ++i) cout << state_i[i];
	cout << endl;
#endif
	ans = 0;
	for (int i = 0 ; i +K-1 < state_i.size(); ++i) {
	    if (state_i[i] == 1) continue;
	    ans++;
	    for (int j = 0; j < K; ++j) {
		state_i[i+j]^=1;
	    }
	}
	for (int i = 0 ; i < state_i.size(); ++i) {
	    if (state_i[i]==0) ans = -1;
	}
	if (ans == -1) 
	    cout << "Case #" << (t+1) << ": IMPOSSIBLE" << endl;
	else
	    cout << "Case #" << (t+1) << ": " << ans << endl;
    }

    return 0;
}
