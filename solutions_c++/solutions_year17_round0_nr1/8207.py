#include <fstream>
#include <string>

using namespace std;

int main() {
  string filename = "A-large";
  ifstream fin(filename + ".in");
  ofstream fout(filename + ".out");
  int num_tests; fin >> num_tests;

  for (int num_test = 0; num_test < num_tests; ++num_test) {
    string pancackes;
    int K, swaps{0};
    fin >> pancackes >> K;
    for (int i = 0; i <= pancackes.size() - K; ++i) {
      if (pancackes[i] == '-') {
        ++swaps;
        for (int j = i; j < i + K; ++j) {
          pancackes[j] = (pancackes[j] == '+') ? '-' : '+'; 
        }
      }
    }
    auto minus = pancackes.find('-');
    fout << "Case #" << num_test + 1 << ": ";
    fout << ((minus == string::npos) ? to_string(swaps) : "IMPOSSIBLE") << endl;
  }

  fin.close();
  fout.close();

  return 0;
}

