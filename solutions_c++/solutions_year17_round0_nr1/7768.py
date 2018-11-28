#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int d=1;d<=t;d++){
        string s;
        int k;
        bool f=false;
        cin>>s>>k;
        int n=s.size(),c=0;
        for(int i=0;i<n;i++)
            if(s[i]=='-'&&i+k<=n){
                c++;
                for(int j=i;j<i+k;j++){
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
            }
        for(int i=0;i<n;i++)
            if(s[i]=='-'){
                f=true;break;
            }
        printf("Case #%d: ",d);
        if(f)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",c);

    }
    return 0;
}
