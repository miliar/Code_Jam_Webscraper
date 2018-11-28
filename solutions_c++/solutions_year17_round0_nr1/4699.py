#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,k;
    string s;
    cin>>t;
    for(int m=1;m<=t;m++)
    {
        int count1=0;
        cin>>s>>k;
        int l=s.size()-k+1;
        for(int i=0;i<l;i++)
        {
          /*  for(int j=i;j<k+i;j++)
            {
                if(s[j]=='-')
                {
                    s[j]='+';
                    count1++;
                }
            }*/
            if(s[i]=='-')
            {
                count1++;
                for(int j=i;j<k+i;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
        }
        int flag=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-')
            {
                flag=1;
                break;
            }
        }
        if(flag==0)
        {
            cout<<"Case #"<<m<<": "<<count1<<endl;
        }
        else
        {
            cout<<"Case #"<<m<<": IMPOSSIBLE"<<endl;
        }
    }
    return 0;
}
