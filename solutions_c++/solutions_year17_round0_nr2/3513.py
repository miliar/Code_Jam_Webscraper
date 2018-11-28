#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <algorithm>

using namespace std;

const int MAXN=1000+10;
#define ll long long

ll n;
vector <int > p;

ll solve(ll x){
    p.clear();
    while(x){
        p.push_back(x%10);
        x/=10;
    }
    int len=p.size();
    for(int i=len-1;i>0;i--){
        if(p[i-1]<p[i]){
            for(int j=i-1;j>=0;j--){
                p[j]=9;
            }
            if(p[i]) p[i]-=1;
            else{
                p[i]=9;
                p[i+1]-=1;
            }
        }
    }
    bool flag=false;
    for(int i=len-1;i>0;i--){
        if(p[i-1]<p[i]){
            flag=true;
            break;
        }
    }
    ll tmp=0;
    for(int i=0;i<len;i++){
        tmp+=p[i]*(ll)pow(10.0,i);
    }
    if(flag){
        return solve(tmp);
    }else return tmp;
}



int main(){
    //freopen("in.txt","r",stdin);
    int T;
    scanf("%d",&T);
    int time=0;
    while(T--){
        scanf("%lld",&n);
        printf("Case #%d: %lld\n",++time,solve(n));
    }
    return 0;
}

