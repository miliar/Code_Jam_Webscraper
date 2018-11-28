#include <iostream>
#include <string>
#include <map>
#include <deque>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

pair<int, int> solve(int N, int K)
{
  map<int, int> len_cnt;
  deque<int> len_heap;
  pair<int, int> res;
  int max_free = 0, len_max = 0, len_min = 0;

  len_cnt[N] = 1;
  len_heap.push_back(N);

  for (int i = 0; i < K; i++)
  {
    // check whether any runs left (shouldn't really be a problem)
    if (len_heap.size()>0)
    {
      // get longest free run
      max_free = len_heap[0];
      // reduce count by one, and remove if zero remain
      len_cnt[max_free]--;
      if (!len_cnt[max_free])
      {
        len_heap.pop_front();
        len_cnt.erase(max_free);
      }
      // calc resulting split run lengths
      // increment counts
      // push into heap
      len_max = floor(max_free/2);
      len_cnt[len_max]++;
      if (len_cnt[len_max] == 1)
        len_heap.push_back(len_max);

      len_min = max_free - len_max - 1;
      len_cnt[len_min]++;
      if (len_cnt[len_min] == 1)
        len_heap.push_back(len_min);
      // fix heap
      make_heap(len_heap.begin(), len_heap.end());
    }
  }
  res.first = len_max;
  res.second = len_min;
  return res;
}

int main(int argc, char * argv[])
{
  pair<int, int> res;
  int nr_cases, N, K;
  cin >> nr_cases;

  for (int cas = 1; cas <= nr_cases; cas++)
  {
    cin >> N;
    cin >> K;

    res = solve(N, K);

    cout << "Case #" << cas << ": " << res.first << " " << res.second << endl;
  }
}
