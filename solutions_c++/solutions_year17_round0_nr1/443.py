#include <cstdio>
#include <cstring>

int F[1009];

int L;

int query(int x){
    int ans = 0;
    for (int i = x; i > 0; i -= i&-i){
        ans += F[i];
    }
    return ans;
}

void update(int l, int r){
    for (int i = l; i <= L; i += i&-i){
        F[i]++;
    }
    for (int i = r+1; i <= L; i += i&-i){
        F[i]++;
    }
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("Aoutputlarge.o","w",stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++){
        char S[1009];
        int K;
        scanf(" %s %d", S, &K);
        int ans = 0;
        L = strlen(S);
        for (int i = 0; i < L; i++){
            if (S[i]=='-'){
                update(i+1,i+1);
            }
        }
        for (int i = 1; i <= L-K+1; i++){
            if (query(i)%2==1){
                update(i,i+K-1);
                ans++;
            }
        }
        for (int i = L-K+2; i <= L; i++){
            if (query(i)%2==1){
                ans = -1;
                break;
            }
        }
        if (ans==-1){
            printf("Case #%d: IMPOSSIBLE\n",t);
        }
        else {
            printf("Case #%d: %d\n",t,ans);
        }
        for (int i = 1; i <= L; i++){
            F[i] = 0;
        }
    }
}
