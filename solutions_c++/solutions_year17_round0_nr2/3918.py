#include<bits/stdc++.h>

using namespace std;

#define FOR(i,n)	for(int i=0;i<(int)n;i++)
#define FOB(i,n)	for(int i=n;i>=1;i--)
#define MP(x,y)	make_pair((x),(y))
#define ii pair<int, int>
#define lli long long int
#define ulli unsigned long long int
#define lili pair<lli, lli>
#ifdef EBUG
#define DBG	if(1)
#else
#define DBG	if(0)
#endif
#define SIZE(x) int(x.size())
const int infinity = 2000000999 / 2;
const long long int inff = 4000000000000000999;

typedef complex<long double> point;

template<class T>
T get() {
    T a;
    cin >> a;
    return a;
}

template <class T, class U>
ostream& operator<<(ostream& out, const pair<T, U> &par) {
    out << "[" << par.first << ";" << par.second << "]";
    return out;
}

template <class T>
ostream& operator<<(ostream& out, const set<T> &cont){
    out << "{";
    for (const auto &x:cont) out << x << ", ";
    out << "}";
    return out;
}

template <class T, class U>
ostream& operator<<(ostream& out, const map<T,U> &cont){
    out << "{";
    for (const auto &x:cont) out << x << ", ";
    out << "}"; return out;
}

template <class T>
ostream& operator<<(ostream& out, const vector<T>& v) {
  FOR(i, v.size()){
    if(i) out << " ";
    out << v[i];
  }
  out << endl;
  return out;
}

bool ccw(point p, point a, point b){
  if((conj(a - p) * (b - p)).imag() <= 0) return(0);
  else return(1);
}

void solve(){
    lli n = get<lli>();
    vector<vector<lli> > was_less(19, vector<lli>(10, 0)), wasnt(19, vector<lli>(10, -1));
    
    string sn = to_string(n);
    while(sn.size() < 20) sn = "0" + sn;
    DBG cout << "Sn = |" << sn << "|" << endl;
    
    FOR(i, 10){
        was_less[0][i] = 9;
        if((sn.back() - '0') >= i) wasnt[0][i] = max(sn.back() - '0', i);
    }
    
    lli a = 0;
    lli nasb = 1;
    
    for(int i = 1; i < 19; i ++){
        nasb *= 10;
        FOR(j, 10){
            for(int l = j; l < 10; l ++){
                was_less[i][j] = max(l * nasb + max(wasnt[i - 1][l], was_less[i - 1][l]), was_less[i][j]);
                if(l < (sn[19 - i] - '0')){
                    DBG cout << l << " ok on " << i << "th place " << endl;
                    wasnt[i][j] = max(wasnt[i][j], l * nasb + max(wasnt[i - 1][l], was_less[i - 1][l]));
                }
                if(l == (sn[19 - i] - '0') && wasnt[i - 1][l] != -1) wasnt[i][j] = max(l * nasb + wasnt[i - 1][l], wasnt[i][j]);
            }
        }
    }
    
    DBG cout << "L" << was_less << "N" << wasnt;
    
    FOR(i, 10) a = max(wasnt[18][i], a);
    cout << a << endl;
    
}

int main(){
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    int t = get<int>();
    FOR(i, t){
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    
}
