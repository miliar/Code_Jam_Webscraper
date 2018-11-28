/* Eat a live frog first thing in the morning,
   and nothing worse will happen to you the rest of the day */

/* You can't connect the dots looking forward 
   you can only connect them looking backwards. */

/* Nothing is impossible; impossible itself says "I'm possible" */

#include<bits/stdc++.h>
#define ll long long
#define ld long double
#define ull unsigned long long
#define boost ios_base::sync_with_stdio(false);cin.tie(0);cout.precision(10);cout << fixed;
#define dbset(x) for(int i=0 ; i<x.size(); i++) cerr << x[i] << " "; cerr << endl;
#define inf 1000000007
#define INF 1000000000000000000LL
#define PI 3.14159265358979323846
#define mod 1000000007
#define mod1 1000696969
#define flusz fflush(stdout);
#define VI vector<int>
#define VPI vector < pair<int,int> >
#define PII pair<int, int>
#define BIT bitset<N>
#define st first
#define nd second
#define pb push_back
#define mp make_pair
#define eb emplace_back
#define endl '\n'
#define REP(x, y) for(int x = 0; x < (y); ++x)
#define FOR(x, y, z) for(int x = y; x <= (z); ++x)
#define FORR(x, y, z) for(int x = y; x >= (z); --x)
using namespace std;

template<class TH> void _dbg(const char *sdbg, TH h){cerr<<sdbg<<"="<<h<<"\n";}
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while(*sdbg!=',')cerr<<*sdbg++;cerr<<"="<<h<<","; _dbg(sdbg+1, a...);
}
#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)

#define N 5000
#define int long long

int test;

int n;
string res;

char t[]={'R', 'O', 'Y', 'G', 'B', 'V'};

int il[N];

struct cmp{
       bool operator()(PII a,PII b)
       {
              if (a.st>=b.st)
                     return true;  
              else
                     return false;
       }
};

set <PII,cmp> s;

void solve()
{
       cin >> n;

       s.clear();
       res.clear();

       FOR(i,0,5)
       {
              cin >> il[i];

              if (il[i]!=0)
              {
                     s.insert(mp(il[i],i));
              }
       }

       if ((*s.begin()).st*2>n)
       {
              cout << "IMPOSSIBLE" << endl;
              return;
       }

       if (s.size()==2)
       {
              auto it=s.begin();

              auto it1=*it;

              it++;

              auto it2=*it;

              FOR(i,1,n/2)
              {
                     res+=t[it1.nd];
                     res+=t[it2.nd];
              }
       }
       else
       {
              auto it=s.begin();

              auto it1=*it;

              it++;

              auto it2=*it;

              it++;

              auto it3=*it;

              int last=0;

              while(it1.st)
              {
                     if (it2.st>it3.st)
                     {
                          res+=t[it1.nd];
                          res+=t[it2.nd];

                          it1.st--;
                          it2.st--;  

                          last=2;
                     }
                     else
                     {
                           res+=t[it1.nd];
                           res+=t[it3.nd];

                           it1.st--;
                           it3.st--; 

                           last=3;
                     }
              }

              if (last==2)
              {
                     while(it3.st)
                     {
                            res+=t[it3.nd];

                            if (it2.st)
                                   res+=t[it2.nd];

                            it3.st--;
                            it2.st--;
                     }
              }
              else
              {
                     while(it2.st)
                     {
                            res+=t[it2.nd];

                            if (it3.st)
                                   res+=t[it3.nd];

                            it3.st--;
                            it2.st--;
                     }
              }
       }

       cout << res << endl;

       return;
}

int32_t main()
{
    boost

    cin >> test;

    FOR(i,1,test)
    {
         cout << "Case #" << i <<": ";
         solve();
    }

  return 0;
}
