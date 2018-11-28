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
  int n = RI;
  vi v;
  while(n){
    v.pb(n%10);
    n/=10;
  }

  reverse(all(v));
  cout << "Case #" << tn << ": ";

  vector<int> res;

  int pref = 0;

  for(int i = 0; i < v.size(); i++){
    if(i && v[i] < v[i-1])
      break;

    if(i+1 == v.size() || v[i+1] > v[i])
      pref = i+1;
  }

  for(int i = 0; i < pref; i++){
    res.pb(v[i]);
  }

  if(pref < v.size())
    res.pb(v[pref]-1);

  for(int i = pref+1; i < v.size(); i++)
    res.pb(9);

  if(!res.front())
    res.erase(res.begin());
  for(int x : res) cout << x;
  cout << endl;
}

int32_t main(){
    // YOU SHALL CLEAR DAMN VARIABLES BEFORE EACH TEST
  // WITH MEMSET
  int T = RI;
  for(int tn = 1; tn <= T; tn++)
    solve(tn);
}
