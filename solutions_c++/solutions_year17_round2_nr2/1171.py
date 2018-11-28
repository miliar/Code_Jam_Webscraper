#include<bits/stdc++.h>
#define pb push_back
#define F first
#define S second
#define ll long long int
#define inf 1450000090
#define fastio ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define sd(x) scanf("%d",&x)
#define sd2(x,y) scanf("%d%d",&x,&y)
#define sdl(x) scanf("%lld",&x)
#define nax 100010
#define mp make_pair
#define sz(x) (int)(x.size())
#define pi pair <int , char>
#define pii pair < int , pair <int ,int > >
#define MOD 1000000007
using namespace std;
set < pi >  sett;
set < pi >  :: iterator it;
char ans[1010];
int main(int argc, char const *argv[])
{
  freopen("input.txt","read",stdin);
  freopen("output.txt","write",stdout);
  int t;
  sd(t);
  for(int tt=1;tt<=t;tt++)
  {
     printf("Case #%d: ",tt);
     memset(ans,'\0',sizeof ans);
     sett.clear();
     int n,r,o,y,g,b,v;
     sd(n);
     sd2(r,o);
     sd2(y,g);
     sd2(b,v);
     char ch = '?';
     if(r!=0)
     sett.insert(mp(r,'R'));
     if(b!=0)
     sett.insert(mp(b,'B'));
     if(y!=0)
     sett.insert(mp(y,'Y'));
     int mi = 1;
     int ptr =0;
     while(!sett.empty())
     {
      if(mi == 1)
      {
        pi beg = *sett.begin();
        char cc = beg.S;
        if(beg.S == ch)
        {
            if(sz(sett) == 1)
              break;
            it = sett.begin();
            it++;
            beg = *it;
        }
        ans[ptr++] = beg.S;
        sett.erase(beg);
        if(beg.F-1 > 0)
        sett.insert(mp(beg.F-1,beg.S));
        ch = beg.S;
        mi = 0;
      }
      else
      {
        it = sett.end();
        it--;
        char cc = it->S;
        if(cc == ch)
        {
          if(sz(sett) == 1)
              break;
            it--;
        }
        ans[ptr++] = it->S;
        pi ins = *it;
        sett.erase(it);
        if(ins.F-1 > 0)
          sett.insert(mp(ins.F-1,ins.S));
        ch = ins.S;
        mi = 1;
      }
     }
     ans[ptr] = '\0';
     if(sz(sett) == 0)
      puts(ans);
    else
      puts("IMPOSSIBLE");
  }
  return 0;
}