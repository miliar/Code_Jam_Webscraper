#include<bits/stdc++.h>
using namespace std;

int T;
int N;
struct state {
  int n,k;
  state(){}
  state(int n,int k):n(n),k(k){}
  bool isng(int c){
    if( c == -1 ) return false;
    if( (c+1)%6 == k ||
        (c+5)%6 == k ||
        c == k ) return true;
    return false;
  }
  bool operator<( const state& a ) const {
    return n < a.n;
  }
};

string ch="ROYGBV";

bool solve(){
  priority_queue<state> q;
  for(int i=0;i<6;i++){
    int a; cin >> a;
    q.emplace( a,i );
  }

  int c = -1;
  vector<char> res;
  for(int i=0;i<N;i++){
    vector<state> tmp;
    state p;
    while( !q.empty() ) {
      p = q.top(); q.pop();
      if( !p.isng( c ) ) break;
      tmp.emplace_back( p );
    }
    //cout << c <<" "<< p.n<< " "<< p.k << endl;
    if( p.isng(c) ) return false;
    if( p.n == 0 ) return false;

    p.n--;
    for( auto t : tmp ) q.emplace( t );
    q.emplace( p );

    res.emplace_back( ch[p.k] );
    c = p.k;
  }
  reverse( res.begin(), res.end() );
  if( res[0] == res.back() ) {
    swap( res[0], res[1] );
    if( res[0] == res.back()||
        res[0] == res[1] ||
        res[1] == res[2] ) return false;
  }
  for( char c : res )
    cout << c;
  cout << endl;
}

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  cin >> T;
  for(int ttt=1;ttt<=T;ttt++){

    cin >> N;

    cout << "Case #" << ttt << ": ";
    if( !solve() ) cout << "IMPOSSIBLE" << endl;


  }
}
