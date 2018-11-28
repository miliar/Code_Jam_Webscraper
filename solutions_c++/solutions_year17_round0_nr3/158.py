#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <functional>
#include <map>
#include <bitset>

#define INF 0x7fffffff
#define REP(i,j,k) for(int i = j;i <= k;i++)
#define squr(x) (x) * (x)
#define lowbit(x) (x&(-x))
#define getint(x) scanf("%d", &(x))

typedef long long LL;

using namespace std;

LL n, k;
int T;
map<LL, LL> t;

void add (LL num, LL time) {
    if (t.count(num) == 0) {
        t.insert(pair<LL, LL>(num, time));
    } else {
        auto it = t.find(num);
        it -> second += time;
    }
}

int main(int argc, const char * argv[]) {
    //freopen("C-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    cin >> T;
    REP(ca, 1, T) {
        cin >> n >> k;
        LL ansmax = 0, ansmin = 0;
        t.clear();
        t.insert(pair<LL, LL> (n, 1));
        while (k > 0) {
            auto it = t.end(); it--;
            LL temp = it -> first;
            if (k > it -> second) {
                if (temp % 2 == 1) {
                    add(temp / 2, 2 * it->second);
                } else {
                    add(temp / 2, it->second);
                    add(temp / 2 - 1, it->second);
                }
                k -= it->second;
            } else {
                if (temp % 2 == 1) {
                    ansmax = ansmin = temp / 2;
                } else {
                    ansmax = temp / 2;
                    ansmin = temp / 2 - 1;
                }
                k = 0;
            }
            t.erase(it);
        }
        printf("Case #%d: %lld %lld\n", ca, ansmax, ansmin);
    }
    return 0;
}









