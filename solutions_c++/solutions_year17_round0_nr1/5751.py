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

void solve(int tn){
  string s;
  cin >> s;
  int n = s.size();
  vector<int> v;
  for(char c : s ) v.push_back(c=='-');

  int ans = 0;
  int K = RI;
  for(int i = 0; i < n-K+1; i++){
    ans += v[i];
    for(int j = i+1; j< i+K; j++)
      v[j] ^= v[i];
    v[i] =0;
  }

  vector<int> vv(n);

  cout << "Case #" << tn << ": ";
  if(v != vv)
    cout << "IMPOSSIBLE" << endl;
  else cout << ans << endl;

}

int32_t main(){
    // YOU SHALL CLEAR DAMN VARIABLES BEFORE EACH TEST
  // WITH MEMSET
  int T = RI;
  for(int tn = 1; tn <= T; tn++)
    solve(tn);
}
