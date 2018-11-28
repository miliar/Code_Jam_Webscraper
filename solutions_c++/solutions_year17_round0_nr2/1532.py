#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <math.h>
#include <fstream>
#include <thread>
#include <assert.h>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <array>
#include <sstream>
#include <set>
#include <map>
#include <list>
#include <time.h>
#include <iomanip>
#include <forward_list>

using namespace std;

long long find(long long n, int max) {
  if (n < 10) {
    if ((int) n <= max) {
      return n;
    } else {
      return 0;
    }
  }

  long long res = 0;
  int dig = n % 10;
  long long other = n / 10;
  if (dig <= max) {
    res = find(other, dig) * 10 + dig;
  }
  res = std::max(res, find(other-1, 9) * 10 + 9);
  return res;
}

int main(int argc, const char * argv[]) {
  freopen("/Users/efimovmichael/Downloads/b.txt","r",stdin);
  freopen("/Users/efimovmichael/b.out","w",stdout);

  int t;
  cin >> t;
  for (int tc = 1; tc <= t; ++tc) {
    long long n;
    cin >> n;
    cout << "Case " << tc << ": " << find(n, 9) << endl;
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
