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

const string BAD = "IMPOSSIBLE";

string solve() {
  int n = ri();
  vi C(6);
  rep(i, 6) {
    C[i] = ri();
  }

  vvi G(6);
  G[0] = {2, 4};
  G[1] = {4};
  G[2] = {4, 0};
  G[3] = {0};
  G[4] = {0, 2};
  G[5] = {2};

  rep(i, 6) if (C[i]) {
    vi ans;
    vi A(C);
    int cur = i;

    bool ok = 1;

    int nex;

    while (1) {
      A[cur]--;
      //out(cur, A);
      ans.emplace_back(cur);
      int s = accumulate(all(A), 0);
      if (s == 0) break;

      if (cur % 2 == 0) {
        int tar = (cur + 3) % 6;
        if (A[tar]) {
          cur = tar;
          continue;
        }
        nex = (A[G[cur][0]] > A[G[cur][1]]) ? G[cur][0] : G[cur][1];
      }
      else {
        nex = G[cur][0];
      }

      if (A[nex] == 0) {
        ok = 0;
        break;
      }
      cur = nex;
      continue;
    }

    if (ok) {
      //out(ans);
      if (ans[0] == ans.back()) {
        swap(ans[n-1], ans[n-2]);
        if (ans[n-3] == ans[n-2]) return BAD;
      }
      string sol;
      string conv = "ROYGBV";
      forr(a, ans) {
        sol += conv[a];
      }
      return sol;
    }
  }


  return BAD;
}

void Main() {
  cout << solve() << endl;
}

int main() {
  cin.tie(nullptr);
  ios::sync_with_stdio(false);
  int T;cin>>T;
  for (int i = 0; i < T; i++) {
    //printf("Case #%d: ", i + 1);
    cout << "Case #" << (i + 1) << ": ";
    Main();
  }
  return 0;
}
