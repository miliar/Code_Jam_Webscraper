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
int is_tidy( const string & str ){
  int idx = 0;
  for(  ; idx < str.size()-1; ++ idx ){
    if( str[idx] >  str[idx+1] ){
      return idx;
    }
  }
  idx = str.size();
  return idx;
}


// int solve_brutal( const string & str );
string solve( const string & str);

int main( int argc, char * argv[] ){
  int T; cin >> T;
  vector<string> v(T);
  input(v);
  forall( t,0,T ){
    cout << "Case #" << t+1 << ": ";
  //  cout << solve_brutal( v[t] ) << '\t' << solve( v[t] ) << '\n';
    cout << solve( v[t] ) << '\n';
  }
  return 0;
}

//int solve_brutal( const string & str ){
//  uint64_t x = stoull( str );
//  debug(x);
//  string tmp = str;
//  while( is_tidy(tmp) != tmp.length() ){
//    uint64_t x = stoull( tmp );
//    x --;
//    tmp = to_string(x);
//  }
//  return stoull(tmp);
//}

string solve( const string & str ){
  int idx = is_tidy( str );
  if( is_sorted(str.begin(), str.end() ) ) return str;
  auto itr = lower_bound( str.begin(), str.begin() + idx, str[idx] );
  debug( "lower bnd = ", itr-str.begin(), *itr );
  if( itr == str.begin() && *itr == '1' ){
    string tmp( str.size()-1, '9' );
    return tmp;
  }else{
    auto tmp = str;
    int idx = itr-str.begin();
    tmp[idx] -= 1;
    for( idx++; idx != tmp.size(); ++idx ){
      tmp[idx] = '9';
    }
    return tmp;
  }
  debug( "miss idx = ", idx );
  return 0;
}

  


