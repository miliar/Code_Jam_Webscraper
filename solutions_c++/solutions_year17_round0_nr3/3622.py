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

const int INF=0x3f3f3f3f;
const int MAXN=1000+10;
#define ll long long

int n,k;

struct line{
    int l;
    int r;
    bool operator <(const line &s) const{
        if((r-l)==(s.r-s.l)) return l<s.l;
        else return (r-l)<(s.r-s.l);
    }
};

priority_queue <line> q;

void solve(){
    int minn=0,maxx=0;
    while(k--){
        line tmp=q.top();
        q.pop();
        int mid=(tmp.l+tmp.r)>>1;
        minn=min(tmp.r-mid-1,mid-tmp.l-1);
        maxx=max(tmp.r-mid-1,mid-tmp.l-1);
        if(mid>tmp.l+1) q.push(line{tmp.l,mid});
        if(mid+1<tmp.r) q.push(line{mid,tmp.r});
    }
    printf("%d %d\n",maxx,minn);
}


int main(){
    //freopen("in.txt","r",stdin);
    int T;
    scanf("%d",&T);
    int time=0;
    while(T--){
        while(!q.empty()) q.pop();
        scanf("%d%d",&n,&k);
        q.push(line{1,n+2});
        printf("Case #%d: ",++time);
        solve();
    }
    return 0;
}

