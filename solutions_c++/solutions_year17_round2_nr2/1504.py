#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
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
int N, R, O, Y, G, B, V;
vector<int> v(6,0);
//map<int, int> cnt;
vector<char> c = {'R', 'O', 'Y', 'G', 'B', 'V'};
vector<vector<int>> graph(6);

string solve1( void ){
  // small
  string rst = "";
  auto itr = max_element( all(v) );
  int idx = itr-v.begin();
  debug( "idx = ", idx, v[idx]);
  debug(idx);
  v[idx] --;
  rst += c[idx];
  const int init_idx = idx;
  int idx2;
  for( int i = 0; i < N-1; ++i ){
   //bool flag = false;
    print_(v);
    debug("idx=", idx);
    if( idx != init_idx && v[init_idx]!= 0 ){
      idx2 = init_idx;
    }else{
      idx2 = *max_element( all(graph[idx]), [](const int lhs, const int rhs){
        if ( v[lhs] < v[rhs] ) return true; else return false;
        } );
    }
    debug( "idx2=", idx2, "v[idx2]=", v[idx2] );
    if( v[idx2] != 0 ){
      debug( "idx2=", idx2, "v[idx2]=", v[idx2] );
      rst += c[idx2];
      v[idx2]--;
      idx = idx2;
    }else{
      return "IMPOSSIBLE";
    }
    // for( auto u : graph[idx] ){
    //   debug( "u=", u, "v[uu]=", v[u]);
    //   if( v[u] != 0 ){
    //     idx = u;
    //     flag = true;
    //     break;
    //   }
    // }
    // if( flag == false ){
    //   return "IMPOSSIBLE";
    // }
  }
  debug(rst.back(), rst[0]);
  if( rst.back() == rst[0] ){
    return "IMPOSSIBLE";
  }else{
    return rst;
  }
}

int main( int argc, char * argv[] ){
  graph[0] = {2,3,4};
  graph[1] = {4};
  graph[2] = {0,4,5};
  graph[3] = {0};
  graph[4] = {0,1,2};
  graph[5] = {2};
  int T; cin >> T;
  int t = T;
  while( t-- > 0 ){
    // cin >> N >> R >> O >> Y >> G >> B >> V;
    cin >> N;
    input(v);
    print_(v);
    cout << "Case #" << T-t << ": ";
    cout <<  solve1() << '\n';
  }





  return 0;
}
