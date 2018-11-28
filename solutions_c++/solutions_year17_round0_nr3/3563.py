#include <iostream>
#include <fstream>
using namespace std;

void solve(istream& ifile) {
  int T = 0;
  ifile >> T;

  for(int i = 0; i < T; ++i) {
    int N = 0;
    int K = 0;
    ifile >> N >> K;

    int max = 0;
    int min = 0;
    if(K == 1) {
      max = N / 2;
      min = (N - 1) / 2;
    } else {
      max = N / 2;
      min = (N - 1) / 2;
      K -= 1;
      int b1 = 1;
      int b2 = 1;
      while(K > (b1 + b2)) {
        K -= (b1 + b2);
        if(max == min) {
          max = max / 2;
          min = (min - 1) / 2;
          b1 *= 2;
          b2 *= 2;
        } else {
          max = max / 2;
          int min_max = min / 2;
          min = (min - 1) / 2;
          if(min_max != min) {
            b1 = (2 * b1) + b2;
          } else {
            b2 = b1 + (2 * b2);
          }
        }
      }
      if(K > b1) {
        max = min / 2;
        min = (min - 1) / 2;
      } else {
        min = (max - 1) / 2;
        max = max / 2;
      }
    }
    cout << "Case #" << (i+1) << ": " << max << ' ' << min << endl;
  }
}

int main(int argc, char** argv) {
  if(argc != 2) {
    cerr << "Wrong usage." << endl;
    return 0;
  }
  ifstream ifile(argv[1]);

  solve(ifile);

  return 0;
}
