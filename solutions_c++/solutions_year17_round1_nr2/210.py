#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int Times;
char lineEnd[15];

int getmax(int a, int b) {
	return (a - 1) / b + 1;
}
int getmin(int a, int b) {
	return a / b;
}

struct Pair {
public:
	int l, r;
	Pair(int ll, int rr) {
		l = ll;
		r = rr;
	}
	Pair() {
		 l = 0;
		 r = 0;
	}
};

struct cmpcmp {
	inline bool operator()(const Pair &a, const Pair &b) {
		return a.l < b.l || (a.l == b.l && a.r < b.r);
	}
};

int main() {

    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);

    scanf("%d", &Times);
    gets(lineEnd);
    for (int times = 1; times <= Times; ++times) {
        printf("Case #%d: ", times);
        
        int n, p;
        int r[55];
		vector<vector<Pair> > pairs(55, vector<Pair>(0));

        scanf("%d%d", &n, &p);
        for (int i = 0; i < n; ++i) {
			scanf("%d", &r[i]);
		}
		int q;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < p; ++j) {
				scanf("%d", &q);
				int rr = getmin(q * 10, r[i] * 9);
				int ll = getmax(q * 10, r[i] * 11);
				
				if (ll > rr || rr <= 0) {
					continue;
				}
				pairs[i].push_back(Pair(ll, rr));
			}
			
			sort(pairs[i].begin(), pairs[i].end(), cmpcmp());
			/*
			for (int j = 0; j < pairs[i].size(); ++j) {
				printf("%d %d; ", pairs[i][j].l, pairs[i][j].r);
			}
			printf("\n");
			*/
		}
		
		vector<int> idx(50, 0);
		int ans = 0;
		while (true) {
			bool f = false;
			for (int i = 0; i < n; ++i) {
				if (idx[i] >= pairs[i].size()) {
					f = true;
					break;
				}
			}
			if (f) break;
			
			int p_h = 0, p_t = 0;
			for (int i = 1; i < n; ++i) {
				if (pairs[i][idx[i]].l > pairs[p_h][idx[p_h]].l) p_h = i;
				if (pairs[i][idx[i]].r < pairs[p_t][idx[p_t]].r) p_t = i;
			}
			if (pairs[p_t][idx[p_t]].r >= pairs[p_h][idx[p_h]].l) {
				ans += 1;
				for (int i = 0; i < n; ++i) idx[i] += 1;
				continue;
			}
			
			idx[p_t] += 1;
		}
		
		printf("%d\n", ans);

    }
	
    return 0;
}
