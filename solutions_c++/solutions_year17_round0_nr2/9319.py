//Find me in >>>>>>>>>>>>>>>>>>>>>>>>>>  Tom CLANCY's Rainbow Six Siege  <<<<<<<<<<<<<<<<<<<<<<< _-_ (O_O)
//My handle >>>>>>>>>>>>>>>>>>>>> DXIANDROID <<<<<<<<<<<<<<<<<<<<<<<<<<
//<<<<<<<< regards >>>>>>>>>>>
//<<<<<<<<<<<< Vinay Goel >>>>>>>>>>>>>>>>
//$$$$$$$$$$$ NITJ $$$$$$$$$$$$$$$$$$


#include<bits/stdc++.h>
using namespace std;

#define int long long
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
#define dbg(x) cout << " " << #x << " = " << x < " "
#define ol cout << endl

int compute( vector<int> &y, int pos ){
      int p = pos;
      while( p > 0 && y[p] == y[p-1] ) p--;
      y[p]--;
      for( int i = p+1; i < y.size(); i++ ) y[i] = 9;

      int ret = 0;
      for( int i = y.size()-1, ten = 1; i >= 0; i--, ten *= 10 ) ret += y[i]*ten;
      return ret;
}

int solve(){
      int N;
      scanf( "%lld", &N );

      vector<int> x(0), y(0);
      for( int i = N; i > 0; i /= 10 ) x.pb( i%10 );

      y.resize(x.size());
      for( int i = 0; i < x.size(); i++ ) y[x.size()-1-i] = x[i];

      int pos = 0;
      while( pos < y.size()-1 && y[pos] <= y[pos+1] ) pos++;

      if( pos == y.size()-1 ) return N;
      return compute(y,pos);
}
signed main(){
      freopen( "input.in", "r", stdin );
      freopen( "output.txt", "w", stdout );
      int T;
      scanf( "%lld", &T );
      for( int i = 1; i <= T; i++ ) printf( "Case #%lld: %lld\n", i, solve() );
      return 0;
}
