#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/hash_policy.hpp>
#define f first
#define s second
//#pragma comment(linker,"/STACK:102400000,102400000")
using namespace std;
using namespace __gnu_pbds;
typedef pair<int,int> par;
int s[1005],k[1005];
int main(){
    int t,T=0;
    scanf("%d",&t);
    while(t--){T++;
        int d,n;
        scanf("%d%d",&d,&n);
        for(int i=0;i<n;i++)
            scanf("%d%d",&k[i],&s[i]);
        long double mit=0,one=1,tmp;
        for(int i=0;i<n;i++){
            tmp=(one*(d-k[i]))/s[i];
            mit=max(tmp,mit);
            }
        printf("Case #%d: %.07f\n",T,(double)(d/mit));
        }
    return 0;
    }
