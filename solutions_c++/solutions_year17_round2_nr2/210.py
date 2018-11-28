#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, R, O, Y, G, B, V;

int T;

vector<char> ans;
int a[3];
bool ansflag;

char ch[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};

int trans[3], start_c;

void search(int lastc) {
	if (a[0] == 0 && a[1] == 0 && a[2] == 0)
		return;
	int id = -1, max_v = 0;
	for (int i = start_c; i < start_c + 3; ++i) {
		if (lastc == i % 3)
			continue;
		if (a[i % 3] > max_v) {
			id = i % 3;
			max_v = a[i % 3];
		}
	}
	if (id == -1) {
		ansflag = false;
		return;
	}
	--a[id];
	ans.push_back(ch[id * 2]);
	search(id);
}

int main() {
	int T0 = 0;
	cin >> T;
	for ( ; T; --T) {
		ansflag = true;
		ans.clear();
		cin >> N >> R >> O >> Y >> G >> B >> V;
		//GVO RYB
		R -= G;
		Y -= V;
		B -= O;
		if (R < 0 || Y < 0 || B < 0) {
			printf("Case #%d: IMPOSSIBLE\n", ++T0);
			continue;
		}

		if (R >= Y && R >= B) {
			start_c = 0;
		}
		else if (Y >= R && Y >= B) {
			start_c = 1;
		}
		else if (B >= Y && B >= R) {
			start_c = 2;
		}
		a[0] = R;
		a[1] = Y;
		a[2] = B;
		search(-1);
		printf("Case #%d: ", ++T0);
		if (ansflag) {
			bool flagR = 0;
			bool flagY = 0;
			bool flagB = 0;
			for (int i = 0; i < ans.size(); ++i) {
				if (ans[i] == 'R') {
					flagR = 1;
				}
				if (ans[i] == 'Y') {
					flagY = 1;
				}
				if (ans[i] == 'B') {
					flagB = 1;
				}
			}
			if ((!flagR) && (G > 0) && (Y > 0 || V > 0 || B > 0 || O > 0) || (!flagY) && (V > 0) && (R > 0 || G > 0 || B > 0 || O > 0) || (!flagB) && (O > 0) && (R > 0 || G > 0 || Y > 0 || V > 0)) {
				printf("IMPOSSIBLE\n");
				continue;
			}
			while (G > 0 && !flagR) {
				ans.insert(ans.begin(), 'R');
				ans.insert(ans.begin(), 'G');
				--G;
			}
			while (V > 0 && !flagY) {
				ans.insert(ans.begin(), 'Y');
				ans.insert(ans.begin(), 'V');
				--V;
			}
			while (O > 0 && !flagB) {
				ans.insert(ans.begin(), 'B');
				ans.insert(ans.begin(), 'O');
				--O;
			}
			for (int i = 0; i < ans.size(); ++i)
				if (ans[i] == 'R') {
					while (G > 0) {
						ans.insert(ans.begin() + i + 1, 'R');
						ans.insert(ans.begin() + i + 1, 'G');
						--G;
					}
				}
			for (int i = 0; i < ans.size(); ++i)
				if (ans[i] == 'Y') {
					while (V > 0) {
						ans.insert(ans.begin() + i + 1, 'Y');
						ans.insert(ans.begin() + i + 1, 'V');
						--V;
					}
				}
			for (int i = 0; i < ans.size(); ++i)
				if (ans[i] == 'B') {
					while (O > 0) {
						ans.insert(ans.begin() + i + 1, 'B');
						ans.insert(ans.begin() + i + 1, 'O');
						--O;
					}
				}
			if (ans[0] == ans[ans.size() - 1] && ans.size() > 1) {
				printf("IMPOSSIBLE\n");
			}
			else {
				for (int i = 0; i < N; ++i)
					printf("%c", ans[i]);
				puts("");
			}
		}
		else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}