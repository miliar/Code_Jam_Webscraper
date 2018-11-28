#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
using namespace std;
typedef long long ll;
typedef double R;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

const R PI = acos(-1);
const int MAXN = 1<<20;
const int P = 1e9+7;

char s[MAXN];
ll pow10(int k){
	ll ret = 1;
	for(int i = 0; i < k; i++)
		ret *= 10;
	return ret;
}

int main(){
#ifdef LOCAL
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif
	int T, i0;
	scanf("%d", &T);
	for(i0 = 1; i0 <= T; i0++){
		scanf("%s", s);
		int n;
		int i, j;
		ll v;
		n = strlen(s);
		sscanf(s, "%lld", &v);
		for(i = 0; i < n-1; i++)
			if(s[i] > s[i+1])
				break;
		if(i < n-1){
			while(i-1 >= 0 && s[i-1] == s[i])
				i--;
			if(s[i] == '1'){
				n--;
				fill(s, s+n, '9');
				s[n] = 0;
			}
			else{
				s[i]--;
				fill(s+i+1, s+n, '9');
			}
		}
		printf("Case #%d: %s\n", i0, s);
	}
	return 0;
}
