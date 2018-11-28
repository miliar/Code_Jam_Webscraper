#include <iostream>
#include <vector>

using namespace std;

void solve(unsigned long long N) {
  vector<char> result;
  while(N / 10 > 0) {

    int ones = N % 10;
    int tens = (N / 10) % 10;

    if(tens > ones) {
      N -= 10;
      for(int i = 0; i < result.size(); ++i) {
        result[i] = '9';
      }
      result.push_back('9');
    }
    else {
      result.push_back(ones + '0');
    }

    N /= 10;
  }

  if(N != 0) result.push_back(N + '0');

  for(int i = result.size() - 1; i >= 0; --i) {
    cout << result[i];
  }
}

int main() {

  int T;
  cin >> T;

  for(int i = 0; i < T; ++i) {
    cout << "Case #" << (i+1) << ": ";
    unsigned long long N;
    cin >> N;
    solve(N);
    cout << endl;
  }

  return 0;
}
