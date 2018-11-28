#include <iostream>
#include <string>

using namespace std;

int T = 0;

void swap(string&S, int begin, int end) {
  for (int j = begin; j < end; j++) {
    if (S[j] == '-') {
      S[j] = '+';
    } else {
      S[j] = '-';
    }
  }
}

int solve(string& S, int K) {
  int count = 0;
  const int S_size = S.size();
  const int index_max = S_size - K + 1;

  int index = 0;
  while (index < index_max) {
    if (S[index] == '+') {
      index++;
      continue;
    }
    count++;

    int m = index + 1;
    while (m < index + K && m < index_max) {
      if (S[m] == '+') {
        break;
      }
      m++;
    }

    if (m < index + K) {
      int begin = index + K;
      int end = m + K;
      if (m == index_max) {
        begin = index;
        end = index + K;
      } else {
        count++;
      }
      swap(S, begin, end);
    }
    index = m;
  }

  int j = S_size - K + 1;
  if (j < 0) {
    j = 0;
  }

  for (int i = j; i < S_size; i++) {
    if (S[i] == '-') {
      return -1;
    }
  }

  return count;
}


int main() {

  string S;
  int K;
  int ret;

  cin >> T;
  for (int i = 1; i <= T; i++) {
    cin >> S >> K;
    ret = solve(S, K);
    cout << "Case #" << i << ": ";
    if (ret == -1) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << ret << endl;
    }
  }

  return 0;
}
