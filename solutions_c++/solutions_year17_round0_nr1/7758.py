#include <iostream>
#include <string>
#define FOR(i, n) for(int i = 0; i < n; i++)
#define SOL(x) cout << "Case #" << tc << ": " << (x) << "\n"

using namespace std;

int main(){
  int tcn; cin >> tcn;
  for(int tc = 1; tc <= tcn; tc++){
    string s;
    int k;
    cin >> s >> k;
    int n = s.size();
    int flips = 0;

    for(int i = 0; i <= n-k; i++){
      if(s[i] != '+'){
        flips++;
        for(int j = 0; j < k; j++){
          s[i+j] = s[i+j]=='-'?'+':'-';
        }
      }
    }

    bool pos = true;
    FOR(i, n){
      if(s[i] != '+'){
        pos = false;
        break;
      }
    }
    if(pos){
      SOL(flips);
    } else {
      SOL("IMPOSSIBLE");
    }
  }
}
