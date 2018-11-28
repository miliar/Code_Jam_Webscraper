#include <iostream>
#include <string>
using namespace std;
void solve() {
	string s;
	int K;
	cin >> s >> K;
	int res = 0;
	for(int i = 0; i <= s.size() - K;) {
		while(i < s.size() - K && s[i] == '+')
			i++;
		if(s[i] == '+')
			break;
		for(int j = 0; j < K; j++)
			s[j + i] = s[j + i] == '+' ? '-' : '+';
		res++;
	}
	for(char c: s)
		if(c == '-') {
			cout << "IMPOSSIBLE\n";
			return;
		}
	cout << res << '\n';
}
int main(int argc, char *argv[]) {
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}