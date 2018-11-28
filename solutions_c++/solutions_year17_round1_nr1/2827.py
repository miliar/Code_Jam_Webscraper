#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
const int maxn=30;
/*
1
3 4
????
?CJ?
????
*/
char cake[maxn][maxn];
int main()
{
    int t;
    int r,c;
    char str[30];
    FILE*f1=fopen("A-small-attempt1.in","r");
    FILE*f2=fopen("A-small-attempt1.out","w");
    fscanf(f1,"%d",&t);
    //scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        fscanf(f1,"%d %d",&r,&c);
        //scanf("%d %d",&r,&c);
        for(int i=0;i<r;i++){
            fscanf(f1,"%s",str);
            //scanf("%s",str);
            for(int j=0;j<c;j++){
                cake[i][j]=str[j];
            }
        }
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(cake[i][j]=='?')
                    continue;
                for(int k=j-1;k>=0;k--){
                    if(cake[i][k]=='?')
                        cake[i][k]=cake[i][j];
                    else
                        break;
                }
                for(int k=j+1;k<c;k++){
                    if(cake[i][k]=='?')
                        cake[i][k]=cake[i][j];
                    else
                        break;
                }
            }
        }
        for(int i=0;i<r;i++){
            bool isempty=true;
            for(int j=0;j<c;j++){
                if(cake[i][j]!='?'){
                    isempty=false;
                    break;
                }
            }
            if(isempty){
//printf("empty: %d\n",i);
                char ch;
                bool flag=false;
                for(int j=0;j<c;j++){
                    //search up
                    flag=false;
                    for(int k=i-1;k>=0;k--){
                        if(cake[k][j]!='?'){
                            ch=cake[k][j];
                            flag=true;
                            break;
                        }
                    }
                    if(flag){
                        for(int k=i;k>=0;k--){
                            if(cake[k][j]=='?')
                                cake[k][j]=ch;
                            }
                        }
                    //search down
                    else{
//printf("sada\n");
                        for(int k=i+1;k<r;k++){
                            if(cake[k][j]!='?'){
                                ch=cake[k][j];
                                break;
                            }
                        }
                        for(int k=i;k<r;k++){
                            if(cake[k][j]=='?')
                                cake[k][j]=ch;
                        }
                    }
                }
            }
        }
        fprintf(f2,"Case #%d:\n",tt);
        //printf("Case #%d\n",tt);
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                fprintf(f2,"%c",cake[i][j]);
                //printf("%c",cake[i][j]);
            }
            fprintf(f2,"\n");
            //printf("\n");
        }
    }
    fclose(f1);
    fclose(f2);
    return 0;
}
