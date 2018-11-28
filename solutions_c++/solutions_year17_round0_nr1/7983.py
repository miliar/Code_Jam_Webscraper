#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t,n,count1=0;
    cin>>t;
    string st;
    for(int i=1; i<=t; i++)
    {
        int f=0;
        cin>>st>>n;
        int sz=st.size();
        count1=0;
        for(int j=0; j<=sz-n; j++)
        {
            if(st[j]=='-')
            {
                for(int k=j; k<(j+n); k++)
                {
                    if(st[k]=='-')
                    {
                        st[k]='+';
                    }
                    else
                    {
                        st[k]='-';
                    }
                }
                count1++;
                //cout<<st<<endl;
            }
        }


        for(int h=0; h<sz; h++)
        {
            if(st[h]=='-')
            {
                cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
                f=1;
                break;

            }

        }
        if(f==0)
        {
            cout<<"Case #"<<i<<": "<<count1<<endl;
        }


    }
    return 0;
}
