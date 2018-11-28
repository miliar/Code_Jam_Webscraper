#include<bits/stdc++.h>
using namespace std;
int main()
{
     freopen("teesra.in","r",stdin);
    freopen("teesra.out","w",stdout);
    int tt;
    cin>>tt;
    for(int t=1;t<=tt;t++)
    {
         printf("Case #%d: ",t);
        string str;
        cin>>str;
       //string ans="";
       //vector<long long> v;
       //cout<<str<<endl;
        long long int l=str.length();
        //cout<<l<<endl;
        for(int i=0;i<l-1;i++)
        {
             if(str[i]>str[i+1])
             {
                str[i]=str[i]-1;
            for(int j=i+1;j<l;j++)
             str[j]='9';
                i=-1;
        }
        }
        if(str[0]=='0')
        {
            for(int i=1;i<l;i++)
            {
                cout<<str[i];
            }
        }
        else
        {
            for(int i=0;i<l;i++)
            {
                cout<<str[i];
            }
        }
        cout<<"\n";
    }
    return 0;
}
