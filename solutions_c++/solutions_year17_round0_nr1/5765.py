#include<iostream>
#include<string>
using namespace std;
int T;
string S;
int K;

int main()
{
	cin >> T;
	for (int now_case = 1;now_case <= T;++now_case) {
		cin >> S >> K;
		int ans = 0;
		int len = S.size();
		for (int i = 0;i <= len - K;++i) {
			if (S[i] == '+') continue;
			int nxt = -233;
			for (int j = 0;j < K;++j) {
				if (S[i + j] == '-') S[i + j] = '+';
				else {
					S[i + j] = '-';
					if (nxt == -233) nxt = i + j - 1;
				}
			}
			++ans;
		}
		int flg;
		for (flg = len - K + 1;flg < len;++flg) {
			if (S[flg] == '-') break;
		}
		cout << "Case #" << now_case << ": ";
		if (flg >= len) cout << ans << '\n';
		else cout << "IMPOSSIBLE\n";
	}
	return 0;
}