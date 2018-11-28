#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

char color[] = "ROYGBV";
const int p[] = {3, 4, 5, 0, 1, 2};
int N;
int a[6];

void solve()
{
    cin >> N;
    for(int i = 0; i < 6; ++ i) {
        cin >> a[i];
    }
    for(int i = 1; i < 6; i += 2) {
        if (a[p[i]] < a[i]) {
            puts("IMPOSSIBLE");
            return;
        }
        if (a[p[i]] == a[i] && a[i]) {
            if (a[p[i]] + a[i] != N) {
                puts("IMPOSSIBLE");
                return;
            }
            for(int j = 0; j < N; ++ j) {
                if (j & 1) putchar(color[i]);
                else putchar(color[p[i]]);
            }
            puts("");
            return;
        }
        a[p[i]] -= a[i];
    }

    vector<int> alive;
    for(int i = 0; i < 6; i += 2) {
        if (a[i]) alive.push_back(i);
    }
    vector<int> ans;
    if (alive.size() == 1) {
        if (a[alive[0]] > 1 || a[p[alive[0]]] > 0) {
            puts("IMPOSSIBLE");
            return;
        }
        ans.push_back(alive[0]);
    } else if (alive.size() == 2) {
        if (a[alive[0]] != a[alive[1]]) {
            puts("IMPOSSIBLE");
            return;
        }
        for(int i = 0; i < a[alive[0]] + a[alive[1]]; ++ i) {
            ans.push_back(alive[i & 1]);
        }
    } else {
        int argmax = 0;
        for(int i = 1; i < 3; ++ i) {
            if (a[alive[i]] > a[alive[argmax]]) {
                argmax = i;
            }
        }
        for(int i = 0; i < a[alive[argmax]]; ++ i) {
            ans.push_back(alive[argmax]);
        }
        int ptr = 0;
        int sum = 0;
        for(int j = 0; j < 3; ++ j) {
            if (argmax == j) continue;
            sum += a[alive[j]];
            for(int i = 0; i < a[alive[j]]; ++ i) {
                ans.insert(ans.begin() + ptr, alive[j]);
                ptr = (ptr + 2) % ans.size();
            }
        }
        if (sum < a[alive[argmax]]) {
            puts("IMPOSSIBLE");
            return;
        }
    }
    for(int i = 1; i < 6; i += 2) {
        int goal = p[i];
        for(int j = 0; j < ans.size(); ++ j) {
            if (ans[j] == goal) {
                for(int k = 0; k < a[i]; ++ k) {
                    ans.insert(ans.begin() + j, i);
                    ans.insert(ans.begin() + j, p[i]);
                }
                break;
            }
        }
    }
    for(int i = 0; i < ans.size(); ++ i) {
        putchar(color[ans[i]]);
    }
    puts("");
    for(int i = 0; i < ans.size(); ++ i) {
        assert(ans[i] != ans[(i + 1) % ans.size()]);
    }
}

int main()
{
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	//freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
	//freopen("B-small-attempt2.in", "r", stdin); freopen("B-small-attempt2.out", "w", stdout);
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	int test_case;
	cin >> test_case;
	for(int i = 0; i < test_case; ++ i) {
	    cerr << "Start: " << i << endl;
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
