#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <cmath>
#include <vector>
#include <stack>
#include <bitset>

using namespace std;

const int INF = 2 * (int)1e9;
typedef int64_t ll;

#define cout out
#define cin in


int main()
{
    ifstream in("/home/vlad/Downloads/A-large.in");
    ofstream out("/home/vlad/output.txt");
    int ntest;
      cin >> ntest;  // read t. cin knows that t is an int, so it reads it as such.
      for (int test = 1; test <= ntest; ++test) {
        int d, n;
        cin >> d >> n;  // read n and then m.
        double res = 0;
        int k, s;
        for(int i = 0; i < n; ++i){
            cin >> k >> s;
            res = max(res, (double)(d - k) / s);
        }
        res = d / res;
        cout.precision(6);
        cout << "Case #" << test << ": " << fixed << res << endl;
      }

      return 0;

}




