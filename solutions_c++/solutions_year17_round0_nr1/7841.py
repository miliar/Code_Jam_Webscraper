#include <iostream>
#include <string>
#include <vector>

using namespace std;



int flips(const string &pancakes, const int K){
  vector<bool> cakes(pancakes.size());
  // cout << pancakes << '\n';
  for (int i=0; i < cakes.size(); i++){
    cakes[i] = (pancakes[i] == '+');
  }
  int flips = 0;
  for (int i=0; i <= cakes.size() - K; i++){
    if (!cakes[i]){
      // cout << "flip " << i << '\n';
      flips++;
      for(int j=i; j < i + K; j++){
	cakes[j] = !cakes[j];
      }
    }
  }
  for (int i = cakes.size() - K + 1; i < cakes.size(); i++){
    if (!cakes[i]){
      return -1;
    }
  }
  return flips;
}



int main() {
  std::ios::sync_with_stdio(false);

  int T = 0;
  cin >> T;

  for (int i = 1; i<=T; ++i){
    string s;
    int K = 0;
    cin >> s;
    cin >> K;

    int total_flips = flips(s, K);
    cout << "Case #" << i << ": ";
    if (total_flips >= 0) {
      cout << total_flips;
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << '\n';
  }

  return 0;
}
