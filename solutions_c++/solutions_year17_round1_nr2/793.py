#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <limits>
#include <iostream>
#include <utility>

using namespace std;

#define TRACE(x...) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define PRINT(x...) TRACE(printf(x); fflush(stdout))

#define gc getchar  //unlocked linux
#define all(v) (v).begin(), (v).end()
#define FU(i, a, b) for(decltype(b) i = (a); i < (b); ++i)
#define fu(i, n) FU(i, 0, n)
#define FD(i, a, b) for (decltype(b) i = (b)-1; i >= a; --i)
#define fd(i, n) FD(i, 0, n)
#define mod(a, b) ((((a)%(b))+(b))%(b))
#define pb push_back
#define sz(c) int((c).size())
#define mk make_pair

const int INF = 0x3F3F3F3F; const int NEGINF = 0xC0C0C0C0;

const double EPS = 1e-8;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;

int cmp_double(double a, double b, double eps = 1e-9){
  return a + eps > b ? b + eps > a ? 0 : 1 : -1;  //0 = iguais, 1 = a maior
}

inline void scanint(int &x){
  register int c = gc();
  x = 0;
  int neg = 0;
  for(;((c<48 || c>57) && c != '-');c = gc());
  if(c=='-') {neg=1;c=gc();}
  for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
  if(neg) x=-x;
}

bool canDo(ll qtd, ll pack, ll grams) {
  double A = (double)grams * (double)(qtd) * 0.9;
  double B = (double)grams * (double)(qtd) * 1.1;
  if (cmp_double(A, (double)pack) <= 0 && cmp_double(B, (double)pack) >= 0) {
    return true;
  }
  return false;
}

pair<int,int> computeRange(int pack, int grams) {
  int qtd = pack/grams;
  double maxGrams = pack/0.9;
  double minGrams = pack/1.1;
  int qtdMax = maxGrams/(double)grams;
  int qtdMin = minGrams/(double)grams;
  if (qtdMin == 0) qtdMin++;
  if (qtdMax == 0) qtdMax++;

  int minL = -1;
  int maxR = -1;
  if (canDo(qtdMin, pack, grams)) {
    minL = qtdMin;
  } else if (canDo(qtdMin+1, pack, grams)) {
    minL = qtdMin+1;
  }
  if (canDo(qtdMax, pack, grams)) {
    maxR = qtdMax;
  } else if (canDo(qtdMax-1, pack, grams)) {
    maxR = qtdMax-1;
  }
  if (minL == 0) minL = -1;
  if (maxR == 0) maxR = -1;
  return {minL, maxR};
}

int main(){
  int T;
  int cases = 1;
  cin >> T;
  while(T--){
    int N, P;
    cin >> N >> P;
    vector<int> grams(N);
    for (int i = 0; i < N; i++) {
      scanf(" %d", &grams[i]);
    }

    vector<vector<int>> packages(N, vector<int>(P));
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < P; j++) {
        scanf(" %d", &packages[i][j]);
      }
    }


    vector<pair<int, pair<bool, int>>> events;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < P; j++) {
        int pack = packages[i][j];
        pair<int,int> p = computeRange(pack, grams[i]);
       // printf("%d %d = %d %d\n", i, j, p.first, p.second);
        if (p.first == -1 || p.second == -1) continue;
        events.pb( {p.first, {false, i}} );
        events.pb( {p.second, {true, i}} );
       // printf("ID %d\n", i);
      }
    }
    sort(events.begin(), events.end());

    vector<int> seen(N, 0);
    vector<int> toremove(N, 0);
    ll ans = 0;

    for (int i = 0; i < events.size(); i++){
      bool isOpen = !events[i].second.first;
      int id = events[i].second.second;
      //printf("%d %d %d\n", isOpen , id, events[i].first);
      if (isOpen == true) {
        seen[id]++;

        bool ok = true;
        for (int j = 0; j < N; j++) {
          if (seen[j] == 0) {
            ok = false; break;
          }
        }
        if (ok) {
          ans++;
          for (int j = 0; j < N; j++) {
            toremove[j]++;
            seen[j]--;
          }
        }

      } else {
        if (toremove[id] > 0) {
          toremove[id]--;
        } else {
          seen[id]--;
        }
      }
    }

    printf("Case #%d: %lld\n", cases++, ans);
  }

  return 0;
}
