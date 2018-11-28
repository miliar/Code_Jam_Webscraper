#include <bits/stdc++.h>

#define PI 3.14159265358979323846
#define EPS 1e-6
#define INF 1000000000

#define _ ios_base::sync_with_stdio(0), cin.tie(0), cin.tie(0), cout.tie(0), cout.precision(15);
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define RFOR(i, a, b) for(int i=int(a)-1; i>=int(b); i--)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define RFORC(cont, it) for(decltype((cont).rbegin()) it = (cont).rbegin(); it != (cont).rend(); it++)
#define pb push_back
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;

#define MAXN 10
#define MOD 1000000007

bool b;
string s;
int cant[MAXN];
vi mat[MAXN];
int n;

void llena() {
    mat[0].pb(3);
    mat[0].pb(2);
    mat[0].pb(4);

    mat[1].pb(4);

    mat[2].pb(5);
    mat[2].pb(0);
    mat[2].pb(4);


    mat[3].pb(0);

    mat[4].pb(1);
    mat[4].pb(0);
    mat[4].pb(2);

    mat[5].pb(2);
}


int next(int act, int first) {
    if (cant[mat[act][0]] > 0) {
        cant[mat[act][0]] --;
        return mat[act][0];
    }

    if (act % 2)    return -1;

    if (cant[mat[act][1]] == 0 && cant[mat[act][2]] == 0)
        return -1;

    if (cant[mat[act][1]] > cant[mat[act][2]]) {
        cant[mat[act][1]] --;
        return mat[act][1];
    }
    else if (first != -1 && cant[mat[act][1]] == cant[mat[act][2]]) {
        if (first == mat[act][1]) {
            cant[mat[act][1]] --;
            return mat[act][1];
        }
        if (first == mat[act][2]) {
            cant[mat[act][2]] --;
            return mat[act][2];
        }
    }

    cant[mat[act][2]] --;
    return mat[act][2];
}

int selectFirst() {
    if (cant[0] >= cant[2] && cant[0] >= cant[4]) return 0;
    if (cant[2] >= cant[0] && cant[2] >= cant[4]) return 2;
    return 4;
}

string roy = "ROYGBV";
bool solve() {
    int act = selectFirst();
    int first = act;
    s = roy[first];
    cant[first] --;
    while(true) {
        act = next(act, first);
        if (act == -1)   break;

        s = s + roy[act];
    }
    return s.length() == n;
}

int main() { _
    int T;

    /**/
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    /**/
    llena();
    cin >> T;
    FOR (t, 1, T + 1) {
        cin >> n;
        FOR(i, 0, 6) {
            cin >> cant[i];
        }

        bool b = !solve();
        b = b || s[0] == s[s.length() - 1];
        if (b)  cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        else    cout << "Case #" << t << ": " << s << endl;
    }

    return 0;
}

