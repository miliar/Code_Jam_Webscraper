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
#define MAX 1005
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
vector<pii> v;
int n;
const double pi=acos(-1.0);

double area(double radius){
	return pi * radius * radius;
}

double circum(double height, double radius){
	return 2.0 * pi * radius * height;
}

double areaExposed( int last, int current ){
	pii down = v[last];
	pii up = v[current];
	return circum(down.second, down.first ) + area( down.first ) - area( up.first);
}

double dp[MAX][MAX];

double solve( int last, int k ){
	if( k == 0 ){
		return area(v[last].first) + circum(v[last].second, v[last].first);
	}
	if( dp[last][k] != -1 ) return dp[last][k];
	double result = 0.0;
	for( int i = last + 1 ; i < n ; ++i ){
		result = max( result, areaExposed(last, i) + solve( i , k - 1 ) );
	}
	return dp[last][k] = result;
}

int main() {
    int t, k;
    scanf("%d", &t) ;
    for( int q = 1 ; q <= t ; ++q ){
		scanf("%d %d" , &n , &k );
		v = vector<pii>(n , mp(0,0));
		for( int i = 0 ; i < n && scanf("%d %d" , &v[i].first, &v[i].second) ; ++i );
		sort( v.rbegin(), v.rend() );
		for( int i = 0 ; i <= n ; ++i ){
			for( int j = 0 ; j <= k ; ++j )
				dp[i][j] = -1;
		}	
		double result = 0;
		for( int i = 0 ; i < n ; ++i ){
			result = max( result, solve(i , k - 1) );
		}
        printf("Case #%d: %.9lf\n", q, result );
    }
    return 0 ;
}
