#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

int main() {
  int T;

  cin >> T;
  for (int t=0; t<T; ++t) {
    ll N, K;
    cin >> N >> K;

    ll bot = N;
    ll block;
    pair<ll, ll> count = make_pair(1, 0);

    ll pow = 1LL;
    ll step = 0LL;

    // cout << 0 << ' ' << count.first << 'x' << bot << ' ' << count.second << 'x' << bot + 1 << endl;

    while (true) {
      if (step + pow < K) {
        step += pow;
      } else {
        if (K - step <= count.second) {
          block = bot + 1LL;
        } else {
          block = bot;
        }

        break;
      }

      if (bot == 1LL) {
        bot = 1LL;
        count = make_pair(count.second, 0);
      } else if (bot%2 == 1LL) {
        bot = bot/2;
        count = make_pair(count.first*2 + count.second, count.second);
      } else {
        bot = (bot-1)/2;
        count = make_pair(count.first, count.first + count.second*2);
      }

      // cout << step << ' ' << count.first << 'x' << bot << ' ' << count.second << 'x' << bot + 1 << endl;

      pow *= 2;
    }

    cout << "Case #" << t + 1 << ": " << block/2 << ' ' << (block-1)/2 << endl;
  }

  return 0;
}
