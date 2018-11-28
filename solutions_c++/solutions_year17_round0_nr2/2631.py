#include <iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
int t, ls, pozitie,poz;
char s[30];

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++){
        scanf("%s",&s);
        ls=strlen(s);
        for (int i=0;i<ls-1;i++){
            if (s[i]>s[i+1]){
                for (int j=i+1;j<ls;j++)
                    s[j]='9';
                pozitie=i;
                poz=i-1;
                while ((poz>=0)&&(s[poz]==s[poz+1]))
                    poz--;
                s[poz+1]--;
                for (int j=poz+2;j<ls;j++)
                    s[j]='9';
                if (s[0]=='0'){
                    s[0]='#';
                    for(int i=1;i<=pozitie;i++)
                        s[i]='9';
                }
                break;
            }
        }
        printf("Case #%d: ",ii);
        for (int i=0;i<ls;i++)
            if (s[i]!='#')
                printf("%c",s[i]);
        printf("\n");
    }
    return 0;
}
