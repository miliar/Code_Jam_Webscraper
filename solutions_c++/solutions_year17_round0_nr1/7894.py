#include <bits/stdc++.h>

#define ll long long
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define Nn 100005
#define M 1000005
//#define mod 1e9+7

using namespace std;

typedef pair<int,int> ii;
typedef pair<ll,ll> lii;
typedef vector<int> vi;
typedef vector<ii> vii;
const double pi = acos(-1);
const int inf = 2e9;

char s[1005];
vi v;
int p = 1;

int solve(vector<int> bits, int N)
{
  queue<int> flips;
  int moves = 0;

  for (int i = 0; i < bits.size(); ++i)
  {
    if (!flips.empty() && flips.front() <= i - N)
      flips.pop();

    if ((bits[i] ^ (flips.size() % 2 == 0)) == 1)
    {
      if (i > bits.size() - N)
        return -1; // IMPOSSIBLE

      moves++;
      flips.push(i);
    } 
  }

  return moves;
}

int main() {

      #ifndef ONLINE_JUDGE
            freopen("in.in", "r", stdin);
            freopen("out.in", "w", stdout);
      #endif
            
           int t, q , k;
      scanf("%d", &t);
      for(q = 0; q < t; q ++)
      {
            v.clear();
            scanf("%s" , s);
            scanf("%d" , &k);
            int l = strlen(s);
            for(int i = 0; i < l; ++i) {
                  if(s[i] == '+')
                        v.pb(1);
                  else
                        v.pb(0);
            }
            if(solve(v , k) == -1)
                  printf("Case #%d: IMPOSSIBLE\n" , p++);
            else
                  printf("Case #%d: %d\n" , p++ , solve(v , k));
          
      }
}