#include<bits/stdc++.h>

using namespace std;

#define READ(f)         freopen(f,"r",stdin)
#define WRITE(f)        freopen(f,"w",stdout)

char str[34];
int main(void)
{
    READ("input.txt");
    WRITE("output.txt");
    int T,N=0;
    scanf("%d",&T);
    while(++N<=T){
        scanf("%s",str);
        int len=strlen(str);
        int low=0,ind=0;
        for(int i=0;i<len;i++){
            int val=str[i]-'0';
            if(val < low){
                ind=i;
                break;
            }
            low=val;
        }
        printf("Case #%d: ",N);
        if(ind){
            int last=9;
            bool flag=true;
            for(int i=ind;i<len;i++)str[i]='9';
            for(int i=ind-1;i>=0;i--){
                int val=str[i]-'0';
                if(flag){
                    if(i>0 && str[i]==str[i-1]){
                        str[i]='9';
                        continue;
                    }
                    val=val-1;
                    if(val > 0){
                        str[i]=val+'0';
                        flag=false;
                    }
                    else if(i > 0) str[i]='9';
                    else str[0]='0';
                }
                if(i < len-1){
                    if(str[i] > str[i+1]){
                        val=val-1;
                        if(val > 0){
                            str[i]=val+'0';
                        }
                        else if(i > 0){
                            str[i]='9';
                            flag=true;
                        }
                        else str[0]='0';
                    }
                }
            }
            ind=0;
            while(str[ind]=='0')ind++;
            for(int i=ind;i<len;i++)printf("%c",str[i]);
            printf("\n");
        }
        else printf("%s\n",str);
    }
    return 0;
}
