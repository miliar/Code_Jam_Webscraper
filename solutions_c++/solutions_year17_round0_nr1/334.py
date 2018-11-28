#include <iostream> 
using namespace std;

void solve_case(int T){
	string inp;
  int row[2000];
  int N, ans = 0, K;

  cin >> inp;
  cin >> K;
  N = inp.size();

  for (int i = 0; i < N; i++){
    if (inp[i] == '-'){
      row[i] = 1;
    } else {
      row[i] = 0;
    }
  }

  for (int i = 0; i < N; i++){
    if (row[i] == 1){
      if (i > N - K){
        goto failed;
      }
      for (int j = 0; j < K; j++){
        row[i + j] = 1 - row[i + j];
      }
      ans++;
    }
  }

  cout << "Case #" << T << ": " << ans << endl;
  return;

  failed:
	cout << "Case #" << T << ": IMPOSSIBLE" << endl;
  return;
}

int main() {
  	int t;
  	cin >> t; 
  	for (int i = 1; i <= t; i++) {
  	  	solve_case(i);
  	}
  	return 0;
}