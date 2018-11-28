#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long t,z,l,flag,i,j;string s;
    cin>>t;
    for(z=1;z<=t;z++)
    {
        cin>>s;
        l=s.size();
        flag=0;
        for(i=l-1;i>0;i--)
        {
            if(s[i]<s[i-1] && s[i]!=0 && s[i-1]!=0)
                {
                    for(j=i;j<l;j++)
                        s[j]='9';
                    s[i-1]=s[i-1]-1;
                    if(s[i-1]=='0')
                        i++;
                }
            while(s[i]=='0')
            {
                flag=1;
                i--;
            }
            if(flag==1)
            {
                s[i]=s[i]-1;
                for(j=i+1;j<l;j++)
                    s[j]='9';
                if(s[i]=='0')
                    i++;
                flag=0;
            }
 
        }
        printf("Case #%lld: ",z);
        flag=0;
        for(i=0;i<l;i++)
         {
                 if(s[i]!='0')
                 {
                     flag=1;
                 }
                 if(flag==1)
                    cout<<s[i];
         }
         cout<<endl;
    }
    return 0;
}

