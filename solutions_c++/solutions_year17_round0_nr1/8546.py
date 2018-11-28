/*
submitted by: prakhar8795
SLEEP. EAT. CODE. REPEAT.
*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("A-small-attempt0.in","r",stdin) ;
    freopen("A-large.in","r",stdin) ;
    freopen("A-prakhar-large.out","w", stdout) ;
    int t,test;
    cin>>t;
    for(test=1;test<=t;test++)
    {
        string s;
        cin>>s;
        int n=s.length(),k,i,coun=0,j;
        cin>>k;
        int flag=0;
        for(i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
                if(i+k>n)
                {
                    flag=1;
                    break;
                }
                for(j=i;j<i+k;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                coun++;
            }

        }
        if(flag==1)
        {
            printf("Case #%d: ",test);
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            printf("Case #%d: ",test);
            cout<<coun<<endl;
        }
    }
return 0;
}
