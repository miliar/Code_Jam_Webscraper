/*
 */
#include <cassert>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#define tol 1e-11
#define L(k) ((k)&((~(k))+1))
#define N 64
#define Q (1<<N)
#define oo (0xfffffffful)
#define BIT(k) (1ULL<<(k))
#define MASK(k) (BIT(k)-1ULL)
using namespace std;
typedef long long i64;
typedef unsigned long long u64;

char which[1<<20];
int who( u64 u ) {
	if ( u < BIT(20) )
		return which[u];
	if ( u < BIT(40) )
		return 20+which[u>>20];
	if ( u < BIT(60) )
		return 40+which[u>>40];
	return 60+which[u>>60];
}

int n,p,q[N][N],r[N],cur[N];
vector<pair<int,int> > vec[N];

int Ceil( double x ) {
	int a = (int)(x+tol);
	if ( fabs(a-x) < tol )
		return a;
	return a+1;
}

int Floor( double x ) {
	int a = (int)(x+tol);
	return a;
}

int lower( double a, double A ) {
	return Ceil((10*a)/(11*A));
}


int upper( double a, double A ) {
	return Floor((10*a)/(9*A));
}

int good( int x, int y ) {
	return x <= y && y > 0;
}

int intersect( vector<pair<int,int> > &u ) {
	int x,y;
	if ( !u.size() ) return 0;
	x = u[0].first, y = u[0].second;
	for ( int i = 1; i < (int)u.size(); ++i ) {
		if ( u[i].first > y || u[i].second < x ) return 0;
		x = max(x,u[i].first), y = min(y,u[i].second);
	}
	return x <= y;
}

int main() {
	int i,j,k,ts,cs = 0,ans;
	for ( i = 0; i < 20; which[1<<i] = i, ++i ) ;
	for ( scanf("%d",&ts); ts-->0; ) {
		scanf("%d %d",&n,&p);
		for ( i = 0; i < n; ++i )
			scanf("%d",r+i);
		for ( i = 0; i < n; ++i )
			for ( j = 0; j < p; ++j )
				scanf("%d",&q[i][j]);
		for ( i = 0; i < n; cur[i++] = 0 ) {
			vec[i].clear();
			for ( j = 0; j < p; ++j ) {
				int l = lower(q[i][j],r[i]), u = upper(q[i][j],r[i]);
				if ( good(l,u) )
					vec[i].push_back(make_pair(l,u));
			}
			sort(vec[i].begin(),vec[i].end());
		}
		ans = 0;
		for ( bool flag = true; flag; ) {
			vector<pair<int,int> > u;
			u.clear();
			for ( i = 0; i < n; ++i )
				if ( cur[i] == vec[i].size() ) {
					flag = false ;
					break ;
				}
				else u.push_back(vec[i][cur[i]++]);
			if ( !flag ) break ;
			if ( !intersect(u) ) {
				int idx = -1, right = (1<<30);
				for ( i = 0; i < n; ++i ) {
					right = min(right,vec[i][--cur[i]].second);
					if ( right == vec[i][cur[i]].second ) idx = i;
				}
				assert( idx != -1 );
				++cur[idx];
			}
			else ++ans;
		}
		printf("Case #%d: %d\n",++cs,ans);
	}
	return 0;
}

