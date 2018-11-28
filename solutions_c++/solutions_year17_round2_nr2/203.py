#include <bits/stdc++.h>

using namespace std;

int n,r,o,y,g,b,v;
bool b1,r1,y1;
void printred(){
    r--;
    printf("R");
    if(r1){
        r1=false;
        for(int i=0;i<g;i++){
            printf("GR");
        }
    }
}
void printyellow(){
    y--;
    printf("Y");
    if(y1){
        y1=false;
        for(int i=0;i<v;i++){
            printf("VY");
        }
    }
}
void printblue(){
    b--;
    printf("B");
    if(b1){
        b1=false;
        for(int i=0;i<o;i++){
            printf("OB");
        }
    }
}

int main(){
    freopen("hi.txt","r",stdin);
    freopen("hi2.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
        if(r==0 && o==b && y==0 && g==0 && v==0){
            printf("Case #%d: ",t);
            for(int i=0;i<o;i++){
                printf("OB");
            }
            printf("\n");
            continue;
        }
        if(r==g && o==0 && y==0 && b==0 && v==0){
            printf("Case #%d: ",t);
            for(int i=0;i<r;i++){
                printf("RG");
            }
            printf("\n");
            continue;
        }
        if(r==0 && o==0 && y==v && g==0 && b==0){
            printf("Case #%d: ",t);
            for(int i=0;i<y;i++){
                printf("YV");
            }
            printf("\n");
            continue;
        }
        if(o>0){
            if(b<=o){
                printf("Case #%d: IMPOSSIBLE\n",t);
                continue;
            }
            b-=o;
        }
        if(g>0){
            if(r<=g){
                printf("Case #%d: IMPOSSIBLE\n",t);
                continue;
            }
            r-=g;
        }
        if(v>0){
            if(y<=v){
                printf("Case #%d: IMPOSSIBLE\n",t);
                continue;
            }
            y-=v;
        }
        if(2*max(b,max(r,y))>b+r+y){
            printf("Case #%d: IMPOSSIBLE\n",t);
            continue;
        }
        b1=true,r1=true,y1=true;
        printf("Case #%d: ",t);
        if(b>=r && b>=y){
            while(b>1){
                printblue();
                if(r>y){
                    printred();
                }
                else{
                    printyellow();
                }
            }
            printblue();
            while(r>0 || y>0){
                if(r>y){
                    printred();
                    if(y>0)printyellow();
                }
                else{
                    printyellow();
                    if(r>0)printred();
                }
            }
            printf("\n");
        }
        else if(r>=y){
            while(r>1){
                printred();
                if(b>y){
                    printblue();
                }
                else{
                    printyellow();
                }
            }
            printred();
            while(b>0 || y>0){
                if(b>y){
                    printblue();
                    if(y>0)printyellow();
                }
                else{
                    printyellow();
                    if(b>0)printblue();
                }
            }
            printf("\n");
        }
        else{
            while(y>1){
                printyellow();
                if(b>r){
                    printblue();
                }
                else{
                    printred();
                }
            }
            printyellow();
            while(r>0 || b>0){
                if(r>b){
                    printred();
                    if(b>0)printblue();
                }
                else{
                    printblue();
                    if(r>0)printred();
                }
            }
            printf("\n");
        }
    }

    return 0;
}
