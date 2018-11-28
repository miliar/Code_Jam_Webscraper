#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

inline void flip(char& c) {
  c == '-' ? c = '+' : c = '-';
}

int main() {  
  int T;
  
  cin >> T;

  for(int i = 1; i <= T; ++i) {        
    string S;
    int K;
    
    cin >> S >> K;
    
    int flips = 0;
    int c = 0;
    
    for(c = 0; c <= S.size() - K; ++c) {
      if(S[c] == '-') {
	for(int k = 0; k < K; ++k)
	  flip(S[c+k]);

	++flips;
      }
    }

    for(; c < S.size(); ++c)
      if(S[c] == '-') {
	flips = -1;
	break;
      }	

    if(flips == -1)
      cout << "Case #" << i << ": IMPOSSIBLE\n";
    else
      cout << "Case #" << i << ": " << flips << '\n';
  }
}
