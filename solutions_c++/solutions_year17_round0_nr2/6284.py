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

bool tidy()
{
  FOR(i, 0, s.size() - 1)
  {
    if (s[i] > s[i+1]) return false;
  }


  return true;
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

    while (!tidy())
    {
      FOR (i, 0, s.size() - 1)
      {
        if (s[i] > s[i+1])
        {
          s[i]--;
          FOR(j, i+1, s.size()) s[j] = '9';
        }
      }
    }

    const char *q = s.c_str();
    if (s.size() > 1) while(*q == '0') q++;

    printf("Case #%lld: %s\n", T + 1, q);
  }
}
