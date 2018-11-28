#include<iostream>
#include<string.h>
#include<stdio.h>
#include<set>
using namespace std;

int max(int a,int b){
    if(a>b) return a;
    return b;
}

int min(int a,int b){
    if(a<b) return a;
    return b;
}

int lp_list[1000005];
int rp_list[1000005];

struct node{
    int lp,rp,p;
    node(int pos){
        p=pos;
    }
    int minv(){
        return min(p-lp-1,rp-p-1);
    }
    int maxv(){
        return max(p-lp-1,rp-p-1);
    }
    bool operator<(const node& other)const{
        int mmin = min(p-lp,rp-p);
        int omin = min(other.p-other.lp,other.rp-other.p);
        if(mmin != omin) return mmin > omin;
        int mmax = max(p-lp,rp-p);
        int omax = max(other.p-other.lp,other.rp-other.p);
        if(mmax != omax) return mmax > omax;
        return p < other.p;
    }
    void UpdateLeft(int newp){
        lp = newp;
        lp_list[p]=lp;
    }
    void UpdateRight(int newp){
        rp = newp;
        rp_list[p]=rp;
    }
};

set<node> my_set;

int main(){
    freopen("C-small-2-attempt0.in","r",stdin);
    //freopen("C-small-2-attempt0.out","w",stdout);
    int T,ca=0;
    int i,j,k;
    int n,l;
    scanf("%d",&T);
    while(T--){
        ca++;
        cin>>n>>l;
        my_set.clear();
        for(i=1;i<=n;i++){
            node t(i);
            t.UpdateLeft(0);
            t.UpdateRight(n+1);
            my_set.insert(t);
        }
        for(i=1;i<l;i++){
            node t = *(my_set.begin());
            my_set.erase(t);
            for(j=t.lp+1;j<t.p;j++){
                node a(j);
                a.lp = lp_list[j];
                a.rp = rp_list[j];
                my_set.erase(a);
                a.UpdateRight(t.p);
                my_set.insert(a);
            }
            for(j=t.p+1;j<t.rp;j++){
                node a(j);
                a.lp = lp_list[j];
                a.rp = rp_list[j];
                my_set.erase(a);
                a.UpdateLeft(t.p);
                my_set.insert(a);
            }
            /*printf("i=%d\n",i);
            for(set<node>::iterator iter = my_set.begin();iter!=my_set.end();iter++){
                printf("%d %d %d\n",(*iter).p,(*iter).lp,(*iter).rp);
            }*/
        }
        if(!my_set.empty()){
            node t = *(my_set.begin());
            printf("Case #%d: %d %d\n",ca,t.maxv(),t.minv());
        }
        else{
            printf("Case #%d: %d %d\n",ca,0,0);
        }
    }
    return 0;
}
