#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <random>
#include <functional>

using namespace std;

#define F first
#define S second
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 
#define db3(x, y, z) cerr << "(" << #x << ", " << #y << ", " << #z << ") = (" << x << ", " << y << ", " << z << ")\n"
#define dbv(a) cerr << #a << ": "; for (auto& xxxx: a) cerr << xxxx << " "; cerr << endl;
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)a.size()
#define pw(n) (1ll << (n))
#define equal equalll
#define less lesss


typedef long double dbl;
typedef long long ll;
const int N = -1;
const ll INF = 1.01e9;
typedef vector<int> vi;

int p;

map<pair<vector<int>,int>, int> answer;

int rec(vector<int> cnt, int curRem) {
    if (answer.count({cnt, curRem}) == 0) {
        int res = 0;
        for (int i = 0; i < p; i++) {
            if (cnt[i] > 0) {
                cnt[i]--;
                res = max(res, rec(cnt, (curRem + i) % p) + (curRem == 0));
                cnt[i]++;
            }
        }
        answer[make_pair(cnt, curRem)] = res;
    }
    return answer[make_pair(cnt, curRem)];
}

int main(){
#ifdef HOME 
    assert(freopen("A.in", "r", stdin));
    freopen("A.out", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for (int tt = 0; tt < T; tt++) {
        printf("Case #%d: ", tt + 1);
        int n;
        answer.clear();
        scanf("%d%d", &n, &p);
        vector<int> rem(p);
        for (int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            rem[x % p]++;
        }
        int cnt0 = rem[0];
        rem[0] = 0;
        printf("%d\n", cnt0 + rec(rem, 0));
    }
      
    
    
#ifdef HOME 
    epr("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
#endif
    return 0;
}

