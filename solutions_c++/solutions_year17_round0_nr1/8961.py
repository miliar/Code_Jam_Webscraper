#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);

  int T;

  cin >> T;

  for(int t = 1 ; t <= T ; t++){
    int K,cnt=0;
    string S;
    cin >> S >> K;
    int len = S.size();

    for(int i=0 ;i<len-K+1 ;i++){
      if(S[i] == '-'){
        for(int j=0 ; j<K ; j++){
          if(S[i+j] == '-')
            S[i+j] = '+';
          else
            S[i+j] = '-';
        }
        cnt++;
      }
    }

    for(int i=0 ;i<K;i++){
      if(S[len-1-i] == '-'){
        cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        cnt = -1;
        break;
      }
    }
    if(cnt!=-1)
      cout << "Case #" << t << ": " << cnt << endl;

  }


  return 0;
}
