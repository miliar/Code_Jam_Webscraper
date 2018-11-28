#include<bits/stdc++.h>
using namespace std;
char s[30][30];
char cnt[30];
int cntc[30];
int main(){
    FILE *fp1 = fopen("C:\\Users\\Hmc1994\\Downloads\\A-large.in","r+");
    FILE *fp2 = fopen("C:\\Users\\Hmc1994\\Downloads\\ans.out","w+");
    int t;
    int ansn=1;
    fscanf(fp1,"%d",&t);
    while(t--){
        int r,c;
        fscanf(fp1,"%d%d",&r,&c);
        for(int i=1;i<=r;i++){
            fscanf(fp1,"%s",*(s+i)+1);
        }

        for(int i=1;i<=r;i++){
            int cur=1;
            for(int j=1;j<=c;j++){
                if(s[i][j]!='?'){
                    cnt[cur++]=s[i][j];
                }
            }
            int tot=1;
            if(cur==1) continue;
            else{
                for(int j=1;j<=c;j++){
                    if(s[i][j]=='?'){
                        if(tot<cur)
                            s[i][j]=cnt[tot];
                        else
                            s[i][j]=cnt[cur-1];
                    }
                    else{
                        tot++;
                    }
                }
            }
        }
        memset(cntc,0,sizeof(cntc));
        int tot=1,cur=1;
        for(int i=1;i<=r;i++){
            if(s[i][1]!='?'){
                cntc[tot++]=i;
            }
        }
        for(int i=1;i<=r;i++){
            if(s[i][1]=='?'){
                for(int j=1;j<=c;j++){
                    if(cur<tot)
                        s[i][j]=s[cntc[cur]][j];
                    else
                        s[i][j]=s[cntc[tot-1]][j];
                }
            }
            else{
                cur++;
            }
        }
        fprintf(fp2,"Case #%d:\n",ansn++);
        for(int i=1;i<=r;i++){
            fprintf(fp2,"%s\n",*(s+i)+1);
        }
    }
}
