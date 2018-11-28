#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<map>
#include<set>
#include<cmath>
#include<cassert>
#include<queue>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
struct cww{cww(){ios::sync_with_stdio(false);cin.tie(0);}}star;

void solve() {
	int H, W;
	cin >> H >> W;
	vector<string> board(H);
	for (int i = 0; i < H; i++)
		cin >> board[i];
	int cur = 0;
	for (int i = 0; i < H; ) {
		vector<pair<int, char> > pos;
		for (int j = 0; j < W; j++) {
			if (board[i][j] != '?') {
				pos.emplace_back(j, board[i][j]);
			}
		}
		if (pos.empty()) {
			++i;
			continue;
		}
		int tar = 0;
		for (int k = 0; k < pos.size(); ++k) {
			char c = pos[k].second;
			int next = (k+1 == pos.size() ? W : pos[k+1].first);
			for (int j = tar; j < next; ++j)
				board[i][j] = c;
			tar = next;
		}
		int ni = i+1;
		for (; ni < H; ++ni) {
			bool ok = true;
			for (int j = 0; j < W; j++)
				if (board[ni][j] != '?') ok = false;
			if (!ok) break;
		}
		for (int h = cur; h < ni; ++h) {
			for (int j = 0; j < W; j++) {
				board[h][j] = board[i][j];
			}
		}
		i = ni;
		cur = ni;
	}
	for (int i = 0; i < H; i++)
		cout << board[i] << endl;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": " << endl;
		solve();
	}
	return 0;
}
