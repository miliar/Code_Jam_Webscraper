#include<bits/stdc++.h>
using namespace std;
string s;

int check(int i,int k)
{
    for(int j=i;j<i+k;j++){
        if(s[j]=='+')s[j]='-';
        else s[j]='+';
    }
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,k,cs=0;
    scanf("%d",&t);

    while(t--){
        cin>>s>>k;
        int count=0,flag=0;
        for(int i=0;i<=s.length()-k;i++){
            if(s[i]=='+')continue;
            count++;
            check(i,k);
        }
        for(int i=0;i<s.length();i++){
            if(s[i]=='-')flag=1;
        }
        if(flag==1)printf("Case #%d: IMPOSSIBLE\n",++cs);
        else printf("Case #%d: %d\n",++cs,count);
    }
}
