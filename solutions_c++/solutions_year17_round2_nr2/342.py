#include <bits/stdc++.h>

#define mt make_tuple
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<string> vs;

vector<char> cKleur = {'R','Y','B','O','G','V'};

bool can(int n, vi kleur, vi &res){
  if(n == 1){
    for(int i = 0 ; i < 6 ; i++)
      if(kleur[i] == 1)
        res.assign(1,i);
    return true;
  }
  bool prim = true;
  for(int i = 3; i < 6; i++)
    prim &= (kleur[i] == 0);
  if(prim){
    if(2*max(kleur[0],max(kleur[1],kleur[2]))>
      kleur[0]+kleur[1]+kleur[2])
      return false;
    int mKleur = 0, mI = -1;
    for(int i = 0 ; i < 3 ; i++){
      if(kleur[i] > mKleur){
        mKleur = kleur[i];
        mI = i;
      }
    }
    int i = mI;
    int j = (i+1)%3, k = (i+2)%3;
    for(int m = 0 ; m < mKleur ; m++){
      res.pb(i);
      if(m<kleur[j])
        res.pb(j);
      if(mKleur-m <= kleur[k])
        res.pb(k);
    }
    return true;
  }
  int som = 0;
  for(int i = 0 ; i < 6 ; i++)
    som += kleur[i];
  if(som == kleur[3]+kleur[2]){
    if(kleur[3]!=kleur[2])
      return false;
    for(int i = 0 ; i < kleur[3]; i++){
      res.pb(3);
      res.pb(2);
    }
    return true;
  }
  if(som == kleur[0]+kleur[4]){
    if(kleur[0]!=kleur[4])
      return false;
    for(int i = 0 ; i < kleur[0]; i++){
      res.pb(0);
      res.pb(4);
    }
    return true;
  }
  if(som == kleur[1]+kleur[5]){
    if(kleur[1]!=kleur[5])
      return false;
    for(int i = 0 ; i < kleur[1]; i++){
      res.pb(1);
      res.pb(5);
    }
    return true;
  }
  if(kleur[3]>=kleur[2]||
     kleur[4]>=kleur[0]||
     kleur[5]>=kleur[1])
     return false;
  vi nKleur = {kleur[0]-kleur[4],kleur[1]-kleur[5],kleur[2]-kleur[3],0,0,0};
  vi nres;
  if(can(n,nKleur,res)){
    for(int i = 0 ; i < res.size(); i++){
      nres.pb(res[i]);
      if(res[i] == 0){
        for(;kleur[4]>0;kleur[4]--){
          nres.pb(4);
          nres.pb(0);
        }
      }
      if(res[i] == 1){
        for(;kleur[5]>0;kleur[5]--){
          nres.pb(5);
          nres.pb(1);
        }
      }
      if(res[i] == 2){
        for(;kleur[3]>0;kleur[3]--){
          nres.pb(3);
          nres.pb(2);
        }
      }
    }
    res = nres;
    return true;
  }
  return false;
} 

//          b, r, y
// r, y, b, o, g, v
// 0, 1, 2, 3, 4, 5

void test(){
  int n;
  vi kleur(6);
  cin >> n >> kleur[0] >> kleur[3] >> kleur[1] >> kleur[4]
  >> kleur[2] >> kleur[5];
  vi res;
  if(can(n,kleur, res)){
    assert(n == res.size());
    for(int a: res)
      cout << cKleur[a];
    cout << endl;
    return;
  }
  cout << "IMPOSSIBLE" << endl;
}

int main(){
    int t;
    cin >> t;
    for( int i = 1;i<= t;i++){
        cout << "Case #" << i << ": ";
        test();
    }
	return 0;
}
