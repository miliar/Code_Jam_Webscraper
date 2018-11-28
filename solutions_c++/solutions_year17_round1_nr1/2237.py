#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;
char m[100][100];
void cal(int right,int up,int down){
    if(up<down)return;
    int i,j,first,pre;
    bool bo=false;
    for(i=down;i<=up;i++){
        for(j=0;j<=right;j++)
            if(m[i][j]!='?'){bo=true;break;}
        if(bo)break;
    }
  //  printf("down:%d   up:%d   %d   %d\n",down,up,i,j);
    first=i;
    if(first>up){
        for(int k=down;k<=up;k++){
            for(int w=0;w<=right;w++){
                m[k][w]=m[down-1][w];
            }
        }
        return;
    }
    for(int k=0;k<j;k++)m[i][k]=m[i][j];
    pre=j;
    while(j<right){
        j++;
        while(j<=right&&m[i][j]=='?')j++;
      //  printf("pre:%d  j:%d\n",pre,j);
        for(int k=pre+1;k<j;k++)m[i][k]=m[i][pre];
        pre=j;
    }
    for(int k=down;k<=first;k++){
        for(int w=0;w<=right;w++){
            m[k][w]=m[first][w];
        }
    }
    cal(right,up,first+1);
}
int main()
{
    freopen("E://project/code-jam/2017/round1a/A-large.in","r",stdin);
    freopen("E://project/code-jam/2017/round1a/a-large.txt","w",stdout);
    int t,a,b,k=0;
    cin>>t;
    while(t--){
        scanf("%d%d",&a,&b);
        for(int i=0;i<a;i++)
            scanf("%s",m[i]);
        for(int i=0;i<a;i++){
            for(int j=0;j<b;j++){
                if(m[i][j]=='?'){

                }
            }
        }
        cal(b-1,a-1,0);
        printf("Case #%d:\n",++k);
        for(int i=0;i<a;i++){
            for(int j=0;j<b;j++)
                printf("%c",m[i][j]);
            printf("\n");
        }
    }
    return 0;
}
