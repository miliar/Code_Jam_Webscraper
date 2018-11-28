#include <bits/stdc++.h>

using namespace std;
#define int long long
#define all(a) (a).begin(), (a).end()
#define ms(a,v) memset(a, v, sizeof(a))
#define sz(v) ((int)(v).size())
#define mp make_pair
#define pb push_back
#define prev biiiiirl_sai_de_casa_comi_pra_caralho
#define next trapezio_descendente
#define index eh_ele_que_nos_vai_buscar
#define left aqui_eh_37_anos_porra
#define R32 ({int32_t x; scanf("%d", &x); x;})
#define RL ({long long x; scanf("%lld", &x); x;})
#define RC ({char x; scanf(" %c", &x); x;})
#define RI RL
#define ff first
#define ss second
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef long long ll;

const int N = 1005;
int L[N];
int R[N];
int occ[N];
int n;

void fill(int x){
  for(int i = x; i >= 0; i--){
    if(occ[i]) break;
    R[i] = x-i;
  }

  for(int i = x; i < n+2; i++){
    if(occ[i]) break;
    L[i] = i-x;
  }

  occ[x] = 1;
}

void solve(int tn){
  n = RI;
  int K = RI;

  ms(occ, 0);
  ms(L, 0x3f);
  ms(R, 0x3f);
  fill(0);
  fill(n+1);
  while(K--){

    tuple<int, int, int> best = make_tuple(0, 0, 0);
    for(int i = 1; i <= n; i++){
      int left = L[i];
      int right = R[i];
      best = max(best, make_tuple(min(left, right), max(left, right), i));
    }

    fill(get<2>(best));
    if(K == 0){
      cout<< "Case #" << tn << ": ";
      cout << get<1>(best)-1 << " " << get<0>(best)-1 << endl;
    }
  }
}

int32_t main(){
    // YOU SHALL CLEAR DAMN VARIABLES BEFORE EACH TEST
  // WITH MEMSET
  int T = RI;
  for(int tn = 1; tn <= T; tn++)
    solve(tn);
}
