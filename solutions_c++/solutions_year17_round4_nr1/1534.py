#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int mem[4][101][101][101];
int P;

int go(int r, int r1, int r2, int r3)
{
	if (r1 < 0 || r2 < 0 || r3 < 0) return -1;
	if (r1 == 0 && r2 == 0 && r3 == 0) return 0;
	int& ret = mem[r][r1][r2][r3];
	if (ret != -1) return ret;
	return ret = max({ go((r + 1) % P, r1 - 1, r2, r3), go((r + 2) % P, r1, r2 - 1, r3), go((r + 3) % P, r1, r2, r3 - 1) }) + (r ? 0 : 1);
}

int main()
{
	ios_base::sync_with_stdio(false);
	int TC;
	cin >> TC;
	for (int tc =1; tc <=TC; ++tc) {
		cout << "Case #" << tc << ": ";
		int N;
		int ANS = 0;
		cin >> N >> P;
		vector<int> rem(4, 0);
		for (int i = 0; i < N; ++i) {
			int G;
			cin >> G;
			G = (P - (G % P)) % P;
			rem[G]++;
		}
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j <= 100; ++j) {
				for (int k = 0; k <= 100; ++k) {
					for (int l = 0; l <= 100; ++l) {
						mem[i][j][k][l] = -1;
					}
				}
			}
		}
		ANS = go(0, rem[1], rem[2], rem[3]) + rem[0];
		cout << ANS << '\n';
	}
}