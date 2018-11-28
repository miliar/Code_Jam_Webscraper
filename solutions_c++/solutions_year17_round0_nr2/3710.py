#include<iostream>
#include<cstdio>
using namespace std;
typedef long long ll;

const int N=20;
int a[N];

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;scanf("%d",&T);
    int ca=0;
    while(T--) {
        printf("Case #%d: ",++ca);
        ll n;cin>>n;
        int len=0;
        while(n) {
            a[len++]=n%10;
            n/=10;
        }
        int p=0;//p之后的都是9
        for(int i=1;i<len;++i) {
            if(a[i]>a[i-1]) {
                --a[i];
                p=i;
            }
        }
        while(a[len-1]==0) --len;
        for(int i=len-1;i>=p;--i) printf("%d",a[i]);
        for(int i=p-1;i>=0;--i) printf("%d",9);
        puts("");
    }
    return 0;
}
