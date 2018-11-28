#include<bits/stdc++.h>
using namespace std;

int main()
{   int t,k1=1;
    ifstream cin("inputf.in");
    ofstream cout("output.txt");
    cin>>t;
    while(t--)
    {   string s;
        cin>>s;
        int k=0,i,j,mpos=-1;
        long long int cnt=0,flg=0;
        cin>>k;
        for(i=0;i<s.length();)
        {   mpos=-1;
            if(s[i]=='-')
            {
                if(i+k<=s.length())
                {   s[i]='+';
                    cnt++;
                    for(j=i+1;j<i+k;j++)
                    {   if(s[j]=='+')
                        {   s[j]='-';
                            if(mpos==-1)
                            mpos=j;
                        }
                        else
                        s[j]='+';
                        //cout<<"j: "<<j<<"\n";
                    }
                }
            }
            if(mpos!=-1)
            i=mpos;
            else
            i=i+1;
            //cout<<"i: "<<i<<"\n";
        }
        for(i=0;i<s.length();i++)
        {   if(s[i]=='-')
            {   flg=1;
                break;
            }
        }
        if(flg==1)
        cout<<"Case #"<<k1<<": IMPOSSIBLE\n";
        else
        cout<<"Case #"<<k1<<": "<<cnt<<"\n";
        k1++;
    }
    return 0;
}
