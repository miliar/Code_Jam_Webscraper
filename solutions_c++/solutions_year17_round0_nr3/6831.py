#include <iostream>
#include <vector>

using namespace std;

int main() {
  int T, t;
  long long N, n, K, k, size, start, end, max_size, pos, max_pos, left, right;

  cin >> T;
  for(t = 1; t <= T; t++) {
    cin >> N;
    cin >> K;

    vector<bool> stalls(N, false);

    for(k = 0; k < K; k++) {
      start = 0;
      end = 0;
      max_size = 0;
      max_pos = 0;
      for(n = 0; n < N; n++) {
        if(stalls[n]) {
          end = n - 1;
          size = end - start + 1;
          pos = (end + start)/2;
          start = n+1;

          if(size > max_size) {
            max_size = size;
            max_pos = pos;
          }
        }
      }

      end = N - 1;
      size = end - start + 1;
      if(size > max_size) {
        max_size = size;
        max_pos = (end + start)/2;
      }

      // pos = (start + end)/2;
      // cout << max_size << " " << max_pos << endl;
      stalls[max_pos] = true;

      // for(n = 0; n < N; n++) {
      //   cout << stalls[n] << " ";
      // } cout << endl;
    }

    left = (max_size+1)/2 - 1;
    right = max_size - left - 1;

    cout << "Case #" << t << ": " << max(right, left) << " " << min(right, left) << endl;
  }

  return 0;
}
