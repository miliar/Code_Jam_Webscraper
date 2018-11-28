#include <cstdio>
#include <iostream>
#include <queue>
#include <utility>

using namespace std;

void solve(int t){
    priority_queue <int> q;
    int N, K;
    cin >> N >> K;
    pair<int, int> last;
    q.push(N);
    for (int i = 0; i < K; ++i)
    {
      int space = q.top();
      q.pop();
      int mid = (space+1)/2;
      int L = mid-1;
      int R = space-mid;
      last = make_pair(max(L,R), min(L,R));
      q.push(R);
      q.push(L);
    }
    cout << "Case #" << t << ": " << last.first << " " << last.second << endl;

}
int main(int argc, char const *argv[])
{
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i)
  {
    solve(i+1);
  }
  return 0;
}


