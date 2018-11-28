#include <iostream>
#include <map>
using namespace std;

int T;
long long N, K;
map<long long, long long> M;

long long f() {
  long long longest = M.rbegin()->first;
  long long cnt = M[longest];

  if (cnt > K)
    cnt = K;

  long long left = (longest - 1) / 2;
  long long right = longest / 2;

  M[longest] -= cnt;
  if (M[longest] == 0) M.erase(longest);

  M[left] += cnt;
  M[right] += cnt;

  return cnt;
}

int main(int argc, char** argv) {
  cin >> T;
  for (int t = 0; t < T; ++t) {
    cin >> N >> K;
    M.clear();
    M[N] = 1;

    --K;
    while (K > 0) {
      K -= f();
    }

    cout << "Case #" << (t + 1) << ": "
      << (M.rbegin()->first / 2) << " "
      << ((M.rbegin()->first - 1) / 2) << endl;
  }

  return 0;
}
