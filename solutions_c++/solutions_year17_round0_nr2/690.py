#include<bits/stdc++.h>
#define f first
#define s second
using namespace std;
char s[10005];
int main(){
    int t,T=0;;
    scanf("%d",&t);
    while(t--){T++;
        scanf("%s",s);
        int n=strlen(s);
        int ni=n;
        for(int i=n-2;i>=0;i--){
            if(s[i+1]<s[i]){
                ni=i+1;
                s[i]--;
                }
            }
        for(int i=ni;i<n;i++)
            s[i]='9';
        int shft=0;
        for(int i=0;i<n;i++)
            if(s[i]=='0')
                shft=i+1;
            else
                break;
        printf("Case #%d: %s\n",T,s+shft);
        }
    return 0;
    }
