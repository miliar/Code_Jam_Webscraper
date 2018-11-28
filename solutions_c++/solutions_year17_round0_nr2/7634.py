#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
char s[25];
int  t,n;
bool nueve;
int main()
{
    freopen("entrada.in","r",stdin);
    freopen("salida.out","w",stdout);
    scanf("%d",&t);
    for (int caso=1;caso<=t;caso++){
        scanf("%s",&s);
        n = strlen(s);
        nueve = false;
        for (int i=0;i<n;i++){
            if (nueve)
                s[i]='9';
            else{
                if (i<n-1 && s[i+1]<s[i]){
                    nueve=true;
                    int voy=0;
                    while (s[voy]!=s[i]) voy++;
                    s[voy]--;
                    i=voy;
                }
            }
        }
        printf("Case #%d: ",caso);
        if (s[0]!='0') printf("%c",s[0]);
        for (int i=1;i<n;i++) printf("%c",s[i]);
        printf("\n");
    }
    return 0;
}
