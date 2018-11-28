#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
int main(){
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++){
        int     n,r,o,y,g,b,v;
        scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
        //small dataset
        printf("Case #%d: ",cas);
        if(2*r>n||2*y>n||2*b>n){printf("IMPOSSIBLE\n");continue;}
        char last=(y<b)?((y<r)?'y':'r'):((b<r)?'b':'r');
        char first=0;
        while(r+y+b>0){
                 if(last=='r'){if(y>b || y==b && first=='y'){if(!first)first='y';printf("Y");y--;last='y';}else{printf("B");b--;last='b';if(!first)first='b';}}
            else if(last=='y'){if(r>b || r==b && first=='r'){if(!first)first='r';printf("R");r--;last='r';}else{printf("B");b--;last='b';if(!first)first='b';}}
            else if(last=='b'){if(y>r || y==r && first=='y'){if(!first)first='y';printf("Y");y--;last='y';}else{printf("R");r--;last='r';if(!first)first='r';
                }}
        }
        printf("\n");



    }
    return 0;
}
