#include<bits/stdc++.h>

using std::pair;
using std::vector;

struct seg {
	int s, e, idx;
	bool operator<(const seg& p)const {
		return s < p.s;
	}
	int len() {
		int ret = e - s;
		if (ret < 0) {
			ret += 1440;
		}
		return ret;
	}
};


int main() {
	int tc;
	scanf("%d", &tc);
	int T = 0;
	while (tc--) {
		int p, q;
		scanf("%d%d", &p, &q);
		vector<seg> S;
		int A = 0;
		int B = 0;
		for (int i = 0; i < p; i++) {
			int a, b;
			scanf("%d%d", &a, &b);
			a %= 1440;
			b %= 1440;
			S.push_back({ a,b ,1});
			A += S.back().len();
		}
		for (int i = 0; i < q; i++) {
			int a, b;
			scanf("%d%d", &a, &b);
			a %= 1440;
			b %= 1440;
			S.push_back({ a,b,-1 });
			B += S.back().len();
		}
		std::sort(S.begin(), S.end());
		vector<seg> e;
		int cnt = 0;
		int sum = 0;
		int P = 0;
		int Q = 0;
		for (int i = 0; i < S.size(); i++) {
			if (S[i].e != S[(i + 1) % S.size()].s) {
				e.push_back({ S[i].e,S[(i + 1) % S.size()].s ,S[i].idx + S[(i + 1) % S.size()].idx });
			}
			if (S[i].idx + S[(i + 1) % S.size()].idx == 0) {
				cnt++;
				int len = S[(i + 1) % S.size()].s - S[i].e;
				if (len < 0) {
					len += 1440;
				}
				sum += len;
			}
			else if (S[i].idx + S[(i + 1) % S.size()].idx == 2) {
				int len = S[(i + 1) % S.size()].s - S[i].e;
				if (len < 0) {
					len += 1440;
				}
				A += len;
			}
			else if (S[i].idx + S[(i + 1) % S.size()].idx == -2) {
				int len = S[(i + 1) % S.size()].s - S[i].e;
				if (len < 0) {
					len += 1440;
				}
				B += len;
			}
		}
		if (A + sum < 720) {
			std::priority_queue<int> heap;
			for (seg s : e) {
				if (s.idx == -2) {
					heap.push(s.len());
				}
			}
			while (A+sum<720) {
				cnt+=2;
				A += heap.top();
				heap.pop();
			}
		}
		if (B + sum < 720) {
			std::priority_queue<int> heap;
			for (seg s : e) {
				if (s.idx == 2) {
					heap.push(s.len());
				}
			}
			while (B + sum<720) {
				cnt+=2;
				B += heap.top();
				heap.pop();
			}
		}
		T++;
		printf("Case #%d: %d\n", T, cnt);
	}
}