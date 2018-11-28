/*
submitted by: prakhar8795
SLEEP. EAT. CODE. REPEAT.
*/
#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-small-attempt0.in","r",stdin) ;
    //freopen("B-large.in","r",stdin) ;
    freopen("B-otu-small-asdfsaf-codejam.out","w", stdout) ;

    int t,test=1;
    cin>>t;
    for(test=1;test<=t;test++)
    {
        string s;
        cin>>s;
        //cout<<s<<" ";
        int n=s.length(),j,i;
        if(n==1)
        {
        printf("Case #%d: ",test);
        cout<<s[0]<<endl;
            continue;
        }
        string ans="";
        for(i=0;i<n;i++)
        {
            if(i<n-1&&s[i]>s[i+1])
            {
               if(s[i]=='1')
               {
                   j=1;
                   while(j<n)
                   {
                       ans=ans+'9';
                       j++;
                   }
               }
               else
               {
                   if(i==0)
                   {
                       ans=s[i]-1;
                       j=1;
                       while(j<n)
                       {
                           ans=ans+'9';
                           j++;
                       }
                   }
                   else
                   {
                       j=i-1;
                       int flag=0;
                       while(j>=0&&s[j]==s[i])
                       {
                           flag=1;
                           ans[j]=ans[j]-1;
                           j--;
                       }
                       if(flag==0)
                       {
                            j=i+1;
                            ans+=s[i]-1;
                       }
                       else
                       {
                           j=i;
                       }
                       while(j<n)
                       {
                           ans=ans+'9';
                           j++;
                       }
                   }
               }
               break;
            }
            ans=ans+s[i];
        }
        printf("Case #%d: ",test);
        cout<<ans<<endl;
    }
return 0;
}
