#include <bits/stdc++.h>

#define st first
#define nd second
#define pb push_back
#define mp make_pair

#define cl(x,y) memset(x, y, sizeof(x))
#define dbs(x) cerr << x << endl;
#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int INF = 0x3f3f3f3f, MOD = 1e9+7;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const double PI=acos(-1), EPS = 1e-9;
const int N = 1e3+9;

struct Bit {
    static const int N = 1e3+9;
    int b[N] = {};
    int sum(int p) {
        int s = 0;
        for(p+=2;p;p-=p&-p)
            s += b[p];
        return s;
    }
    void upd(int p, int v) {
        for(p+=2; p<N; p+=p&-p)
            b[p]+=v;
    }
};

int main () {
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++) {
        Bit b;
        char s[N];
        int k;
        scanf("%s %d", s, &k);
        int n = strlen(s);
        int ans = 0;
        for(int i = 0; i+k-1 < n; i++) {
            if((s[i]=='-' and b.sum(i)%2 == 0) or (s[i]=='+' and b.sum(i)%2)) {
                ans++;
                b.upd(i,1);
                b.upd(i+k,-1);
            }
        }
        bool ok = true;
        for(int i = 0; i < n; i++)
            if((s[i]=='-' and b.sum(i)%2 == 0) or (s[i]=='+' and b.sum(i)%2)) {
                ok = false;
            }
        if(ok)
            printf("Case #%d: %d\n", t, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", t);
    }

    return 0;
}
