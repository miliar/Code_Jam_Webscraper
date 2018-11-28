#include <cstdlib>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <fstream>
#include <sstream>
#include <cmath>
#include <stack>
#include <string.h>
#include <climits>
#include <limits>
//#include <pthread.h>
#include <unistd.h>

#include <math.h>

using namespace std;

typedef vector<int> vi;
typedef vector<pair<int, int> > vpi;

#define ll long long
#define FOR(i, a, b) for(ll i=a; i<b; i++)
#define FORE(i, a, b) for(ll i=a; i<=b; i++)
#define pii pair<int, int>
#define mp make_pair
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define ceil(a, b) ((a)/(b) + ((a)%(b)!=0))
#define square(a) ((a)*(a))
#define PI 3.14159265359
#define INF 1000000000000LL;
#define mod 1000000009LL

string s;

void flip(int j, int k)
{
for (int i = j; i < k + j && i < s.size(); i++)
  s[i] = s[i] == '-' ? '+' : '-';

}

int main(int argc, char *argv[])
{
  freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);

  int t;
  cin >> t;
 
 
  FOR(T, 0, t)
  {
    cin >> s; 
    int k;
    cin >> k;
    int flips = 0;
    FORE(i, 0, s.size() - k)
    {
      if (s[i] == '-')
      {
        flip(i, k);
        flips++;
      }
    }

    bool corr = true;
    FOR(i, 0, s.size()) if (s[i] == '-') corr = false;

    if (corr) printf("Case #%lld: %d\n", T + 1, flips);
    else printf("Case #%lld: IMPOSSIBLE\n", T + 1);

  }
}
