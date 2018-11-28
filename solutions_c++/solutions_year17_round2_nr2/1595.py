// Lupus Nocawy
// 2017-04-22
// Google Code Jam
// Round 1B 2017
// https://code.google.com/codejam
// https://code.google.com/codejam/contest/8294486/dashboard
// Problem B

#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <cmath>
using namespace std;
#define REP(i,n) for(int i=0, _n=n; i<_n; ++i)
#define FOR(i,a,b) for(int i=(a), _b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a), _b=(b); i>=_b; --i)
#define IT(i,x) __typeof__(x) i=x
#define FOREACH(it,x) for(__typeof__((x).begin()) it=(x).begin(); it!=(x).end(); ++it)
#define ALL(x) x.begin(),x.end()
#define MP make_pair
#define PB push_back
#define DEBUG(x) if(debug) cout << x << endl;
typedef long long int lli;
typedef unsigned long long int llu;
typedef pair<int,int> pii;
const int debug=0;

const int INF = 2147483647;
const int max_n = 2147483647;

void solve(int c){
	int n,r,o,y,g,b,v;
	scanf("%d %d %d %d %d %d %d ", &n, &r, &o, &y, &g, &b, &v);
	// small: r y b
	// printf("%d %d %d\n", r, y, b);

	if(r>y+b || y>r+b || b>r+y){
		printf("IMPOSSIBLE\n");
		return;
	}

	char last = 0;
	char first = 0;
	if(r>=y && r>=b){
		printf("R");
		r--;
		last = 'r';
		first = 'r';
	}
	else if(y>=b && y>=r){
		printf("Y");
		y--;
		last = 'y';
		first = 'y';
	}
	else if(b>=r && b>=y){
		printf("B");
		b--;
		last = 'b';
		first = 'b';
	}
	// printf("\n");

	while(r+y+b > 0){
		// printf("%d %d %d\n", r, y, b);
		if(last == 'r'){
			if(y==b){
				if(first=='y'){
					printf("Y");
					y--;
					last = 'y';
				}
				else{
					printf("B");
					b--;
					last = 'b';
				}
			}
			else if(y>=b){
				printf("Y");
				y--;
				last = 'y';
			}
			else{
				printf("B");
				b--;
				last = 'b';
			}
		}

		else if(last == 'y'){
			if(r==b){
				if(first=='r'){
					printf("R");
					r--;
					last = 'r';
				}
				else{
					printf("B");
					b--;
					last = 'b';
				}
			}
			else if(r>=b){
				printf("R");
				r--;
				last = 'r';
			}
			else{
				printf("B");
				b--;
				last = 'b';
			}
		}

		else if(last == 'b'){
			if(r==y){
				if(first=='r'){
					printf("R");
					r--;
					last = 'r';
				}
				else{
					printf("Y");
					y--;
					last = 'y';
				}
			}
			else if(r>=y){
				printf("R");
				r--;
				last = 'r';
			}
			else{
				printf("Y");
				y--;
				last = 'y';
			}
		}

	}
	printf("\n");
	return;
}

int main(void){
	int t;
	scanf("%d ", &t);
	for(int c=1; c<=t; ++c){
		printf("Case #%d: ", c);
		solve(c);
	}
	return 0;
}
