#include<bits/stdc++.h>
#define INF 0x7fffffff
#define INFLL 1e17
#define PI 2*acos(0.0)
#define show(x) cout<< #x <<" is "<< x <<"\n"
using namespace std;

#define FS first
#define SC second
#define PB(t) push_back(t)
#define ALL(t) t.begin(),t.end()
#define MP(x, y) make_pair((x), (y))
#define Fill(a,c) memset(&a, c, sizeof(a))

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<PII> VPII;

int main() {
    #ifndef ONLINE_JUDGE
        freopen("A-large.in", "rt", stdin);
        freopen("outputA.txt", "wt", stdout);
    #endif

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int cas = 0; cas < T; cas++) {
        string line;
        int k, res = 1, cnt = 0;
        cin >> line >> k;

        for (int i = 0; i <= line.size() - k; i++) {
            if (line[i] == '-') {
                cnt ++;
                for (int j = 0; j < k; j++) {
                    if (line[i + j] == '+') {
                        line[i + j] = '-';
                    } else {
                        line[i + j] = '+';
                    }
                }
            }
        }

        for (int i = 0; i < line.size(); i++) {
            if (line[i] == '-') {
                res = 0;
                break;
            }
        }


        cout << "Case #" << cas + 1 << ": ";
        if (res) {
            cout << cnt << "\n";
        } else {
            cout << "IMPOSSIBLE\n";
        }

    }

return 0;
}
