#include <bits/stdc++.h>
using namespace std;

#define _p(...) (void)printf(__VA_ARGS__)
#define forr(x,arr) for(auto&& x:arr)
#define _overload3(_1,_2,_3,name,...) name
#define _rep2(i,n) _rep3(i,0,n)
#define _rep3(i,a,b) for(int i=int(a);i<int(b);++i)
#define rep(...) _overload3(__VA_ARGS__,_rep3,_rep2,)(__VA_ARGS__)
#define _rrep2(i,n) _rrep3(i,0,n)
#define _rrep3(i,a,b) for(int i=int(b)-1;i>=int(a);i--)
#define rrep(...) _overload3(__VA_ARGS__,_rrep3,_rrep2,)(__VA_ARGS__)
#define all(x) (x).begin(),(x).end()
#define bit(n) (1LL<<(n))
#define sz(x) ((int)(x).size())
#define ten(n) ((int)1e##n)
#define fst first
#define snd second
using ll=long long;
using pii=pair<int,int>;using pll=pair<ll,ll>;using pil=pair<int,ll>;using pli=pair<ll,int>;
using vs=vector<string>;using vvs=vector<vs>;using vvvs=vector<vvs>;
using vb=vector<bool>;using vvb=vector<vb>;using vvvb=vector<vvb>;
using vi=vector<int>;using vvi=vector<vi>;using vvvi=vector<vvi>;
using vl=vector<ll>;using vvl=vector<vl>;using vvvl=vector<vvl>;
using vd=vector<double>;using vvd=vector<vd>;using vvvd=vector<vvd>;
using vpii=vector<pii>;using vvpii=vector<vpii>;using vvvpii=vector<vvpii>;
template<class T> bool amax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> bool amin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
ll ri(){ll l;cin>>l;return l;} string rs(){string s;cin>>s;return s;}
template<class T>T read(){T t;cin>>t;return t;}
template<class T,class U>ostream&operator<<(ostream&o,const pair<T,U>&p){return o<<'('<<p.fst<<", "<<p.snd<<')';}
ostream&operator<<(ostream&o,const vb&t){forr(e,t)o<<"#."[e];return o;}
template<class T>ostream&operator<<(ostream&o,const vector<T>&t){o<<"{";forr(e,t)o<<e<<",";o<<"}"<<endl;return o;}
#ifdef LOCAL
vs s_p_l_i_t(const string&s,char c){vs v;stringstream ss(s);string x;while(getline(ss,x,c))v.emplace_back(x);return move(v);}
void e_r_r(vs::iterator it){cerr<<endl;}
template<class T,class... Args>void e_r_r(vs::iterator it,T a,Args... args){cerr<<it->substr((*it)[0]==' ',it->length())<<" = "<<a<<", ";e_r_r(++it,args...);}
#define out(args...){vs a_r_g_s=s_p_l_i_t(#args,',');e_r_r(a_r_g_s.begin(),args);}
#else
#define out(args...)
#endif

void Main() {
  int n = ri();
  int k = ri();

  vector<pair<int, double>> P(n);
  const double pi = 3.14159265358979323846;

  rep(i, n) {
    ll r = ri();
    double h = ri();
    P[i].fst = r;
    P[i].snd = r * 2 * pi * h;
  }

  sort(all(P));

  double ans = 0;

  rep(i, n) {
    if (i+1 < k) continue;
    ll r = P[i].fst;
    double a = P[i].snd;

    vd A;
    rep(j, i) {
      A.emplace_back(P[j].snd);
    }
    sort(all(A), greater<decltype(A)::value_type>());
    //out(r, a);
    //out(A);
    //out(i, r, A);

    double sum_a = 0;
    rep(j, k-1) {
      sum_a += A[j];
    }
    //out(a, sum_a);
    double m = r * r * pi;
    double cand = m + a + sum_a;
    amax(ans, cand);
  }

  cout << ans << endl;
}

int main() {
  cin.tie(nullptr);
  ios::sync_with_stdio(false);
  cout << fixed << setprecision(10);
  int T;cin>>T;
  for (int i = 0; i < T; i++) {
    //printf("Case #%d: ", i + 1);
    cout << "Case #" << (i + 1) << ": ";
    Main();
  }
  return 0;
}
