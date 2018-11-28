#include <iostream>
#include <stdio.h>
#include <cstring>
#include <math.h>
#include <algorithm>
using namespace std;
struct node{
    int start,endd;
    char name;
}nc[1000],nj[1000],nt[1000];
bool cmp(node a,node b){
    return a.start<b.start;
}
int main()
{
    freopen("E://project/code-jam/2017/round1c/B-small-attempt1.in","r",stdin);
    freopen("E://project/code-jam/2017/round1c/b-small.txt","w",stdout);
    int t,k=0,c,J,tot;
    cin>>t;
    while(t--){
        scanf("%d%d",&c,&J);
        tot=0;
        for(int i=0;i<c;i++){scanf("%d%d",&nc[i].start,&nc[i].endd);nc[i].name='c';nt[tot++]=nc[i];}
        for(int i=0;i<J;i++){scanf("%d%d",&nj[i].start,&nj[i].endd);nj[i].name='j';nt[tot++]=nj[i];}
        sort(nt,nt+tot,cmp);
        sort(nc,nc+c,cmp);
        sort(nj,nj+J,cmp);
        //for(int i=0;i<c;i++)cout<<nc[i].start<<endl;
        //for(int i=0;i<J;i++)cout<<nj[i].start<<endl;
        int ans=2;
        if(J==0&&c==2){
            if(nc[1].endd-nc[0].start<=720);
            else if(nc[0].endd-nc[1].start+1440<=720);
            else ans=4;
        }
        if(c==0&&J==2){
            if(nj[1].endd-nj[0].start<=720);
            else if(nj[0].endd-nj[1].start+1440<=720);
            else ans=4;
        }
        printf("Case #%d: %d\n",++k,ans);
    }
    return 0;
}
