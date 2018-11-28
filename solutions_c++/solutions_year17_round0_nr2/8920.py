#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;
typedef long long ll;
#define pb push_back
ll n,ans;
vector<int> a;
int dfs(int now,int e,ll tmp,int pre){
    if (now<0) {
        ans=tmp; return 1 ;
    }
    //cout<<a[now]<<' '<<pre<<' '<<e<<endl;
    if (e){
        dfs(now-1,e,tmp*10+9,9);
        return 1;
    } else {
        if (a[now]>=pre){
            if (dfs(now-1,e,tmp*10+a[now],a[now])) return 1;

        }else  return 0;
        if (a[now]>0) {
            //cout<<a[now]<<endl;
            if (a[now]-1>=pre)
            if (dfs(now-1,1,tmp*10+a[now]-1,a[now]-1)) return 1;
        }
    }
    return 0;
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T; cin>>T;
    for (int tt=1;tt<=T;tt++){
        cin>>n;
        a.clear();
        while (n>0){
            a.pb(n%10);
            n/=10;
        }
        dfs(a.size()-1,0,0,0);
        printf("Case #%d: ",tt);
        cout<<ans<<endl;
    }
}


