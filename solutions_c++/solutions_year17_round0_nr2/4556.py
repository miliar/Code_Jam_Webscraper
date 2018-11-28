#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for(int i = 0; i < (int) (n); i++)
typedef long long tint;

string n;
int tc, TC;

bool ok(){
  int last = 0;
  forn(i, n.size()){
    int d = n[i] - '0';
    if(d < last){
      return false;
    }
    last = d;
  }
  return true;
}

void process(){
  int last = 0;
    forn(i, n.size()){
      int d = n[i] - '0';
      if(d < last){
        n[i - 1]--;
        for(int j = i; j < (int) n.size(); j++){
          n[j] = '9';
        }
        break;
      }
      last = d;
    }
    
    if(n[0] == '0') n = n.substr(1);
}

int main(){
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  
  scanf("%d", &tc);
  while(tc--){
    cin >> n;
    
    while(!ok()){
      process();
    }
    
    printf("Case #%d: %s\n", ++TC, n.c_str());
  }
  return 0;
}
