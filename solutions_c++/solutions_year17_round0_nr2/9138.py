#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include <bits/stdc++.h>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

typedef long long ll;

using namespace std;

int ar[20];

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t,sv;
    scanf("%d",&t);
    sv=t;
    long long int n,val,tmp;
    int ind,i,p1,p2,p;
    while(t--)
    {
        scanf("%lld",&n);
        tmp=n;
        ind=0;
        while(tmp!=0)
        {
            ar[ind]=tmp%10;
            tmp/=10;
            ind++;
        }
        p=0;
        val=0;
        while(p<ind){
            tmp=pow(10,p);
            val+=(ar[ind-1]*tmp);
            p++;
        }
        if(n<val){
            ar[ind-1]--;
            for(i=0;i<ind-1;i++){
               ar[i]=9;
            }
        }
        else{
          p1=ind-1;
          p2=ind-2;
          while(p2>=0){
              if(ar[p1]<=ar[p2]){
                  p1--;
                  p2--;
              }
              else
               break;
          }
          if(p1!=0){
            ar[p1]--;
            for(i=p2;i>=0;i--)
             ar[i]=9;
          }
        }
        tmp=0;
        for(i=ind-1;i>=0;i--){
          tmp=tmp*10+ar[i];
        }
        printf("Case #%d: %lld\n",sv-t,tmp);
    }

    return 0;
}
