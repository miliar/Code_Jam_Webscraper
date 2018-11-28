#include <iostream>
#include <map>

using namespace std;

map<long long, map<long long, long long> > memo;

void add(long long n, long long l) {
  for(auto it = memo[l].begin(); it != memo[l].end(); ++it) {
    long long spaces = it->first;
    long long amount = it->second;
    if(memo[n].count(spaces) == 0) {
      memo[n][spaces] = 0;
    }
    memo[n][spaces] += amount;
  }
}

void count(long long n) {
  if(memo.count(n) == 1) return;
  if(n == 0) return;

  memo[n][n] = 1;
  long long a = (n-1)/2;
  long long b = (n-1)/2 + ((n-1) % 2);
  count(a);
  count(b);
  add(n, a);
  add(n, b);
}

void solve(long long K, long long N) {
  count(N);
  for(auto it = memo[N].rbegin(); it != memo[N].rend(); ++it) {
    K -= it->second;
    if(K <= 0) {
      long long n = it->first;
      long long a = (n-1)/2;
      long long b = (n-1)/2 + ((n-1) % 2);
      cout << b << " " << a;
      break;
    }
  }
}

int main() {

  int T;
  cin >> T;

  for(int i = 0; i < T; ++i) {
    cout << "Case #" << (i+1) << ": ";
    long long K, N;
    cin >> N >> K;
    solve(K, N);
    cout << endl;
  }

  return 0;
}
