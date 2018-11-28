#include <bits/stdc++.h>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 2000000000000000000LL
#define INF 1000000000
#define EPS 1e-7
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

string impossible = "IMPOSSIBLE";
pair<int, char> arr[3];

string solve_small(int x, int y, int z)
{
  int n = x + y + z;
  assert(n > 1);
  arr[0] = mp(x, 'R');
  arr[1] = mp(y, 'Y');
  arr[2] = mp(z, 'B');
  sort(arr, arr + 3, greater<pair<int, char> >());
  if(arr[0].f > n / 2) return impossible;
  string ans = "";
  for(int i=0;i<n;i++) ans += "#";
  int tmp = arr[1].f + arr[2].f - arr[0].f + 1;
  if(tmp / 2 > arr[2].f) return impossible;
  for(int i=0;i<arr[0].f;i++) ans[i*2] = arr[0].s;
  for(int i=1;i<=tmp;i++)
  {
    if(i & 1) ans[n - i] = arr[1].s, arr[1].f--;
    else ans[n - i] = arr[2].s, arr[2].f--;
  }
  for(int j=1;j<=2;j++)
    for(int i=0;i<n && arr[j].f > 0;i++)
    {
      if(ans[i] != '#') continue;
      arr[j].f--;
      ans[i] = arr[j].s;
    }
  assert(arr[1].f == 0);
  assert(arr[2].f == 0);
  return ans;
}

string solve_large(int x, int y, int z, int xy, int xz, int yz, int n)
{
  if(xy + z == n)
  {
    if(xy != z) return impossible;
    string result = "";
    while(xy--) result += "BO";
    return result;
  }
  if(xz + y == n)
  {
    if(xz != y) return impossible;
    string result = "";
    while(xz--) result += "YV";
    return result;
  }
  if(yz + x == n)
  {
    if(yz != x) return impossible;
    string result = "";
    while(yz--) result += "RG";
    return result;
  }
  if(xy && z < xy + 1) return impossible;
  if(xz && y < xz + 1) return impossible;
  if(yz && x < yz + 1) return impossible;
  if(xy) z -= xy;
  if(xz) y -= xz;
  if(yz) x -= yz;
  string answer = solve_small(x, y, z), result = "";
  if(answer == impossible) return impossible;
  for(int i=0;i<answer.size();i++)
  {
    if(answer[i] == 'R')
    {
      if(yz > 0)
      {
        while(yz--) result += "RG";
        result += "R";
      }
      else result += answer[i];
    }
    else if(answer[i] == 'Y')
    {
      if(xz > 0)
      {
        while(xz--) result += "YV";
        result += "Y";
      }
      else result += answer[i];
    }
    else if(answer[i] == 'B')
    {
      if(xy > 0)
      {
        while(xy--) result += "BO";
        result += "B";
      }
      else result += answer[i];
    }
    else assert(false);
  }
  return result;
}

int main()
{
  freopen("B-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    int n, x, y, z, xy, xz, yz;
    cerr << tt << "\n";
    scanf("%d %d %d %d %d %d %d", &n, &x, &xy, &y, &yz, &z, &xz);
    printf("Case #%d: %s\n", tt++, solve_large(x, y, z, xy, xz, yz, n).c_str());
  }
  return 0;
}
