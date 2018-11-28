#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>

using namespace std;

int main()
{
  int T;

  ofstream output;
  ifstream input;
  int D, N, K, S;
  double maxT;
  input.open("input.in");
  output.open ("output.out");
  input >> T;
  for (int test = 0; test < T; ++test){
      input >> D >> N;
      maxT = 0;
      for (int j = 0; j < N; ++j){
          input >> K >> S;
          maxT = max(maxT, (D - K) / (S * 1.0));
      }
      output << "Case #" << test + 1 << ": " << fixed << setprecision(6) << D / maxT << endl;
  }
  output.close();
  input.close();
  return 0;
}
