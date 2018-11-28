#include <cstdio>
#include <cstring>
#include <numeric>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

char s[1111];
int T,k;

void solve(int cases) {
    int ans = 0;
    scanf("%s%d",s,&k);
    int len = strlen(s);
    for(int i = 0 ; s[i] ; i++ ) if( i+k <= len) {
        if(s[i] == '-') {
            ans++;
            for(int j = i; j < i+k ; j++ ) {
                s[j] = (s[j]=='-')?'+':'-';
            }
        }
    }
    bool hasAns = true;
    for(int i = 0; s[i] ; i++ ) {
        if(s[i] == '-') hasAns = false;
    }
    printf("Case #%d: ",cases);
    if(hasAns) {
        printf("%d\n",ans);
    } else {
        printf("IMPOSSIBLE\n");
    }
}

int main() {
    scanf("%d",&T);
    for(int i = 1 ; i <= T ; i++ ) solve(i);
    return 0;
}
