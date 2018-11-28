#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <list>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iomanip>
#include <iterator> 
#include <limits>

#define REP(i,n) for (int i=0;i<(n);i++)
#define FOR(i,a,b) for (int i=(a); i<(b); i++)
#define ALL(a) (a).begin(),(a).end()
#define RALL(A) (a).rbegin(),(a).rend()
#define PB push_back
#define MP make_pair

#define dump(x) cerr << #x << " = " << (x) << endl;

using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = numeric_limits<int>::max() / 2;
const int NEG_INF = numeric_limits<int>::min() / 2;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;

int T;

PII solve(int N, int K) {
    priority_queue<PII> pq;
    int a = N / 2;
    int b = N - 1 - a;
    pq.push(PII(a, b));
    vector<PII> res;
    int n = 0;
    while (!pq.empty()) {
        PII top = pq.top(); pq.pop();
        a = top.first;
        b = top.second;
        //cout << a << " " << b << endl;
        res.PB(PII(a, b));
        n += 1;
        if (n >= K) {
            return res[K - 1];
        }
        if (a != 0) {
            int naa = a / 2;
            int nab = a - 1 - naa;
            pq.push(PII(naa, nab));
        }
        if (b != 0) {
            int nba = b / 2;
            int nbb = b - 1 - nba;
            pq.push(PII(nba, nbb));
        }
    }
    return res[K - 1];
}

int main(int argc, char const* argv[])
{
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, K; cin >> N >> K;
        PII ans = solve(N, K);
        cout << "Case #" << i + 1 << ": " << max(ans.first, ans.second) << " " << min(ans.first, ans.second) << endl;
    }
    return 0;
}

