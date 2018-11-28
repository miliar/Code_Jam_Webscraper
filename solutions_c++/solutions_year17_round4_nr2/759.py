#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define all(c) (c).begin(), (c).end()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define eb emplace_back
#define mp make_pair

typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int N = 1010;
int n,c,m,cl[N],pos[N];

void init() {
    memset(cl,0,sizeof cl);
    memset(pos,0,sizeof pos);
}

int techo(int a, int b) { return (a+b-1)/b; }

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    int T; cin >> T;
    forn(cas,T) {
        cout << "Case #" << cas+1 << ": ";
        init();

        cin >> n >> c >> m;

        int mcl = 0;
        forn(_,m) {
            int p,b; cin >> p >> b;
            p--; b--;
            mcl = max(mcl, ++cl[b]);
            pos[p]++;
        }

        int sum = 0, k = 0;
        forn(i,n) {
            sum += pos[i];
            k = max(k, techo(sum, i+1));
        }

        k = max(mcl,k);

        int prom = 0;
        forn(i,n) prom = max(prom, pos[i] - k);

        cout << k << ' ' << prom << endl;
    }

    return 0;
}
