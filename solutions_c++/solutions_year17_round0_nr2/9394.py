#include<bits/stdc++.h>
using namespace std;
#define MAXN 2222
#define LL long long
int t,n;


LL a[MAXN];
LL val;

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d ",&t);
    for(int ca=1;ca<=t;ca++){
        scanf("%lld",&val);
        n = 0;
        LL tmp = val;
        bool fnd = 1;
        while(tmp){

            if(tmp%10 < (tmp/10)%10)fnd = 0;

            a[n] = tmp%10;
            tmp/=10;
            n ++;
        }
        if(fnd){
            printf("Case #%d: %lld\n",ca,val);
            continue;
        }
        reverse(a,a+n);

        LL ans = 1;
        for(int i = 0 ; i < n;i++){
            if(i){
                if(a[i]<=a[i-1])break;
            }
            LL cur = 0;
            for(int j = 0 ; j < i;j++){
                cur *=10;
                cur +=a[j];
            }
            cur*=10;
            cur +=(a[i]-1);

           // cout<<"cur:"<<cur<<endl;
            while(cur<=val){

                ans = max(ans,cur);
                cur *=10;
                cur +=9;
            }
        }
        printf("Case #%d: %lld\n",ca,ans);
    }
    return 0;
}
