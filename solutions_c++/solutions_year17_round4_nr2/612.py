#include <bits/stdc++.h>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 2000000000000000000LL
#define INF 1000000000
#define EPS 1e-8
#define LL long long
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define setzero(a) memset(a,0,sizeof(a))
#define setdp(a) memset(a,-1,sizeof(a))
#define bits(a) __builtin_popcount(a)

using namespace std;

pair<int, int> tickets[1005];
int cnt1[1005];
int cnt2[1005];
int n, c, mini, m;

bool check(int rides)
{
  mini = 0;
  for(int i=0;i<m;i++)
  {
    cnt1[tickets[i].f]++;
    cnt2[tickets[i].s]++;
  }
  for(int i=1;i<=n;i++) mini += max(0, cnt1[i] - rides);
  for(int i=n-1;i>0;i--)
  {
    if(cnt1[i] >= rides)
      cnt1[i - 1] += cnt1[i] - rides;
  }
  if(cnt1[0]) return false;
  for(int i=1;i<=c;i++)
    if(cnt2[i] > rides)
      return false;
  return true;
}

int main()
{
  freopen("B-small-attempt3.in", "r", stdin);
  freopen("output2.txt", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    int x, y;
    scanf("%d %d %d", &n, &c, &m);
    for(int i=0;i<m;i++)
    {
      scanf("%d %d", &x, &y);
      tickets[i] = mp(x, y);
    }
    sort(tickets, tickets + m);
    int L = 1, R = m;
    while(R > L)
    {
      int mid = L + (R - L) / 2;
      setzero(cnt1);
      setzero(cnt2);
      if(check(mid))
        R = mid;
      else L = mid + 1;
    }
    setzero(cnt1);
    setzero(cnt2);
    assert(check(R));
    printf("Case #%d: %d %d\n", tt++, R, mini);
    cerr << tt << " done\n";
  }
  return 0;
}
