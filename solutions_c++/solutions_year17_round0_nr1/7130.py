#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>

#define io_r freopen("input.txt","r",stdin);
#define io_w freopen("output.txt","w",stdout);
#define io_file io_r; io_w;

#define PB push_back
#define MP make_pair
#define ll long long

#define rep(i,n) for (int i = 0; i<n; ++i)
#define clr(x, y) memset(x, y, sizeof x)
#define all(x) (x).begin(), (x).end()

#define MAX 1010
#define MOD 1000000007

using namespace std;

int k, sz;
char s[MAX];

void calc(int pos){
	rep(i, k){
		if (s[i+pos] == '-')
			s[i+pos] = '+';
		else
			s[i+pos] = '-';
	}
}

int main (){
	int Case = 1;
	int t;
	scanf("%d", &t);
	
	while(t--){
		printf("Case #%d: ", Case++);
		scanf("%s %d", s, &k);
		int ans = 0;
		sz = strlen(s);
		
		for(int i = 0; i<sz-k; i++){
			if(s[i] == '-'){
				calc(i);
				ans++;
			}
		}
		
		int aux = 0;
		bool valid = true;
		
		for(int i = sz-k; i<sz; i++) if(s[i] == '-') aux++;
		
		if(aux) {
			if(aux%k == 0) ans++;
			else valid = false;
		}
		
		if(valid) printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	}
	
	return 0;
}
