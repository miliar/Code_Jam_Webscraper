#include <iostream>
#include <string>

using namespace std;

main() {
  int T, K;
  cin >> T;
  for (int c=1; c<=T; c++) {
    string S;
    cin >> S >> K;
    int answer = 0, n = S.length();
    for (int i=0; i<n-K+1; i++)
      if (S[i] == '-') {
	for (int j=i; j<i+K; j++)
	  S[j] = S[j] == '-' ? '+' : '-';
	answer ++;
      }
    for (int j=n-K; j<n; j++)
      if (S[j] == '-') answer = -1;

    if (answer >= 0)
      cout << "Case #" << c << ": " << answer << endl; 
    else
      cout << "Case #" << c << ": IMPOSSIBLE" << endl; 
  };
};
