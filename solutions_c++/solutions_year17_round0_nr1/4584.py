#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for(int i = 0; i < (int) (n); i++)

int tc, k, TC, am;
string s;

char no(char a){
  if(a == '+') return '-';
  return '+';
}

void stfp(int pos){
  if(pos + k > (int) s.size()){
    return;
  }
  forn(i, k){
    s[pos + i] = no(s[pos + i]);
  }
}

int main(){
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  
  scanf("%d", &tc);
  while(tc--){
    cin >> s; scanf("%d", &k); am = 0;
    forn(i, s.size()){
      if(s[i] == '-'){
        stfp(i);
        am++;
      }
    }
    bool ok = true;
    forn(i, s.size()){
      if(s[i] == '-'){
        ok = false;
      }
    }
    printf("Case #%d: ", ++TC);
    if(ok) printf("%d\n", am);
    else   printf("IMPOSSIBLE\n");
  }
  return 0;
}
