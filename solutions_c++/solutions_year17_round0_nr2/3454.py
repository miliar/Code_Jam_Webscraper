#include <iostream>
#include <fstream>
using namespace std;

void solve(istream& ifile) {
  int T = 0;
  ifile >> T;

  for(int i = 0; i < T; ++i) {
    string N = "";
    ifile >> N;

    int l = N.length();
    for(int j = (l - 1); j > 0; --j) {
      if(N[j] >= N[j-1]) continue;
      for(int k = j; k < l; ++k) {
        if(N[k] == '9') break;
        N[k] = '9';
      }
      N[j-1] = char((int)N[j-1] - 1);
    }
    if(N[0] == '0') N = N.substr(1);

    cout << "Case #" << (i+1) << ": " << N << endl;
  }
}

int main(int argc, char** argv) {
  if(argc != 2) { cerr << "Wrong usage." << endl; }
  ifstream ifile(argv[1]);

  solve(ifile);

  return 0;
}
