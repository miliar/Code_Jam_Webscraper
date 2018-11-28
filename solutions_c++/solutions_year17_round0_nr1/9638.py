#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int T;
ofstream out("ans.out");
int main()
{
	ifstream in("large.in");
	in >> T;
	for (int tcase = 0; tcase < T; tcase++) {
		int K; string S;
		in >> S >> K;
		int ans = 0;
		for (int i = 0; i <= S.length()-K; i++) {
			if (S[i] != '+') {
				ans++;
				for (int j = i; j < i + K; j++) {
					if (S[j] == '+') S[j] = '-';
					else S[j] = '+';
				}
			}
		}
		for (int i = 0; i < S.length(); i++) {
			if (S[i] != '+') {
				ans = -1; break;
			}
		}
		
		out << "Case #" << tcase + 1 << ": ";
		if (ans == -1) out << "IMPOSSIBLE\n";
		else out << ans << "\n";
	}

	return 0;
}