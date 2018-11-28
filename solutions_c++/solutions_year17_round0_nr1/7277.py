#include<bits/stdc++.h>
using namespace std;
int main()
{

    int t;
    cin>>t;
    int b=1;
    while(b<=t)
    { int k,n,count=0,count1=0,flag=1;
        string s;
        cin>>s;
        int l=s.length();
        cin>>k;
        for(int i=l-1;i>=k-1;i--)
        {
            if(s[i]=='-')
            {  n=i;
                for(int m=0;m<k;m++)
                {
                    if(s[n]=='-')
                    {
                        s[n]='+';
                    n--;
                    }
                    else if(s[n]=='+')
                    {
                        s[n]='-';
                    n--;
                    }
                    }
            count++;
            }
            }
            for(int i=0;i<k-1;i++)
            {
                if(s[i]=='-')
                  {
                flag=0;
                break;
            }
            }

        if(flag==0)
            cout<<"Case #"<<b<<": "<<"IMPOSSIBLE"<<"\n";
            else
                cout<<"Case #"<<b<<": "<<count<<"\n";
    b++;
    }
}
