#include <iostream>
#include <stdio.h>
#include <cstring>
#include <algorithm>
#include <math.h>
using namespace std;
int a[10];
char c[1005],s[10]={'R','O','Y','G','B','V'};
struct node{
    char cc;
    int num;
}no[10];
bool cmp(node x,node y){
    if(x.num>y.num)return true;
    return false;
}
int main()
{
    freopen("E://project/code-jam/2017/round1b/B-small-attempt2.in","r",stdin);
    freopen("E://project/code-jam/2017/round1b/b-small3.txt","w",stdout);
    int t,k=0,n;
    cin>>t;
    while(t--){
        scanf("%d",&n);
        bool b=true;
        for(int i=0;i<6;i++)no[i].cc=s[i];
        for(int i=0;i<6;i++)scanf("%d",&no[i].num);
      //  printf("%d ",n);
       // for(int i=0;i<6;i++)printf("%d ",no[i].num);
       // printf("\n");
        for(int i=0;i<6;i++)if(no[i].num>n/2){b=false;break;}
        sort(no,no+6,cmp);
       // for(int i=0;i<6;i++)printf("%d ",no[i].num);
        //printf("\n");
        int loc=0,tot=0;
        for(int i=0;i<6;i++){
            for(int j=0;j<no[i].num;j++){
                c[loc]=no[i].cc;
                tot++;
                loc+=2;
                if(loc>=n&&tot<n)loc=1;
            }
        }
        printf("Case #%d: ",++k);
        if(b){
            for(int i=0;i<n;i++)printf("%c",c[i]);
            printf("\n");
           // for(int i=0;i<n-1;i++)if(c[i]==c[i+1]){printf("\n\n%d!!!!!!!!!!!!!!!!!!!!!\n\n",i);break;};
        }
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
