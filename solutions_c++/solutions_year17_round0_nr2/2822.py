#include<bits/stdc++.h>
using namespace std;
int main()
{    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int t,z=1;
    cin>>t;
    while(t--)
    {
     string s;
     cin>>s;
     for(int i=1;i<s.size();i++)
     {
         if(s[i]<s[i-1])
         {
             int temp=i;
             s[i]='9';
             s[i-1]=s[i-1]-1;
             while(1)
             {

                 if(s[i-1]<s[i-2])
                 {
                     s[i-1]='9';
                     i--;
                     s[i-1]-=1;
                     if(i-1==1&&s[0]=='0')
                     {
                         s[0]='0';
                         break;
                     }
                 }
                 else
                    break;
             }
             for(int j=temp+1;j<s.size();j++)
                s[j]='9';
             break;
         }

     }
     cout<<"Case #"<<z<<": ";
     if(s[0]!='0')
        cout<<s[0];
     for(int i=1;i<s.size();i++)
        cout<<s[i];
     cout<<endl;
     z++;
    }
    return 0;
}
