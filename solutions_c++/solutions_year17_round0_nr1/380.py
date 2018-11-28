#include<stdio.h>
#include<string.h>

#define N 1010

int n;
char s[N];
int st[4*N];
void build(int i=1, int l=1, int r=n){
    if(l == r){
        st[i] = (s[l] == '-');
        return;
    }
    int m = (l+r)/2;
    build(2*i, l, m);
    build(2*i+1, m+1, r);
    st[i] = 0;
}
#define loli do{\
    st[2*i] += st[i];\
    st[2*i+1] += st[i];\
    st[i]=0;\
}while(0)
void update(const int &ql, const int &qr, int i=1, int l=1, int r=n){
    if(ql<=l && r<=qr){
        st[i]++; return;
    }
    if(qr<l || r<ql){
        return;
    }
    loli;
    int m = (l+r)/2;
    update(ql, qr, 2*i, l, m);
    update(ql, qr, 2*i+1, m+1, r);
}
int find(const int &x, int i=1, int l=1, int r=n){
    if(l == r){
        return st[i];
    }
    loli;
    int m = (l+r)/2;
    return (x<=m)? find(x, 2*i, l, m): find(x, 2*i+1, m+1, r);
}

int main(){
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase++){
        int k;
        scanf("%s%d", s+1, &k);
        n = strlen(s+1);
        int ans = 0;
        build();
        for(int i=1; i<=n-k+1; i++){
            if(find(i)&1){
                update(i, i+k-1);
                ans++;
            }
        }
        for(int i=n-k+2; i<=n; i++){
            if(find(i)&1){
                ans = -1;
                break;
            }
        }
        if(~ans){
            printf("Case #%d: %d\n", kase, ans);
        }else printf("Case #%d: IMPOSSIBLE\n", kase);
    }
    return 0;
}
