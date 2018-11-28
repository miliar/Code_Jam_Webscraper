#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;

typedef long long LL;
#define pb push_back

int main () {
	int T;
	scanf("%d", &T);
	for(int tt = 1; tt <= T; ++tt){
		int n, k;
		cin >> n >> k;
		priority_queue<int>q;
		q.push(n);
		for(int i = 0; i < k; ++i){
			int x = q.top();
			q.pop();
			int a, b;
			if(x&1){
				a = b = x>>1;
			}
			else{
				b = x>>1;
				a = b-1;
			}
			if(i == k-1){
				printf("Case #%d:", tt);
				printf(" %d %d\n", b, a);
			}
			q.push(a); q.push(b);
		}
	}
}