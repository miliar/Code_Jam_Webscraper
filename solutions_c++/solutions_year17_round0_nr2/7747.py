
#include<bits/stdc++.h>
using namespace std;
int main()
{
    long t,n,i,j,k,len,l;
    string s;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>s;
        len=s.length();
        j=0;
        while(j+1<len&&s[j]<=s[j+1])
            j++;
        if(j+1==len)
            cout<<"Case #"<<i<<": "<<s<<endl;
        else
        {
            if(s[j]=='1')
            {
                cout<<"Case #"<<i<<": ";
                for(int m=0;m<len-1;m++)
                {
                    cout<<9;
                }
                cout<<endl;
            }
            else
            {
                k=j;
                for(l=j+1;l<len;l++)
                    s[l]='9';
                while(k>0&&s[k]==s[k-1])
                {
                    s[k]='9';
                    k--;
                }
                s[k]=s[k]-1;
                cout<<"Case #"<<i<<": "<<s<<endl;
            }

        }
    }
    return 0;
}

