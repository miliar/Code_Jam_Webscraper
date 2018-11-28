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

int main(){
  int T;
  int cases = 1;
  cin >> T;
  while(T--){
    int N; cin >> N;
    //R, O, Y, G, B, and V.
    int R, O, Y, G, B, V;
    cin >> R >> O >> Y >> G >> B >> V;

    if (R != 0 && O == 0 && Y == 0 && G != 0 && B == 0 && V == 0){
        if (R == G) {
            printf("Case #%d: ", cases++);
            for (int i = 0; i < R; i++){
              printf("RG");
            }
            printf("\n");
            continue;
        }
        printf("Case #%d: IMPOSSIBLE\n", cases++);
        continue;
    }
    if (R == 0 && O != 0 && Y == 0 && G == 0 && B != 0 && V == 0){
      if (O == B) {
            printf("Case #%d: ", cases++);
            for (int i = 0; i < O; i++){
              printf("OB");
            }
            printf("\n");
            continue;
        }
        printf("Case #%d: IMPOSSIBLE\n", cases++);
        continue;
    }
    if (R == 0 && O == 0 && Y != 0 && G == 0 && B == 0 && V != 0){
      if (Y == V) {
            printf("Case #%d: ", cases++);
            for (int i = 0; i < Y; i++){
              printf("YV");
            }
            printf("\n");
            continue;
        }
        printf("Case #%d: IMPOSSIBLE\n", cases++);
        continue;
    }


    int Omin = O+1;
    int Omax = 2*O;

    int Gmin = G+1;
    int Gmax = 2*G;

    int Vmin = V+1;
    int Vmax = 2*V;

    if (B < Omin && O > 0) {
      printf("Case #%d: IMPOSSIBLE\n", cases++);
      continue;
    }
    if (R < Gmin && G > 0) {
      printf("Case #%d: IMPOSSIBLE\n", cases++);
      continue;
    }
    if (Y < Vmin && V > 0) {
      printf("Case #%d: IMPOSSIBLE\n", cases++);
      continue;
    }
    B -= O;
    R -= G;
    Y -= V;

    vector<pair<int,int>> vet;
    vet.pb({B, 0});
    vet.pb({R, 1});
    vet.pb({Y, 2});
    sort(vet.rbegin(), vet.rend());
    if (vet[0].first > vet[1].first + vet[2].first) {
      printf("Case #%d: IMPOSSIBLE\n", cases++);
      continue;
    }
    map<int, char> auxm;
    auxm[0] = 'B';
    auxm[1] = 'R';
    auxm[2] = 'Y';

    map<int, char> m;
    for (int i = 0; i < 3; i++){
      m[i] = auxm[vet[i].second];
    }

    int qtd = vet[0].first;
    vector<vector<int>> ans(qtd);
    int pos = 0;

    int qtdB = vet[1].first;
    while(qtdB > 0) {
      ans[pos].pb(1);
      qtdB--;
      pos++;
      if (pos == qtd) pos = 0;
    }

    int qtdC = vet[2].first;
    while(qtdC > 0) {
      ans[pos].pb(2);
      qtdC--;
      pos++;
      if (pos == qtd) pos = 0;
    }

    string resp = "";
    for (int i = 0; i < qtd; i++){
      resp += m[0];
      for (int j = 0; j < ans[i].size(); j++){
        resp += m[ans[i][j]];
      }
    }

    printf("Case #%d: ", cases++);
    for (int i = 0; i < resp.size(); i++){
      if (resp[i] == 'B' && O > 0) {
        printf("B");
        for (int j = 0; j < O; j++) {
          printf("OB");
        }
        O = 0;
        continue;
      }
      if (resp[i] == 'R' && G > 0) {
        printf("R");
        for (int j = 0; j < G; j++) {
          printf("GR");
        }
        G = 0;
        continue;
      }
      if (resp[i] == 'Y' && V > 0) {
        printf("Y");
        for (int j = 0; j < V; j++) {
          printf("VY");
        }
        V = 0;
        continue;
      }
      printf("%c", resp[i]);
    }
    printf("\n");
  }

  return 0;
}
