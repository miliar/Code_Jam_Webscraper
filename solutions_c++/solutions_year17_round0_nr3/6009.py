// =============================================================================
// Author LUONG VAN DO
// Problem 
// Algorithm
// Time Limit
// =============================================================================
#include <iostream>
#include <stdio.h>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <math.h>
#include <cstring>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

#define rep(i, n) for (int i=0;i<n;i++)
#define repr(i, n) for (int i = n - 1;i>=0;i--)
#define fr(i, a, b) for (int i=a;i<=b;i++)
#define frr(i, a, b) for (int i=b;i>=a;i--)
#define FileIn(file) freopen(file".inp", "r", stdin)
#define FileOut(file) freopen(file".out", "w", stdout)
#define fill(ar, val) memset(ar, val, sizeof(ar))
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define PI 3.1415926535897932385
#define uint64 unsigned long long
#define int64 long long
#define INF 1000000009
#define N 1000005
#define C 2
#define md 1000000007
using namespace std;

inline long long max(long long a, long long b) { return a > b ? a : b; }
inline int min(int a, int b) { return a < b ? a : b; }
inline int gcd(int a, int b) { if (a % b) return gcd(b, a % b); else return b; }
inline int lcm(int a, int b) { return (a * (b / gcd(a, b) )); }

inline int And(int mask, int bit) { return mask & (1 << bit); }
inline int Or(int mask, int bit) { return mask | (1 << bit); }
inline int Xor(int mask, int bit) { return mask ^ (1 << bit); }

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
int heap[N], nheap;
int n, k;
void updateHeap(int val) {
	heap[++nheap] = val;
	int par = (nheap >> 1);
	int child = nheap;
	while (par > 0 && heap[par] < heap[child]) {
		swap(heap[par], heap[child]);
		child = par;
		par = (child >> 1);
	}
}
void downHeap() {
	swap(heap[1], heap[nheap--]);
	int r = 1;
	int v = heap[r];
	while (2 * r <= nheap) {
		int c = 2 * r;
		if (c < nheap && heap[c] < heap[c + 1]) c++;
		if (v >= heap[c]) break;
		swap(heap[r], heap[c]);
		r = c;
	}
}
int main() {
	#ifndef ONLINE_JUDGE
        freopen("exam.inp","r", stdin);
        freopen("exam.out","w", stdout);
    #endif
    int cases;
    scanf("%d",&cases);
    rep(it, cases) {
    	scanf("%d %d", &n, &k);
    	nheap = 0; updateHeap(n);
    	int leftVal, rightVal;
    	rep(i, k) {
    		int val = heap[1];
    		if (val % 2) {
    			leftVal = (val >> 1);
    			rightVal = (val >> 1);
    		}
    		else {
    			rightVal = (val >> 1);
    			leftVal = rightVal - 1;
    		}
    		if (nheap > 0) downHeap();
    		updateHeap(leftVal);
    		updateHeap(rightVal);
    	}
    	printf("Case #%d: %d %d\n", it + 1, max(leftVal, rightVal), min(leftVal, rightVal));
    }
}