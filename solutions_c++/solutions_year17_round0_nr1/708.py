#include<bits/stdc++.h>
using namespace std;

const int N = 1e3 + 10;

int T, n, k, ans;
char s[N];
bool f[N];

int solve(){
	n = strlen(s);
    for(int i=0; i<n; i++){
        if(s[i] == '+'){
			f[i] = 1;
        } else {
			f[i] = 0;
        }
    }
    int ret = 0;
    for(int i=0; i+k<=n; i++){
        if(!f[i]){
            for(int j=0; j<k; j++){
				f[i+j] ^= 1;
            }
            ret++;
        }
    }
    for(int i=0; i<n; i++){
		if(!f[i]){
			return -1;
		}
    }
    return ret;
}

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
        scanf("%s %d", s, &k);
        ans = solve();
        if(ans == -1){
			printf("Case #%d: IMPOSSIBLE\n", t);
        } else {
			printf("Case #%d: %d\n", t, ans);
        }
	}
	return 0;
}
