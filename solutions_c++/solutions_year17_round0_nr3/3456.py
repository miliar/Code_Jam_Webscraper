#include <vector>
#include <bitset>
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
pair<uint64_t, uint64_t> solve( const uint64_t n, const uint64_t k );
int main(int argc, char* argv[]) {
  int T;
  cin >> T;
  vector<int> N(T);
  vector<int> K(T);
  forall(t, 0, T) { cin >> N[t] >> K[t]; }
  forall(t, 0, T) {
    cout << "Case #" << t + 1 << ": ";
    auto rst = solve(N[t], K[t]);
    cout << rst.first << ' ' << rst.second << '\n';
  }

  return 0;
}
pair<uint64_t, uint64_t> solve(const uint64_t n, const uint64_t k) {
  int q = static_cast<int>(log2(n+1));
  int p = static_cast<int>(log2(k));
  debug("==============================");
  debug("n,k=",n,k);
  debug("q,p = ",q,p);
  if( n+1 == 1ull<<q ){
    uint64_t r = n/2/(1ull<<p);
    return mp( r,r );
  }
  uint64_t w = k - (1ull<<p);
  uint64_t m = n;
  debug("w = ",w );
  bitset<32> W(w);
  debug(W);
  uint64_t l = 1;
  uint64_t r = 0;
  uint64_t m1 = n;
  uint64_t m2 = 0;
  for( int i = 0; i < p; ++i ){
  //  int8_t b = w >>( p-i-1 ) & 1;
    
    debug(m1,'x', l,'\t', m2, 'x', r );
    if( m2 == 0 ){
      m1 --;
      if( m1%2 == 0 ){
        l *= 2;
        m1 /= 2;
      }else{
        r = l;
        m1 /= 2;
        m2 = m1;
        m1 += 1;
      }
    }else{
      m1 --;
      m2 --;
      if( m1%2 == 0 ){
        l *= 2;
        l += r;
        // r = r;
        m1 /= 2;
        m2 /= 2;
      }else{
        // l = l;
        r *= 2;
        r += l;
        debug("m1 = ",m1);
        m1 /= 2;
        m1 += 1;
        debug("m1 = ",m1);
        m2 /= 2;
      }
    }
  }
  debug( "at the end=",m1,'x', l,'\t', m2, 'x', r );
  m = w < l ? m1 : m2;
  m--;
  return mp( max( m/2, m/2+m%2 ), min( m/2, m/2+m%2 ) );
}

