#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;

#include <iostream>
#include <string>
using namespace std;

int solve(int N) {
	while (N) {
		string s = to_string(N);
		bool good = 1;
		for (int i = 0; i < s.size() - 1; i++) {
			if (s[i] > s[i + 1]) {
				good = 0;
				break;
			}
		}
		if (good)
			return N;
		else N--;
	}
}

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T, N;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		cin >> N;
		cout << "Case #" << test << ": " << solve(N) << '\n';
	}
	return 0;
}
