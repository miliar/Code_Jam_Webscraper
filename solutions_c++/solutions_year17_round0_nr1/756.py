#include <bits/stdc++.h>
using namespace std;

const int N = 1100;
int k, t, cas = 1;
char s[N];

void solve(){
    int len =strlen(s), ans = 0;
    for(int i=0;i<len-k+1;i++){
        if(s[i] == '-'){
            for(int j=0;j<k;j++){
                s[i+j] = (s[i+j] == '-' ? '+' : '-');
            }
            ans++;
        }
    }

    for(int i=len-k+1; i < len;i++){
        if(s[i] == '-') {
            puts("IMPOSSIBLE");
            return;
        }
    }
    printf("%d\n", ans);
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    while(t--){
        scanf("%s %d", s, &k);
        printf("Case #%d: ", cas++);
        solve();
    }
	return 0;
}
