#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void solve(istream& ifile) {
  int T = 0;
  ifile >> T;

  for(int i = 0; i < T; ++i) {
    string S = "";
    int K = 0;
    int Q = 0;
    ifile >> S >> K;

    int ans = 0;
    int l = S.length();
    for(int j = 0; j < l; ++j) {
      if(S[j] != '-') continue;
      if((l - j) < K) {
        ans = -1;
        break;
      }
      ++ans;
      for(int k = 0; k < K; ++k) {
        S[j+k] = (S[j+k] == '-')? '+' : '-';
      }
    }

    if(ans < 0)
      cout << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
    else
      cout << "Case #" << (i+1) << ": " << ans << endl;
  }
}

int main(int argc, char** argv) {
  if(argc != 2) { cerr << "Wrong usage." << endl; }
  ifstream ifile(argv[1]);

  solve(ifile);

  return 0;
}
