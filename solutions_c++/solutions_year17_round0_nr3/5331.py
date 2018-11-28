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

unsigned long long limit, res;

struct cmp {
    bool operator() (const PII a, const PII b) const {
        if (min(a.FS, a.SC) != min(b.FS, b.SC)) {
            return min(a.FS, a.SC) > min(b.FS, b.SC);
        }
        return max(a.FS, a.SC) > max(b.FS, b.SC);
    }
};


int main() {
    #ifndef ONLINE_JUDGE
        freopen("C-small1.in", "rt", stdin);
        freopen("outputC1.txt", "wt", stdout);
    #endif

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int cas = 0; cas < T; cas++) {
        int n, k, cnt = 0, res = -1;
        int aux;
        cin >> n >> k;
//        map<int, int> freq;
        priority_queue<int> pq;
        pq.push(n);

        while (!pq.empty()) {
            aux = pq.top(); pq.pop();
            if (aux == 0)
                continue;
//            freq[aux] ++;
            cnt ++;
            if (cnt == k) {
                res = aux;
                break;
            }

            if ((aux % 2) != 0){
                pq.push(aux / 2);
                pq.push(aux / 2);
            } else {
                pq.push(aux / 2 - 1);
                pq.push(aux / 2);
            }
        }

//        cout << "\\\\\\ \n";
//        for (auto& xVal : freq) {
//            cout << xVal.first << ", " << xVal.second << "\n";
//        }
//        cout << "\\\\\\ \n";

        cout << "Case #" << cas + 1 << ": ";
        if ((res % 2) == 0) {
            cout << res / 2 << " " << res / 2 - 1 << "\n";
        } else {
            cout << res / 2 << " " << res / 2 << "\n";
        }

    }

return 0;
}
