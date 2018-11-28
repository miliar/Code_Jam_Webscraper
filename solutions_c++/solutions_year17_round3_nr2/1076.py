/*************************************************************************
	> File Name: B.cpp
	> Author: tyxxzjpdez
	> Mail: tyxxzjpdez@163.com
	> Created Time: 2017年04月30日 星期日 17时54分23秒
 ************************************************************************/

#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

struct Node{
    int l,r,id;
    bool operator<(const Node& rhs)const{
        if(l!=rhs.l)return l<rhs.l;
        return r<rhs.r;
    }
};

const int maxn=100+10;
int Ac,Aj;
Node arr[maxn];

set<Node> S;

int main(){
    //ios::sync_with_stdio(false);
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++){
        scanf("%d%d",&Ac,&Aj);
        for(int i=0;i<Ac+Aj;i++){
            scanf("%d%d",&arr[i].l,&arr[i].r);
            if(i<Ac)arr[i].id=0;
            else arr[i].id=1;
            S.insert(arr[i]);
        }
        sort(arr,arr+Ac+Aj);
        if(Ac<2 && Aj<2)printf("Case #%d: 2\n",kase);
        else{
            int ans;
            int tot=Ac+Aj;
            int t=arr[1].r-arr[0].l;
            int tt=arr[1].l-arr[0].r;
            t=min(t,1440-tt);
            if(t<=720)
                ans=2;
            else ans=4;
            printf("Case #%d: %d\n",kase,ans);
        }
    }
    return 0;
}
