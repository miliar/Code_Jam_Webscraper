#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;


#define LL long long


extern string solve(string N);

int main() {
  int T;
  cin >> T;
  cerr << "T: " << T << endl;
  
  for (int i = 1; i <= T; i++) {
    string N;
    cin >> N;
    
    cout << "Case #" << i << ": ";
    string res = solve(N);
    cout << res << endl;
	}
	return 0;
};

string solve(string N) {
  int res[100] = {0};
  int len = N.length();
  cerr << "initial: " << N << " " << len << endl;
  for (int i = len - 1; i >= 0; i--) {

    // debug
    cerr << "debug: ";
    for (int j = 0; j < len; j++) {
      cerr << res[j];
    }
    cerr << endl;
    
    if (i == (len - 1)) {
      res[i] = N[i] - '0';
      continue;
    }

    if (res[i+1] + '0' >= N[i]) {
      res[i] = N[i] - '0';
    } else {
      res[i] = N[i] - '0' - 1;
      for (int k = i + 1; k < len; k++) {
        res[k] = 9;
      }
    }
  }

  // debug
  cerr << "debug: ";
  for (int j = 0; j < len; j++) {
    cerr << res[j];
  }
  cerr << endl;


  string output = "";
  stringstream ss;
  for (int i = 0; i < len; i++) {
    if (i == 0 && res[i] == 0) {
      continue;
    }
    ss << res[i];
  }
  
  return ss.str();
}
