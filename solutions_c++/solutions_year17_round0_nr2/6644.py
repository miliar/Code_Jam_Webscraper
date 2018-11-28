#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
ll pro(ll n) {
    int A[20];
    int acnt=0;
    ll N=n;
    while(N!=0) {
        A[acnt++]=N%10;
        N/=10;
    }
    reverse(A,A+acnt);
    int i;
    for(i=0;i<acnt-1;i++) {
        if(A[i]>A[i+1]) {
            break;
        }
    }
    if(i==acnt-1) {
        return n;
    }
    int re=i;
    int le=0;
    for(int j=re-1;j>=0;j--) {
        if(A[re]!=A[j]) {
            le=j+1;
            break;
        }
    }

    int B[20]={0,};
    for(int i=0;i<le;i++) {
        B[i]=A[i];
    }
    B[le]=A[le]-1;
    for(int i=le+1;i<acnt;i++) {
        B[i]=9;
    }
    ll ret=0;
    for(int i=0;i<acnt;i++) {
        ret*=10;
        ret+=B[i];
    }
    //for(int i=0;i<acnt;i++) printf("%d ",B[i]);
    //printf("\n");
    return ret;
}
int main() {
    int t;
    freopen("input.txt","r",stdin);
    scanf("%d",&t);
    //FILE *f=fopen("output.txt","w");
    for(int i=0;i<t;i++) {
        ll n;
        scanf("%lld",&n);
        printf("Case #%d: ",i+1);
        printf("%lld\n",pro(n));
    }
    return 0;
}
