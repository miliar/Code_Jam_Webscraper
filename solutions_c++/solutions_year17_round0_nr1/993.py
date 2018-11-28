
#include <iostream>
using namespace std;

int main(void) {
  int T; cin >> T;
  for(int ts=1; ts<=T; ts++) {
    string s; cin >> s;
    int K; cin >> K;
    int N=s.size();
    int ret=0;
    for(int i=0; i<=N-K; i++)
      if(s[i]=='-') {
        ret++;
        for(int j=i; j<i+K; j++) s[j]='+'-s[j]+'-';
      }
    cout << "Case #" << ts << ": ";
    if(s==string(N,'+')) cout << ret << endl;
    else cout << "IMPOSSIBLE" << endl;
  }
}
