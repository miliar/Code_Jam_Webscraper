#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>
#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <limits>
#include <fstream>
#include <list>
#include <sstream>
#include <iostream>
#include <iomanip>
//#include <time.h>
using namespace std;
#define MAX 55
int a[ MAX ], w[ MAX ][ MAX];
int n,p;

bool possible(vector<int> &current, int k){
	for( int i = 0 ; i < current.size() ; ++i ){
		double val = a[i] * k;
		double p1 = (current[i] * 100.0);///val;
		if( p1 < 90 * val || p1 > 110 * val ) return false;
	}
	return true;
}

bool seen[ MAX ][ MAX ];
int bruteForce(){
	vector<int> v(p, 0);
	for( int i = 0 ; i < p ; ++i ) v[i] = i;
	int result = 0;
	do{
		vector<int> current;
		int cnt = 0;
		for( int i = 0 ; i < p ; ++i ){
			current.clear();
			current.push_back(w[0][i]);
			if( n > 1 )
				current.push_back(w[1][v[i]]);

			int low = 1<<30, up = 0;
			for( int i = 0 ; i < current.size() ; ++i ){
				low = min( current[i]/a[i], low);
				up = max( up, (int)ceil(current[i]/(double)(a[i])));
			}
		
			for( int i = low - 1 ; i <= up + 1 ; ++i ){
				if( possible(current, i ) ){
					cnt++; break;
				}
			}
			
		}		
		result = max( result, cnt );
	}while( next_permutation(v.begin(), v.end()) );
	return result;
}

int main() {
    int t ;
    scanf("%d", &t) ;
    for( int q = 1 ; q <= t && scanf("%d %d" , &n, &p ) ; ++q ){
        for( int i = 0 ; i < n && scanf("%d" , &a[i]) ; ++i );
		for( int i = 0 ; i < n ; ++i ){
			for( int j = 0 ; j < p && scanf("%d" , &w[i][j]) ; ++j );
		}
		//vector<int> current;
		//memset(seen , 0 ,sizeof(seen) );
		printf("Case #%d: %d\n", q, bruteForce() );
    }
    return 0 ;
}
