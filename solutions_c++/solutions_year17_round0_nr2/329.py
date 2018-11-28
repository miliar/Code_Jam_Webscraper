#include <iostream> 
using namespace std;

void solve_case(int T){
	string N;
	cin >> N;

  if (N.size() == 1){
    cout << "Case #" << T << ": " << N << endl;
    return;
  }

  string A[50];
  A[N.size() - 1] = N[N.size() - 1];

  bool larger;
  for (int i = N.size() - 2; i >= 0; i--){
    larger = false;
    for (int j = 0; j < A[i+1].size(); j++){
      if (N[i] > A[i+1][j]){
        larger = true;
      }
    }
    if (larger){
      A[i] = N[i] - 1;
      for (int j = i + 1; j < N.size(); j++){
        A[i].push_back('9');
      }
    } else {
      A[i] = N[i];
      A[i].append(A[i+1]);
    }
  }

  if (A[0][0] == '0'){
    cout << "Case #" << T << ": " << A[0].substr(1,N.size()-1) << endl;
  } else {
    cout << "Case #" << T << ": " << A[0] << endl;
  }
}

int main() {
  	int t;
  	cin >> t; 
  	for (int i = 1; i <= t; i++) {
  	  	solve_case(i);
  	}
  	return 0;
}