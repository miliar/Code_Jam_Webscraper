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

int main(int argc, const char * argv[]) {
  freopen("/Users/efimovmichael/Downloads/c.txt","r",stdin);
  freopen("/Users/efimovmichael/c.out","w",stdout);

  int t;
  cin >> t;
  for (int tc = 1; tc <= t; ++tc) {
    long long n, k;
    cin >> n >> k;
    k -= 1;
    long long c = 0;
    long long p2 = 1;
    while (true) {
      long long next = c + p2;
      if (k < next) {
        long long m = (n-c) / p2;
        long long r = (n-c) % p2;
        k -= c;
        long long val = m;
        if (k < r) {
          val += 1;
        }
        long long min = (val - 1) / 2;
        long long max = min + ((val - 1) % 2);
        cout << "Case #" << tc << ": " << max << " " << min << endl;
        break;
      }
      c = next;
      p2 *= 2;
    }
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
