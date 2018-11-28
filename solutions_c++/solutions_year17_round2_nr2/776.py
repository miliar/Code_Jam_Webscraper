# include <bits/stdc++.h>

using namespace std;

int N, R, O, Y, G, B, V;

vector<char> ans;

bool solve2(int B, int R, int Y) {
	ans.clear();
	vector< pair<int, char> > vec;
	vec.push_back({B, 'B'});
	vec.push_back({R, 'R'});
	vec.push_back({Y, 'Y'});
	sort(vec.begin(), vec.end());
	reverse(vec.begin(), vec.end());
	if(vec[0].first > vec[1].first + vec[2].first) {
		return false;
	}
	int n = vec[0].first + vec[1].first + vec[2].first;
	ans.resize(n);
	for(int i = 0; i < n; ++i) ans[i] = 0;
	for(int i = 0, cnt = 0; i < n && cnt < vec[0].first; i += 2, ++cnt) {
		ans[i] = vec[0].second;
	}
	for(int i = n - 1, cnt = 0; i >= 0 && cnt < vec[1].first; i -= 2, ++cnt) {
		if(ans[i] != 0) --i;
		ans[i] = vec[1].second;
	}
	for(int i = 0; i < n; ++i) if(ans[i] == 0) ans[i] = vec[2].second;
	return true;
}

int main() {
	int T, cas = 0; scanf("%d", &T);
	while(T--) {
		scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
		printf("Case #%d: ", ++cas);
		if(R + O + V > N / 2 || Y + O + G > N / 2 || B + G + V > N / 2) {
			puts("IMPOSSIBLE");
			continue;
		}
		if(B == O && B + O == N) {
			for(int i = 0; i < N; ++i) putchar(i & 1 ? 'B' : 'O'); putchar('\n');
			continue;
		}
		if(R == G && R + G == N) {
			for(int i = 0; i < N; ++i) putchar(i & 1 ? 'R' : 'G'); putchar('\n');
			continue;
		}
		if(Y == V && Y + V == N) {
			for(int i = 0; i < N; ++i) putchar(i & 1 ? 'Y' : 'V'); putchar('\n');
			continue;
		}
		if(O > 0 && B <= O || G > 0 && R <= G || V > 0 && Y <= V) {
			puts("IMPOSSIBLE");
			continue;
		}
		set<char> normal;
		if(O > 0 && B > O) normal.insert('B');
		if(G > 0 && R > G) normal.insert('R');
		if(V > 0 && Y > V) normal.insert('Y');
		if(!solve2(B - O, R - G, Y - V)) {
			puts("IMPOSSIBLE");
			continue;
		} else {
			for(int i = 0; i < (int)ans.size(); ++i) {
				putchar(ans[i]);
				if(normal.count(ans[i])) {
					char c = ans[i];
					char r = (c == 'B') ? 'O' : ((c == 'R') ? 'G' : 'V');
					int cnt = (c == 'B') ? O : ((c == 'R') ? G : V);
					normal.erase(c);
					while(cnt--) {
						putchar(r);
						putchar(c);
					}
				}
			}
			puts("");
		}
	}
	return 0;
}

