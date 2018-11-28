#include <iostream>
#include <string>

using namespace std;

int main(){
  string s;
  int T,K;

  cin >> T;

  for(int tc = 1;tc <= T;++tc){
    cin >> s >> K;
    int L = s.size();
    int cont = 0;

    for(int i = 0;i + K - 1 < L;++i){
      if(s[i] == '-'){
        ++cont;
        for(int j = 0;j < K;++j){
          if(s[i + j] == '-') s[i + j] = '+';
          else s[i + j] = '-';
        }
      }
    }

    bool ok = true;

    for(int i = L - K + 1;i < L;++i)
      if(s[i] == '-')
        ok = false;

    cout << "Case #" << tc << ": ";
    if(ok) cout << cont << "\n";
    else cout << "IMPOSSIBLE\n";
  }

  return 0;
}
