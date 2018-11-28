#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, k, n) for (int i = (int)(k); i < (int)(n); i++)
#define forba(i, n, k) for (int i = (int)(n) - 1; i >= (int)(k); i--)

#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define db(x) cout << #x << " = " << x << endl

using namespace std;
            
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;
typedef double ld; 

const ld pi = acos(-1.0);
const ld eps = 1e-9;
const int INF = (int)1e9;
const int MAXN = 1111;

string S = "RYB";
string JS = "GVO";

set<pair<char, char>> isOk;

int T, N, n;
int cnt[3], jcnt[3];
int id[3], pos, res[MAXN];
char ans[MAXN];

bool cmp(int i, int j) {
    return cnt[i] > cnt[j];    
}

int main() {

    forn(i, 3) {
        forn(j, 3) {
            if (i != j) {
                isOk.insert(mp(S[i], S[j]));
                isOk.insert(mp(JS[i], S[i]));
                isOk.insert(mp(S[i], JS[i]));   
            }
        }
    }
    
    cin >> T;
    forn(ttt, T) {
        printf("Case #%d: ", ttt + 1);

        scanf("%d", &n);
        scanf("%d", &cnt[0]);
        scanf("%d", &jcnt[2]);
        scanf("%d", &cnt[1]);
        scanf("%d", &jcnt[0]);
        scanf("%d", &cnt[2]);
        scanf("%d", &jcnt[1]);
        
        n = 0;
        forn(i, 3) {
            n += cnt[i];
            n += jcnt[i];   
        }
        N = n;
        
        bool fail = 0;
        
        bool lol = 0;
        //mega sluchai
        for (int i = 0; i < 3; i++) {
            if (n == cnt[i] + jcnt[i] && cnt[i] == jcnt[i]) {
                forn(j, cnt[i]) {
                    cout << JS[i] << S[i];    
                }
                cout << '\n';
                lol = 1;                
            } else if (jcnt[i] >= n / 2) {
                fail = 1;   
            }                        
        }
        
        if (lol) {
            continue;    
        }         
        
        if (fail) {
            cout << "IMPOSSIBLE\n";
            continue;    
        }
        
        //fold jcnt
        forn(i, 3) {
            if (jcnt[i] > 0) {
                if (cnt[i] < jcnt[i] + 1) {
                    fail = 1;
                } else {
                    n -= jcnt[i] * 2;
                    cnt[i] -= jcnt[i];   
                }
            }
        }
        
        if (fail) {
            cout << "IMPOSSIBLE\n";
            continue;    
        }
        
        int tmp = 0;
        forn(i, 3) {
            tmp += cnt[i];    
        }
        
        assert(tmp == n);
        
        forn(i, 3) {
            id[i] = i;
        }
        
        sort(id, id + 3, cmp);
        
        memset(res, -1, sizeof(res));
        
        pos = 0;
        forn(it, 3) {
            int i = id[it];            
            forn(it2, cnt[i]) {
                res[pos] = i;
                pos += 2;
                if (pos >= n) {
                    pos = 1;   
                }
            }
        }
        
        forn(i, n) {
            assert(res[i] != -1);
            cnt[res[i]]--;   
        }
        
        forn(i, 3) {
            assert(cnt[i] == 0);
        }
        
        forn(i, n) {
            if (res[i] == res[(i + 1) % n]) {
                fail = 1;
            }
        }
        
        if (fail) {
            cout << "IMPOSSIBLE\n";
            continue;    
        }
        
        //unfold
        int ptr = 0;
        for (int i = 0; i < n; i++) {
            int cur = res[i];
            if (jcnt[cur] > 0) {
                forn(j, jcnt[cur]) {
                    ans[ptr++] = S[cur];
                    ans[ptr++] = JS[cur];
                }
                jcnt[cur] = 0;
            }
            ans[ptr++] = S[cur];           
        }
        
        assert(ptr == N);
        
        forn(i, N) {
            assert(isOk.find(mp(ans[i], ans[(i + 1) % N])) != isOk.end());    
        }
        
        forn(i, N) {
            printf("%c", ans[i]);
        }
        cout << '\n';
    }
    
    return 0;
}