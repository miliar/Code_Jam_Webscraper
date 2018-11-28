#include <bits/stdc++.h>
using namespace std;

#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define cl(x, v) memset((x), (v), sizeof(x))

#define db(x) cerr << #x << " == " << x << endl
#define dbs(x) cerr << x << endl
#define _ << ", " <<

typedef long long ll;
typedef long double ld;

typedef pair<int, int> pii;
typedef pair<int, pii> piii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

const ld EPS = 1e-9, PI = acos(-1.);
const int INF = 0x3f3f3f3f, MOD = 1e9+7;
const int N = 1e4+5;

int t, n, ok;
int v[8];
int ord[3*N];

void encaixar(int x) {
  for(int i=0; i<v[x]; i++) ord[3*i] = x;
  for(int i=0; i<v[x]; i++) {
    int y = (x+2)%6;
    if(v[y]) {
      ord[3*i+1] = y;
      v[y]--;
      continue;
    }
    y = (y+2)%6;
    if(v[y]) {
      ord[3*i+1] = y;
      v[y]--;
      continue;
    }
  }

  for(int i=0; i<v[x]; i++) {
    int y = (x+2)%6;
    if(v[y]) {
      ord[3*i+2] = y;
      v[y]--;
      continue;
    }
    y = (y+2)%6;
    if(v[y]) {
      ord[3*i+2] = y;
      v[y]--;
      continue;
    }
  }
}

void imprimir(int x) {
  if(x == 0) {
    printf("R");
    for(int i=0; i<v[3]; i++)
      printf("GR");
    v[3] = 0;
  }
  if(x == 2) {
    printf("Y");
    for(int i=0; i<v[5]; i++)
      printf("VY");
    v[5]=0;
  }
  if(x == 4) {
    printf("B");
    for(int i=0; i<v[1]; i++)
      printf("OB");
    v[1]=0;
  }
}

int main() {
  scanf("%d", &t);
  for(int tt=1; tt<=t; tt++) {
    cl(ord, -1);
    scanf("%d", &n);

    for(int i=0; i<6; i++) scanf("%d", &v[i]);
    printf("Case #%d: ", tt);

    if(v[0] == v[3] && v[0]*2 == n) {
      for(int i=0; i<v[3]; i++) printf("RG");
      printf("\n");
      continue;
    }
    if(v[2] == v[5] && v[2]*2 == n) {
      for(int i=0; i<v[5]; i++) printf("YV");
      printf("\n");
      continue;
    }
    if(v[4] == v[1] && v[4]*2 == n) {
      for(int i=0; i<v[1]; i++) printf("OB");
      printf("\n");
      continue;
    }

    ok = 1;

    if(v[1]) {
      if(v[4] <= v[1]) ok=0;
      else {
        v[4]-=v[1];
        n-=2*v[1];
      }
    }
    if(v[5]) {
      if(v[2] <= v[5]) ok=0;
      else {
        v[2]-=v[5];
        n-=2*v[5];
      }
    }
    if(v[3]) {
      if(v[0] <= v[3]) ok=0;
      else {
        v[0]-=v[3];
        n-=2*v[3];
      }
    }
    //db(v[0] _ v[2] _ v[4] _ n);
    if(2*v[0] > n or 2*v[2] > n or 2*v[4] > n) ok = 0;


    if(!ok) printf("IMPOSSIBLE\n");
    else {
      int x;
      if(v[0] > v[2] and v[0] > v[4]) x = 0;
      else if(v[2] > v[4]) x = 2;
      else x = 4;

      encaixar(x);
      for(int i=0; i<3*n; i++) {
        if(ord[i] != -1) imprimir(ord[i]);
      }
      printf("\n");

    }

  }
  return 0;
}
