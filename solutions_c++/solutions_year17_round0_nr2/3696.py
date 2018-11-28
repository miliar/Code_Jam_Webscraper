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
#define dbg(x,y) cerr << x << " " << y << endl;
#define db(x) cerr << x << endl;
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

#define N 500007

#define int long long

int test;

int n;

string s,res;

void solve()
{      
       cin >> s;

       int pierw=0;

       res.clear();

       REP(i,s.size())
       {
              pierw*=10;
              pierw+=s[i]-'0';
       }

       REP(i,s.size()-1)
       {
              if (s[i+1]<s[i])
              {
                     int odp=0;

                     while(s[i]-1<res.back() && i>0)
                     {
                            res.pop_back();
                            i--;
                     }

                     REP(j,i)
                     {
                            odp*=10;
                            odp+=res[j]-'0';
                     }

                     odp*=10;
                     odp+=s[i]-'1';

                     while(odp*10+9<=pierw)
                     {
                            odp*=10;
                            odp+=9;
                     }

                     cout << odp << endl;
                     return;
              }
              else
              {
                     res+=s[i];
              }
       }

       res+=s[s.size()-1];

       cout << res << endl;

       return;
}


int32_t main()
{
  boost

  cin >> test;

  FOR(i,1,test)
  {
       cout << "Case #" << i << ": "; 
       solve();
  }

  return 0;
}
