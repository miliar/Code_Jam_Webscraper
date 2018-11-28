#include<iostream>
#include<string>
#include<set>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    long long N, K;
    cin >> N >> K;
    long long pow2 = 1;
    while (K > pow2) {
      K -= pow2;
      pow2 *= 2;
    }
    long long partition = N%pow2 + 1;
    long long  last_space = N/pow2;
    if (K > partition) last_space -= 1;
    cout << "Case #" << cas << ": " << last_space/2 << " " << last_space - last_space/2 - 1 << endl;
  }
}
