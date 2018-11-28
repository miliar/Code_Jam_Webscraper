#include <iostream>
#include <string>

using namespace std;

int main(int agrc, char **argv) {

  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
  	int K;
  	cin >> K;

    int lastTidy = 1;
    for(int i = 1; i <= K; i++){
      string s = std::to_string(i);
      char const *digits = s.c_str();
      int isTidy = 1;
      for(int j = 1; j < s.size(); j++){
        if(digits[j] < digits[j-1]){
          isTidy = 0;
          break;
        }
        
      }

      if(isTidy == 1)
        lastTidy = i;

    }

    cout << "Case #" << t << ": " << lastTidy << endl;

  }

  return 0;

}