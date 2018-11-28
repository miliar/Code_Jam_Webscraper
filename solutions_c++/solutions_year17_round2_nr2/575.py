//touch {a..m}.in; tee {a..m}.cpp < template.cpp
#include <bits/stdc++.h>
using namespace std;
#define forr(i,a,b) for(int i=(a); i<(b); i++)
#define forn(i,n) forr(i,0,n)
#define sz(c) ((int)c.size())
#define zero(v) memset(v, 0, sizeof(v))
#define forall(it,v) for(auto it=v.begin();it!=v.end();++it)
#define pb push_back
#define RND(a, b) (rand()%((b)-(a)+1)+(a))
#define fst first
#define snd second
typedef long long ll;
typedef pair<int,int> ii;
#define dforn(i,n) for(int i=n-1; i>=0; i--)
#define dprint(v) cout << #v"=" << v << endl //;)

const int MAXN=100100;
int n;
int R, O, Y, G, B, V;
#define LET(i) l[(i)].snd

void solvesmall(){
    cin >> n >> R >> O >> Y >> G >> B >> V;
    vector<pair<int, char> > l;
    l.pb(make_pair(R, 'R'));
    l.pb(make_pair(Y, 'Y'));
    l.pb(make_pair(B, 'B'));
    sort(l.begin(), l.end(), greater<pair<int, char> >());
    string s;
    while(l[1].fst!=l[2].fst){
        if(!l[0].fst){
            assert(false);
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        s+=LET(0);
        s+=LET(1);
        l[0].fst--, l[1].fst--;
    }
    //~ cout << l[0].fst <<  ' ' << l[1].fst <<  ' ' << l[2].fst << endl;
    while(l[0].fst!=l[1].fst){
        if(!l[1].fst){
            //~ assert(false);
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        if(l[0].fst<2) assert(false);
        s+= LET(0), s+= LET(1), s+= LET(0), s+= LET(2);
        l[0].fst-=2;
        l[1].fst--;
        l[2].fst--;
    }
    while(l[0].fst){
        s+=LET(0), s+=LET(1), s+= LET(2);
        l[0].fst--, l[1].fst--, l[2].fst--;
    }
    cout << s  << endl;
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("b.out", "w", stdout);
    ios::sync_with_stdio(0);
    int TC; cin >> TC;
    forr(TCC, 1, TC+1){
        cout << "Case #" << TCC << ": ";
        solvesmall();
    }
    return 0;
}
