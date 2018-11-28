#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
int ac,aj;
struct qq{
    int l,r,id;
    bool operator < (const qq &a)const{
        return l<a.l;
    }
}a[209];
priority_queue<int,vector<int>,greater<int> > pr;
int main(){
//    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;++ca){
        scanf("%d%d",&ac,&aj);
        int a1=0,a2=0;
        for(int i=0;i<ac;++i){
            scanf("%d%d",&a[i].l,&a[i].r);
            a[i].id=0;
            a1+=a[i].r-a[i].l;
        }
        for(int i=0;i<aj;++i){
            scanf("%d%d",&a[ac+i].l,&a[ac+i].r);
            a[ac+i].id=1;
            a2+=a[ac+i].r-a[ac+i].l;
        }
        sort(a,a+ac+aj);
        int ans=0;
        while(!pr.empty())pr.pop();
        for(int i=0;i<ac+aj;++i){
            if(a[i].id==0&&a[(i+1)%(ac+aj)].id==0){
                pr.push((a[(i+1)%(ac+aj)].l-a[i].r+24*60)%(24*60));
            }
        }
        int num=ac;
        while(!pr.empty()){
            int u=pr.top();
            pr.pop();
            if(u+a1<=720){
                a1+=u;
                --num;
            }
        }
        ans=num*2;
        for(int i=0;i<ac+aj;++i){
            if(a[i].id==1&&a[(i+1)%(ac+aj)].id==1){
                pr.push((a[(i+1)%(ac+aj)].l-a[i].r+24*60)%(24*60));
            }
        }
        num=aj;
        while(!pr.empty()){
            int u=pr.top();
            pr.pop();
            if(u+a2<=720){
                a2+=u;
                --num;
            }
        }
        ans=max(num*2,ans);
        printf("Case #%d: ",ca);
        printf("%d\n",ans);
    }
    return 0;
}
