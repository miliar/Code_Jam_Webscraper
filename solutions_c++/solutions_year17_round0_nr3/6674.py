#include <iostream>
#include <vector>

using namespace std;

void computeNums(long long N, long long K, long long* y, long long* z) {
  vector<bool> stall_status;
  vector<long long> left_distance;
  vector<long long> right_distance;
  for (long long i = 0; i < N; ++i) {
    stall_status.push_back(false);
    left_distance.push_back(i);
    right_distance.push_back(N - i - 1);
  }

  for (long long i = 0; i < K; ++i) {
    // Find the maximum min(L_s, R_s).
    long long max_dis = -1;
    for (long long j = 0; j < N; ++j) {
      if (stall_status[j]) continue;
      long long dis = min(left_distance[j], right_distance[j]);
      if (dis > max_dis) {
        max_dis = dis;
      }
    }
    // Of all the S that are maximum min(L_s, R_s) find the one with maximum
    // max(L_s, R_s);
    long long max_max_dis = -1;
    long long stall_to_fill = -1;
    for (long long j = 0; j < N; ++j) {
      if (stall_status[j]) continue;
      long long a = min(left_distance[j], right_distance[j]);
      if (a == max_dis) {
        long long b = max(left_distance[j], right_distance[j]);
        if (b > max_max_dis) {
          max_max_dis = b;
          stall_to_fill = j;
        }
      }
    }
    stall_status[stall_to_fill] = true;
    *y = max(left_distance[stall_to_fill], right_distance[stall_to_fill]);
    *z = min(left_distance[stall_to_fill], right_distance[stall_to_fill]);

    // Update left_distance and right_distance;
    long long curr_dis = 0;
    for (long long j = 0; j < N; ++j) {
      if (stall_status[j]) {
        left_distance[j] = -1;
        curr_dis = 0;
      } else {
        left_distance[j] = curr_dis;
        curr_dis++;
      }
    }
    curr_dis = 0;
    for (long long j = N - 1; j >= 0; --j) {
      if (stall_status[j]) {
        right_distance[j] = -1;
        curr_dis = 0;
      } else {
        right_distance[j] = curr_dis;
        curr_dis++;
      }
    }
  }
}

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    long long N;
    cin >> N;
    long long K;
    cin >> K;
    long long y, z;
    computeNums(N, K, &y, &z);
    cout << "Case #" << i << ": " << y <<  " " << z << endl;
  }
  return 0;
}
