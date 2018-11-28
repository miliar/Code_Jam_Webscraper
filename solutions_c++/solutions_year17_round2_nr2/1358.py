#include<bits/stdc++.h>
using namespace std;
char col[1009];
int main()
{
    freopen("B-small-attempt3.in","r",stdin);
    freopen("a.out","w",stdout);
    int t,cs=1,n,r,y,b,o,g,v,i,pr;
    scanf("%d",&t);
    while(t--){
        scanf("%d %d %d %d %d %d %d",&n,&r,&o,&y,&g,&b,&v);
        //printf("%d %d %d %d\n",n,r,b,y);
        if(r>n/2 || b>n/2 || y>n/2){
            printf("Case #%d: IMPOSSIBLE\n",cs++);
            continue;
        }
        pr=-1;
        for(i=0;i<n;i++){
            if((r>=b || pr==1) && (r>=y || pr==2) && pr!=0){
                col[i]='R';
                r--;
                pr=0;
            }
            else if((b>=y || pr==2) && pr!=1){
                col[i]='B';
                b--;
                pr=1;
            }
            else{
                col[i]='Y';
                y--;
                pr=2;
            }
        }
        if(col[i-1]==col[0]){
            swap(col[i-1],col[i-2]);
            i--;
            while(i>0 && col[i]==col[i-1]){
                swap(col[i],col[i-1]);
                i--;
            }
        }
        col[n]='\0';
        printf("Case #%d: %s\n",cs++,col);
    }
    return 0;
}
