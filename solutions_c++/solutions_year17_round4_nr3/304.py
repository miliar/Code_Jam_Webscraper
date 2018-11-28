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

char s[6][55];
int n, m;

bool DP[55][(1 << 5) + 5][(1 << 5) + 5][(1 << 5) + 5];
int v[55][(1 << 5) + 5][(1 << 5) + 5][(1 << 5) + 5], ch[55][(1 << 5) + 5][(1 << 5) + 5][(1 << 5) + 5], idx;
pair<pair<int, int>, int> nxt[55][(1 << 5) + 5][(1 << 5) + 5][(1 << 5) + 5];

int check(const string &tmp, int lasermask, int mask)
{
  bool done[10];
  setzero(done);
  for(int i=0;i<n;i++)
  {
    if(lasermask & (1 << i)) done[i] = true;
    if(tmp[i] != '.') done[i] = true;
    if(tmp[i] == '-')
    {
      if(lasermask & (1 << i)) return -1;
      if(mask & (1 << i)) return -1;
    }
    if(tmp[i] == '|')
    {
      if(lasermask & (1 << i)) return -1;
      for(int j=i-1;j>=0;j--)
      {
        if(tmp[j] == '.') done[j] = true;
        else if(tmp[j] == '-' || tmp[j] == '|') return -1;
        else break;
      }
      for(int j=i+1;j<n;j++)
      {
        if(tmp[j] == '.') done[j] = true;
        else if(tmp[j] == '-' || tmp[j] == '|') return -1;
        else break;
      }
    }
  }
  int temp = 0;
  for(int i=0;i<n;i++)
    if(!done[i])
      temp |= (1 << i);
  return temp;
}

bool solve(int col, int lasermask, int mask, int need)
{
  if(col == m) return need == 0;
  bool &temp = DP[col][lasermask][mask][need];
  if(v[col][lasermask][mask][need] == idx) return temp;
  v[col][lasermask][mask][need] = idx;
  temp = false;
  for(int j=0;j<n;j++)
  {
    if(s[j][col] == '|' || s[j][col] == '-')
    {
      if(lasermask & (1 << j))
        return temp;
    }
  }
  for(int i=0;i<(1 << n);i++)
  {
    string tmp = "";
    for(int j=0;j<n;j++) tmp += s[j][col];
    for(int j=0;j<n;j++)
    {
      if(i & (1 << j))
      {
        if(tmp[j] == '|')
          tmp[j] = '-';
        else if(tmp[j] == '-')
          tmp[j] = '|';
      }
    }
    int rem = check(tmp, lasermask, mask);
    if(rem != -1)
    {
      int newlasermask = lasermask;
      for(int j=0;j<n;j++)
      {
        if(tmp[j] == '#')
        {
          if(newlasermask & (1 << j))
            newlasermask ^= (1 << j);
        }
        if(tmp[j] == '-')
          newlasermask |= (1 << j);
      }
      int newmask = mask;
      for(int j=0;j<n;j++)
      {
        if(tmp[j] == '#')
        {
          if(newmask & (1 << j))
            newmask ^= (1 << j);
        }
        if(tmp[j] == '-' || tmp[j] == '|')
          newmask |= (1 << j);
      }
      int newneed = need;
      for(int j=0;j<n;j++)
      {
        if(newneed & (1 << j))
        {
          if(tmp[j] == '#' || tmp[j] == '|')
          {
            newneed = -1;
            break;
          }
          else if(tmp[j] == '-')
          {
            newneed ^= (1 << j);
          }
        }
      }
      if(newneed != -1) newneed |= rem;
      temp = solve(col + 1, newlasermask, newmask, newneed);
      if(temp)
      {
        ch[col][lasermask][mask][need] = i;
        nxt[col][lasermask][mask][need] = mp(mp(newlasermask, newmask), newneed);
        return true;
      }
    }
  }
  return temp;
}

void get(int col, int lasermask, int mask, int need)
{
  if(col == m) return;
  int i = ch[col][lasermask][mask][need];
  for(int j=0;j<n;j++)
  {
    if(i & (1 << j))
    {
      if(s[j][col] == '|')
        s[j][col] = '-';
      else if(s[j][col] == '-')
        s[j][col] = '|';
    }
  }
  get(col + 1, nxt[col][lasermask][mask][need].f.f, nxt[col][lasermask][mask][need].f.s, nxt[col][lasermask][mask][need].s);
}

int main()
{
  freopen("C-small-attempt1.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    cin >> n >> m;
    for(int i=0;i<n;i++)
      scanf("%s", s[i]);
    printf("Case #%d: ", tt++);
    idx++;
    if(solve(0, 0, 0, 0))
    {
      printf("POSSIBLE\n");
      get(0, 0, 0, 0);
      for(int i=0;i<n;i++)
        printf("%s\n", s[i]);
    }
    else printf("IMPOSSIBLE\n");
  }
  return 0;
}
