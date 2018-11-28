#include <stdio.h>
#include <iostream>
#include <vector>
#include <assert.h>
#include <math.h>
using namespace std;

int R[100];

struct Stt {
  int num;
  int nid;
  bool start;
};

struct Less {
  bool operator() (Stt a, Stt b)
  {
    if (a.num != b.num) return (a.num < b.num);
    if (a.start != b.start) return a.start;
    return a.nid < b.nid;
  }
};

bool check_all_have(int* lo, int N) {
  for (int i = 0; i < N; i++) if (lo[i] == 0) return false;
  return true;
}

int main()
{
  int numTests;
  cin >> numTests;
  for (int test = 1; test <= numTests; test++) {
    int N, P;
    cin >> N >> P;
    for (int i = 0; i < N; i++) cin >> R[i];
    std::vector<Stt> arr;
    for (int i = 0; i < N; i++)
      for (int j = 0; j < P; j++) {
        int q;
        cin >> q;
        int left =  ceil(q / (1.1 * R[i]));
        int right = floor(q / (0.9 * R[i]));
        if (left <= right) {
          Stt left_st, right_st;
          left_st.num = left; left_st.nid = i; left_st.start = true;
          right_st.num = right; right_st.nid = i; right_st.start = false;
          arr.push_back(left_st); arr.push_back(right_st);
        }
      }

    std::sort(arr.begin(), arr.end(), Less());
    int answer = 0;
    int left_over[100], removed[100];
    for (int i = 0; i < N; i++) {
      left_over[i] = 0;
      removed[i] = 0;
    }
    for (int i = 0; i < arr.size(); i++) {
      if (arr[i].start) {
        left_over[arr[i].nid] ++;
        while (check_all_have(left_over, N)) {
          answer ++;
          for (int j = 0; j < N; j++) removed[j]++;
          for (int j = 0; j < N; j++) left_over[j]--;
        }
      } else {
        if (removed[arr[i].nid] > 0)
          removed[arr[i].nid]--;
        else {
          assert(left_over[arr[i].nid] > 0);
          left_over[arr[i].nid] --;
        }
      }
    }
    cout << "Case #" << test << ": " << answer << endl;
  }
}
