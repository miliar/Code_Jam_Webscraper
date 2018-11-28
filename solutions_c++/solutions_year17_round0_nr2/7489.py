#include <bits/stdc++.h>
using namespace std;
char a[21];
long long N;

long long f(long long x, long long ret, long long lim, long long st){
    if(x == N) return ret;
    long long i, r;
    if(lim > st) return -1;
    for(i = st; i >= lim; i--){
        if(st == a[x]-'0' && i == st) r = f(x+1, ret*10+i, i, a[x+1]-'0');
        else r = f(x+1, ret*10+i, i, 9);
        if(r != -1) break;
    }
    return r;
}
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.out", "w", stdout);
    long long i, T;
    cin>>T;
    for(long long t = 1; t <= T; t++){
        scanf("%s", a);
        N = strlen(a);
        printf("Case #%lld: %lld\n", t, f(0, 0, 0, a[0]-'0'));
    }
}
