#include <iostream>
#include <string.h>
#include <vector>
#include <string>
#include <limits.h>
using namespace std;

int main(int argc, char* argv[])
{
	if (argc >= 2) {
		FILE* fp = freopen(argv[1], "r", stdin);
	}

	int N;
	cin >> N;

	for (int i = 1; i <= N; i++) {
		char S[1024];
		cin >> S;
		int K;
		cin >> K;

		auto solve = [&]() {
			int k = 0;
			char* p = S;
			char* q = S + strlen(S);
			while (p < q) {
				if (*p == '-') {
					if (p + K > q) return -1;
					for (int i = 0; i < K; i++) {
						p[i] = (p[i] == '-') ? '+' : '-';
					}
					k++;
				}
				p++;
			}
			return k;
		};

		int result = solve();
		if (result >= 0) {
			cout << "Case #" << i << ": " << result << endl;
		} else {
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
