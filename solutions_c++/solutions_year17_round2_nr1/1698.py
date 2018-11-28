#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <unordered_map>
#include <limits>
#include <iostream> 
#include <iomanip>  
#include <string>
#include <sstream>  
#include <algorithm>
#include <functional>
#include <numeric>
#include <cmath>
#include <cassert>

#define input(v)                  for(int i = 0; i < v.size(); ++i){ cin >> v[i]; }

#define INF                         (int)1e9
#define EPS                         1e-9

#define bitcount                    __builtin_popcount
#define gcd                         __gcd

#define forall(i,a,b)               for(int i=a;i<b;i++)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define mp                          make_pair

#define checkbit(n,b)                ( (n >> b) & 1)
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())
typedef unsigned long long int ull_t;
typedef long long int           ll_t;

using namespace std;

#ifdef DEBUG
#define debug(args...)            {dbg,args; clog<<endl;}
#define print_( a )               for( auto & x : a ) clog << x << ' '; clog << '\n';
#define printPair_( a )           for( auto & x : a ) clog << '(' << x.first << ',' << x.second << ')' << ' '; clog << '\n';
#else
#define debug(args...)             // Just strip off all debug tokens
#define print_( a )               // skip
#define printPair_( a )           // skip
#endif
struct debugger
{
  template<typename T> debugger& operator , (const T& x)
  {    
    clog << x << " ";    
    return *this;    
  }
} dbg;

/******* Actual Code Starts Here *********/
int D, N;
double solve( vector<pair<int,int>> & v ){
  vector<double> t(N);
  forall(i,0,N)
    t[i] = static_cast<double>( D-v[i].first ) / static_cast<double>( v[i].second );
  double max_time = *max_element( t.begin(), t.end() );
  debug("max_time=",max_time);
  return static_cast<double>(D)/max_time;
}

int main( int argc, char * argv[] ){
  int T; cin >> T;
  int t = T;
  while( t-- > 0 ){
    cin >> D >> N;
    vector<pair<int,int>> v(N);
    forall(i,0,N)
      cin >> v[i].first >> v[i].second;
    cout << "Case #" << T-t << ": ";
    cout << fixed << setprecision(6) <<  solve(v) << '\n';
  }
  return 0;
}

