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

map <int,int> m;

int n,k;

struct cmp{
       bool operator() (int a,int b)
       {
              return a>b;
       }
};


set <int,cmp> s;

void solve()
{
       cin >> n >> k;

       s.clear();
       m.clear();

       m[n]=1;
       s.insert(n);

       while(!s.empty())
       {
              auto it=s.begin();
              s.erase(it);

              auto it1=*it;

              k-=m[it1];

              if (k<=0)
              {
                     if (it1==0)
                            cout << 0 << " " << 0 << endl;
                     else if (it1%2==1)
                            cout << it1/2 << " " << it1/2 << endl;
                     else
                            cout << it1/2 << " " << it1/2-1 << endl; 
                     return;
              }

              if (it1%2==1)
              {
                     m[it1/2]+=2*m[it1];
                     s.insert(it1/2);
              }
              else   
              {
                     m[it1/2]+=m[it1];
                     m[it1/2-1]+=m[it1];

                     s.insert(it1/2);
                     s.insert(it1/2-1);
              }
       }

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
