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
    lli n = get<int>();
    lli c = get<int>();
    map<lli, lli> M;
    M[n] = 1;
    while(c){
        lli nxt = (--M.end()) -> first;
        lli num = (--M.end()) -> second;
        DBG cout << "[" << nxt << " | " << num << endl;
        M.erase(--M.end());
        if(num >= c){
            cout << (nxt) / 2 << " " << (nxt - 1) / 2 << endl;
            return;
        }
        c -= num;
        if(M.find(nxt / 2) == M.end()) M[nxt / 2] = 0;
        if(M.find((nxt - 1) / 2) == M.end()) M[(nxt - 1) / 2] = 0;
        M[nxt / 2] += num;
        M[(nxt - 1) / 2] += num;
    }
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
