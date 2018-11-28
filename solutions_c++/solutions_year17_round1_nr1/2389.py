#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<map>
#include<queue>
#include<cstring>
#include<stack>
#include<set>
#include<vector>
#include<iostream>
#include<fstream>
#include<math.h>
#include<cmath>
#define mp(x,y) make_pair(x,y)
#define INF 1e18
#define EPS 1e-5
using namespace std;
int const sz=1e6+2;
char inp[30][30],tmp[30][30];
int main(){
int t;
freopen("A-large.in","r",stdin);
freopen("out.in","w",stdout);

scanf("%d",&t);
int cnt=1;
while(t--){
    int r,c;
    scanf("%d %d",&r,&c);
    for(int i=0;i<r;i++){
        scanf("%s",inp[i]);
 strcpy(tmp[i],inp[i]);

        }
    for(int i=0;i<r;i++){
        bool flag=false;
        for(int j=0;j<c;j++){
            if(inp[i][j]!='?')
                flag=1;
            if(flag){
                for(int k=j-1;k>-1;k--){
                    if(inp[i][k]=='?')
                    inp[i][k]=inp[i][j];
                    else
                        break;
                }
                for(int k=j+1;k<c;k++){
                 if(inp[i][k]=='?')
                    inp[i][k]=inp[i][j];
                else{
                    j=k-1;
                    break;
                }
                }

            }
            }
        }
        for(int i=0;i<c;i++){
        bool flag=false;
        for(int j=0;j<r;j++){
            if(inp[j][i]!='?')
                flag=1;
            if(flag){
                for(int k=j-1;k>-1;k--){
                    if(inp[k][i]=='?')
                    inp[k][i]=inp[j][i];
                    else
                        break;
                }
                for(int k=j+1;k<r;k++){
                 if(inp[k][i]=='?')
                    inp[k][i]=inp[j][i];
                else{
                    j=k-1;
                    break;
                }
                }

            }
            }
        }
  /*  if(cnt==32){
       // fclose(stdout);
       printf("\n this is input");
        for(int i=0;i<r;i++)
            printf("%s\n",tmp[i]);
    }*/
    printf("Case #%d:\n",cnt++);

    for(int i=0;i<r;i++)
        printf("%s\n",inp[i]);
   /* if(cnt==33)
        break;*/
    }


return 0;
}
/*
1
4 5
z??x?
?A???
???B?
?????
*/
