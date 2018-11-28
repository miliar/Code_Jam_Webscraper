#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define fi first
#define se second

using namespace std;

typedef unsigned long long int64;
typedef pair<int, int> ii;

const double EPS = 1e-9;
const int INF = 0x3f3f3f3f;

int sgn(double a) { return ((a > EPS) ? (1) : ((a < -EPS) ? (-1) : (0))); }
int cmp(double a, double b = 0.0) { return sgn(a - b); }

struct node{
    string s;
    int f, p;
    node(string s = "", int f = 0, int p = 0) : s(s), f(f), p(p) {}
};

int walk(int st, const string& s){
    while (st < s.size() && s[st] == '+') st++;
    return st;
}

int main(){
    ios::sync_with_stdio(false);
    int t;
    int64 n;
    cin >> t;
    for (int cs = 1; cs <= t; cs++){
        cout << "Case #" << cs << ": ";
        cin >> n;
        queue<int64> bfs;
        for (int64 i = 1; i <= 9; i++) bfs.push(i);

        int64 ans = 0LL;
        while (!bfs.empty()){
            int64 at = bfs.front(); bfs.pop();
            int64 last = at % 10LL;
            if (at > n) continue;
            ans = max(ans, at);
            for (int64 i = 1; i <= 9; i++){
                if (last <= i) bfs.push(at*10LL + i);
            }
        }
        cout << ans << endl;
    }
    return 0;
}