#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define fi first
#define se second

using namespace std;

typedef long long int64;
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

string flip(string& pancake, int x, int y){
    bool ops = true;
    string tmp = pancake;
    for (int i = x; i < y; i++){
        if (pancake[i] == '-'){
            pancake[i] = '+';
            ops = false;
        }
        else pancake[i] = '-';
    }
    if (ops) return tmp;
    else return pancake;
}

int walk(int st, const string& s){
    while (st < s.size() && s[st] == '+') st++;
    return st;
}

int main(){
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int cs = 1; cs <= t; cs++){
        cout << "Case #" << cs << ": ";
        string s;
        int k;
        cin >> s >> k;

        queue<node> bfs;
        set<string> visited;
        int st = walk(0, s);
        if (st == s.size()){
            cout << "0\n";
            continue;
        }

        bool ans = false;
        visited.insert(s);
        bfs.push(node(s, 0, st));

        while (!ans && !bfs.empty()){
            node at = bfs.front(); bfs.pop();

            for (; at.p+k <= at.s.size(); at.p++){
                string tmp = at.s;
                string pck = flip(tmp, at.p, at.p+k);
                if (visited.count(pck)) continue;

                int w = walk(0, pck);
                if (w == pck.size()){
                    cout << at.f+1 << "\n";
                    ans = true;
                    break;
                }
                visited.insert(pck);
                bfs.push(node(pck, at.f+1, w));
            }
            if (ans) break;
        }
        cout << ((!ans) ? "IMPOSSIBLE\n" : "");
    }
    return 0;
}