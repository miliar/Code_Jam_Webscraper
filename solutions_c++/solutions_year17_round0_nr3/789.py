#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

typedef tuple<int, int, int, int, int> Item;

Item get_optimal_position(int left, int right) {
  int span = right - left - 1;
  return make_tuple(((span-1)/2), (span/2), left + (span-1)/2 + 1, left, right);
}

void solve(int n, int k) {
  vector<Item> v;
  make_heap(v.begin(), v.end());
  v.push_back(get_optimal_position(0, n+1));
  int low = 0;
  int high = 0;
  for (int i = 0; i < k; i++) {
    Item item = v[0];
    pop_heap(v.begin(),v.end()); v.pop_back();
    low = get<0>(item);
    high = get<1>(item);
    int index = get<2>(item);
    int left = get<3>(item);
    int right = get<4>(item);
    v.push_back(get_optimal_position(left, index)); push_heap(v.begin(),v.end());
    v.push_back(get_optimal_position(index, right)); push_heap(v.begin(),v.end());
  }
  cout << high << ' ' << low << endl;
}

int main() {
  int N;
  cin >> N;
  for (int i = 0; i < N; i++) {
    int n, k;
    cin >> n;
    cin >> k;
    cout << "Case #" << i+1 << ": ";
    cout.flush();
    solve(n,k);
  }
}

/*

def solve(n, k):
    #Heap contains tuples (min(ls, rs), max(ls,rs), index, leftbound, rightbound)
    def get_optimal_position(left, right):
        span = right - left - 1
        return (-((span-1)/2), -(span/2), left + (span-1)/2 + 1, left, right)
    h = []
    heapq.heappush(h, get_optimal_position(0, n+1))
    low = 0
    high = 0
    for i in range(k):
        low, high, index, left, right = heapq.heappop(h)
        heapq.heappush(h, get_optimal_position(left, index))
        heapq.heappush(h, get_optimal_position(index, right))
    return -low, -high

lines = sys.stdin.readlines()
for i, l in enumerate(lines[1:]):
    n, k = map(int, l.strip().split(' '))
    lo, hi = solve(n,k)
    print "Case #%d: %d %d" % (i+1, hi, lo)
*/
