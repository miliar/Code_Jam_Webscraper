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

typedef pair<int,int> PI;
const int dr[] = {-1,0,1,0};
const int dc[] = {0,1,0,-1};
typedef long long LL;

int G[104];
int dp[101][101][3];

int f3( int r, int r1, int r2 ) {
  if( r1 == 0 && r2 == 0 ) return 0;
  
  int& res = dp[r1][r2][r];
  if( res != -1 ) return res;
  res = 0;
  
  int add = 0;  
  if( r == 0 ) ++add;
  
  // r1:
  if( r1 > 0 ) {
    res = max( res, add + f3( (r+1)%3, r1-1, r2 ) );
  }
  // r2:
  if( r2 > 0 ) {
    res = max( res, add + f3( (r+2)%3, r1, r2-1 ) );
  }
  
  return res;
}

int dp4[101][101][101][4];
int f4( int r, int r1, int r2, int r3 ) {
  if( r1 == 0 && r2 == 0 && r3 == 0 ) return 0;
  
  int& res = dp4[r1][r2][r3][r];
  if( res != -1 ) return res;
  res = 0;
  
  int add = 0;  
  if( r == 0 ) ++add;
  
  // r1:
  if( r1 > 0 ) {
    res = max( res, add + f4( (r+1)%4, r1-1, r2, r3 ) );
  }
  // r2:
  if( r2 > 0 ) {
    res = max( res, add + f4( (r+2)%4, r1, r2-1, r3 ) );
  }
  // r3:
  if( r3 > 0 ) {
    res = max( res, add + f4( (r+3)%4, r1, r2, r3-1 ) );
  }
  
  return res;
}


int main() { 
	int cases;
	
	cin >> cases;
	for( int caseid = 1; caseid <= cases; ++caseid ) {
		cout << "Case #" << caseid << ": ";
		int N, P;
		cin >> N >> P;
		for( int i = 0; i < N; ++i ) {
		  cin >> G[i];
		}
		
		if( N == 1 ) {
		  cout << 1 << endl;
		  continue;
		}
		
		if( P == 2 ) {
		  int res = 0;
		  int odd = 0;
		  for( int i = 0; i < N; ++i ) {
		    if( G[i]%2 == 0 ) ++res;
		    else ++odd;
		  }
		  
		  res += (odd+1)/2;
		  cout << res << endl;
		  continue;
		} else if( P == 3 ) {
		  int res = 0;
		  int r1 = 0;
		  int r2 = 0;
      for( int i = 0; i < N; ++i ) {
        if( G[i]%3 == 0 ) ++res;
        else if( G[i]%3 == 1 ) ++r1;
        else ++r2;
      }
      memset( dp, -1, sizeof(dp) );
      cout << res + f3( 0, r1, r2 ) << endl;
		} else {
		  assert( P == 4 );
      int res = 0;
      int r1 = 0;
      int r2 = 0;
      int r3 = 0;
      for( int i = 0; i < N; ++i ) {
        if( G[i]%4 == 0 ) ++res;
        else if( G[i]%4 == 1 ) ++r1;
        else if( G[i]%4 == 2 ) ++r2;
        else ++r3;
      }
      memset( dp4, -1, sizeof(dp4) );
      cout << res + f4( 0, r1, r2, r3 ) << endl;
		}
	}
	return 0;	
}
