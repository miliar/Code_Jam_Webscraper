#include<bits/stdc++.h>
using namespace std;

typedef long long LL;

int T;
LL n, k, x, y;
map<LL, LL> MP;
map<LL, LL>::reverse_iterator it;

void solve(){
	LL a, b;
	MP.clear();
	MP[n] = 1;
    while(true){
        it = MP.rbegin();
        a = it->first;
        b = it->second;
        MP.erase(a);
        x = a / 2;
        y = a - x - 1;
        if(x){
			MP[x] += b;
        }
        if(y){
			MP[y] += b;
        }
        if(b >= k){
			break;
        } else {
			k -= b;
        }
    }
}

int main(){
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
    scanf("%d", &T);
    for(int t=1; t<=T; t++){
		scanf("%I64d %I64d", &n, &k);
		solve();
		printf("Case #%d: %I64d %I64d\n", t, x, y);
    }
	return 0;
}
