#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
char cad [1005];
void _swap(int x){
    if (cad[x]=='-') cad[x]='+';
    else cad[x]='-';
}
int main()
{
    int t,k,l,ans;
    bool suc;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for (int _case=1; _case<=t; _case++){
        scanf("%s %d",cad,&k);
        l=strlen(cad);
        ans=0;
        for (int i=0; i<=(l-k); i++){
            if (cad[i]=='-'){
                ans++;
                for (int j=i; j<i+k; j++){
                    _swap(j);
                }
            }
        }
        suc=true;
        for (int i=0; i<l; i++){
            if (cad[i]=='-'){
                suc=false;
                break;
            }
        }
        if (!suc) printf("Case #%d: IMPOSSIBLE\n",_case);
        else printf("Case #%d: %d\n",_case,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
