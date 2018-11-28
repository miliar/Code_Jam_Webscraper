#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,x=0,flag,k,ct,i,j,l,l1;
    char str[2000];
    cin>>t;
    while(t--)
    {
        x++;
     cin>>str;
     l=strlen(str);
     l1=l;
     cout<<"Case #"<<x<<": ";
     if(l==1)
        cout<<str<<"\n";
     else
        {
            for(i=0;i<l-1;i++)
            {
                if(str[i]>str[i+1])
                {
                    str[i]--;
                    for(j=i+1;j<l;j++)
                        str[j]='9';
                    l=i+1;
                    i=-1;
                }
            }
            for(i=0;i<l1;i++)
            {if(str[i]!='0')
                    cout<<str[i];}
                    cout<<"\n";

        //Case #1: 3
        }
    }
    return 0;
}
