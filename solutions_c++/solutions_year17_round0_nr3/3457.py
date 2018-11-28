#include <bits/stdc++.h>
using namespace std;
const int N = 1e6+5;
int a[N],T,k,n;
struct node{
    int l,r;
    bool operator<(node x)const {
        if(r-l<x.r-x.l)return true;
        if(r-l>x.r-x.l)return false;
        return l>x.l;
    }
    node(int y,int z){
        l=y;
        r=z;
    }
};
priority_queue<node>q;
int main(){
    //freopen("C-small-2-attempt0.in","r",stdin);
    //freopen("C-small-2-out.txt","w",stdout);
    //freopen("out.txt","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++){
        while(!q.empty())q.pop();
        cin>>n>>k;
        q.push(node(0,n+1));
        memset(a,0,sizeof a);
        a[0]=a[n+1]=1;
        int mx=0,mi=N;
        while(k--){
            node tmp=q.top();
            q.pop();
            int ll=tmp.l;int rr=tmp.r;
            int mid=(ll+rr)/2;
            if(rr-ll<=1){
                k++;
                continue;
            }
            q.push(node(mid,rr));
            q.push(node(ll,mid));
            //cout<<ll<<" "<<mid<<" "<<rr<<endl;
            mx=max(mid-ll-1,rr-mid-1);
            mi=min(mid-ll-1,rr-mid-1);
            a[mid]=1;
        }
        cerr<<ca<<endl;
        printf("Case #%d: %d %d\n",ca,mx,mi);
    }
}
