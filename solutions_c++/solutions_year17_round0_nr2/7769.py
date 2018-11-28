#include <iostream>
#include <vector>
#include <string>
#define FOR(i, n) for(int i = 0; i < n; i++)
#define SOL(x) cout << "Case #" << tc << ": " << (x) << "\n"
#define DEB(x) //x

using namespace std;
using ll=long long int;

int main(){
  int tcn; cin >> tcn;
  for(int tc = 1; tc <= tcn; tc++){
    string N; cin >> N;
    int n = N.size();
    vector<int> digs(n);
    FOR(i, n){
      digs[i] = N[i] - '0';
    }

    DEB(cerr << "n: " << n << endl; FOR(i, n) cerr << digs[i]; cerr << endl;)

    int st = -1;
    while(true){
      st = -1;
      FOR(i, n-1){
        if(digs[i] > digs[i+1]){
          st = i;
          break;
        }
      }

      DEB(cerr << "st: " << st << endl;)

      if(st != -1){
        digs[st]--;
        for(int i = st+1; i < n; i++){
          digs[i] = 9;
        }
      } else {
        break;
      }
    }

    for(st = 0; st < n && digs[st]==0; st++);
    cout << "Case #" << tc << ": ";
    for(int i = st; i < n; i++){
      cout << digs[i];
    }
    cout << "\n";
  }
}
