#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
#include<string>
using namespace std;
bool check(string str)
{
    int len=str.size();
    int c1=0;
    for(int i=0;i<len;i++)
    {
        if(str[i]=='+')c1++;
    }
    if(c1==len)return true;
    else return false;
}

int main()
{
    int i,j,k,n,t,tcase=0;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    while(t--){
    tcase++;
    string str;
    cin>>str>>k;
    int cnt=0;
    int flag=0;
    int len=str.size();
    for(i=0;i<len;i++)
    {
        if(str[i]=='-')
        {
            if((i+k-1)>len-1)
            {
                flag=1;
                break;
            }
            else{
            for(j=i;j<i+k;j++)
            {
                if(str[j]=='+')str[j]='-';
                else str[j]='+';
            }
            cnt++;
            }
        }
    }
    if(flag==1)printf("Case #%d: IMPOSSIBLE\n",tcase);
    else printf("Case #%d: %d\n",tcase,cnt);
    }
    return 0;

}
