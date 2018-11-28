#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int T;
int way[1001];

int main(){

  cin >> T;

  for (int cas=1; cas<=T; cas++){
    string s; int K;
    cin >> s >> K;

    for (int i=0; i<s.length(); i++)
      way[i] = (s[i] == '-')? 0:1;

    int count = 0;
    for (int i=0; i<s.length()-K+1; i++){
      if (way[i] == 0){
        // cout << i << endl;
        count += 1;
        for (int j = i; j < i + K; j++){
          if (way[j] == 1) way[j] = 0;
          else way[j] = 1;
        }
      }
    }

    bool possible = true;
    for (int i=0; i<s.length(); i++){
      if (way[i] == 0) possible = false;
    }
    if(possible){
      cout << "Case #" << cas << ": " << count << endl;
    }else{
      cout << "Case #" << cas << ": IMPOSSIBLE" << endl;
    }



  }



  return 0;
}
