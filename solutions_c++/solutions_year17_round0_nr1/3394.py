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
#define print_( a )               for( auto & x : a ) clog << (int)x << ' '; clog << '\n';
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

int solve( const string & str, const int k );

int main( int argc, char * argv[] ){
  int T; cin >> T;
  vector<string> S(T);
  vector<int> K(T);
  forall( t,0,T ){
    cin >> S[t] >> K[t] ;
  }
  forall( t,0,T ){
    cout << "Case #" << t+1 << ": ";
    int rst = solve( S[t], K[t] );
    if( rst >= 0 ){
      cout << rst;
    }else{
      cout << "IMPOSSIBLE";
    }
    cout << '\n';
  }
  return 0;
}

int solve( const string & str, const int k ){
  debug( str, k );
  int cnt = 0;
  int n = str.size();
  vector<int8_t> data( str.size() );
  for( int i = 0; i < n; ++i ){
    data[i] = (str[i] == '+');
  }
  int idx = 0;
  while( idx+k <= n ){
    if( data[idx] == 0 ){
      for( int i = idx; i < idx+k; ++i ){
        data[i] ^= 1;
      }
      cnt ++;
    }
    print_(data);
    debug( cnt );
    ++idx;
  }
  print_(data);
  bool flag = true;
  for( int i = n-1; i >= max(n-k,0); --i ){
    if(data[i] == 0 ){
      flag = false;
      break;
    }
  }
  debug("flag = ", flag );
  return flag ? cnt : -1;
}



