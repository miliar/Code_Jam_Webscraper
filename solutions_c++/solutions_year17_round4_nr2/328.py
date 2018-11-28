#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
#include <cassert>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <unordered_map>
#include <queue>
#include <vector>

using namespace std;

typedef long long LL;

struct ticket {
  int pos;
  int cust;
  
  bool operator<( const ticket& other ) const {
    return pos < other.pos;
  }
};

ticket tickets[1000];
int cust_ticket_cnt[1004];
int N, C, M;
int ffree[1004];

int main() { 
  int cases;
  
  cin >> cases;
  for( int caseid = 1; caseid <= cases; ++caseid ) {
    cout << "Case #" << caseid << ": ";
    cin >> N >> C >> M;
    
    memset( cust_ticket_cnt, 0, sizeof(cust_ticket_cnt) );
    
    for( int i = 0; i < M; ++i ) {
      cin >> tickets[i].pos >> tickets[i].cust;
      ++cust_ticket_cnt[tickets[i].cust];
    }
    
    sort( tickets, tickets+M );
    
    int max_cust_ticket_cnt = 0;
    for( int i = 1; i <= C; ++i ) {
      max_cust_ticket_cnt = max( max_cust_ticket_cnt, cust_ticket_cnt[i] );
    }
    
    int u = max_cust_ticket_cnt;
    int v = M;
    while( u <= v ) {
      int w = (u+v)/2;
      
      bool ok = true;
      for( int i = 0; i < M; ++i ) {
        int placed_customers = i+1;
        if( placed_customers > w*tickets[i].pos ) {
          ok = false;
          break;
        }
      }
      if( ok ) {
        v = w-1;
      } else {
        u = w+1;
      }
    }
    int rides = u;
    
    /////
    for( int i = 1; i <= N; ++i ) {
      ffree[i] = rides;
    }
    
    int promotions = 0;
    for( int i = 0; i < M; ++i ) {
      auto& t = tickets[i];
      if( ffree[t.pos] == 0 ) {
        ++promotions;
      } else {
        --ffree[t.pos];
      }
    }
    
    cout << rides << ' ' << promotions << endl;
  }
  return 0; 
}
