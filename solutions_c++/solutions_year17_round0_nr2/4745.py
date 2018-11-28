#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include<map>
#include<unordered_map>
#include<iostream>
#include<string>
#define ll long long
#define fi first
#define se second
using namespace std;
int main(void){
    freopen("B-large.in","r",stdin);
    //freopen("B-large.out", "w", stdout);
    int T;
    scanf("%i", &T);
    for(int l=0;l<T;l++){
        ll N;
        scanf("%lld", &N);
        ll a[20];
        int i;
        ll m[19];
        m[0]=1;
        for(i=1;i<=18;i++){
            m[i]=10*m[i-1];
            a[i]=0;
        }
        a[19]=0;
        for(i=0;i<20;i++){
            a[i]=N%10;
            N/=10;
            if(N==0) break;
        }
        ll res=0;
        for(;i>0;i--){
            if(a[i-1]<a[i]){
                int j=i;
                while(a[j+1]==a[j]) j++;
                a[j]--;
                j--;
                for(;j>=0;j--) a[j]=9;
            }
        }
        for(i=0;i<18;i++){
            res+=m[i]*a[i];
        }
        printf("Case #%i: %lld\n", l+1, res);
    }
    return 0;
}

