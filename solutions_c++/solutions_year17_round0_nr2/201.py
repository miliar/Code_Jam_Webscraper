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

char s[50];
int n;
LL DP[20][11][2];

LL solve(int ind, int last, bool l)
{
  if(ind == n) return 1;
  LL &temp = DP[ind][last][l];
  if(temp != -1) return temp;
  temp = 0;
  for(int i=last;i<=9;i++)
  {
    if(!l && s[ind] - '0' < i) break;
    temp += solve(ind + 1, i, l | (s[ind] - '0' > i));
  }
  return temp;
}

int main()
{
  freopen("B-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    scanf("%s", s);
    n = strlen(s);
    LL L = 0, R = 0;
    for(int i=0;i<n;i++) R = R * 10 + s[i] - '0';
    printf("Case #%d: ", tt++);
    setdp(DP);
    LL all = solve(0, 0, 0);
    while(R > L)
    {
      LL mid = L + (R - L) / 2;
      setdp(DP);
      string ss;
      LL tmp = mid;
      while(tmp)
      {
        ss += (char)(tmp % 10) + '0';
        tmp /= 10;
      }
      reverse(ss.begin(), ss.end());
      n = ss.size();
      for(int i=0;i<n;i++)
        s[i] = ss[i];
      LL nxt = solve(0, 0, 0);
      if(nxt < all)
        L = mid + 1;
      else R = mid;
    }
    printf("%I64d\n", R);
  }
  return 0;
}
