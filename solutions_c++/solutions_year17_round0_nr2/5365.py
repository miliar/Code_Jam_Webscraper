#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int n;
    cin>>n;
    for(int t=1;t<=n;t++)
    {
        string str;
        cin>>str;
        string tmp=str;
        int sz=str.size();
        if(sz==1)
        {
            cout<<"Case #"<<t<<": "<<str<<endl;
            continue;
        }
        bool ss=false;
        for(int i=0;i<sz-1;i++)
        {
            if(ss)
            {
                i=0;
                ss=false;
            }
            if(str[i]>str[i+1])
            {
                ss=true;
                int d=i;
                int di=str[d]-'0';
                di--;
                if(di<0)
                    di=0;
                str[d]=di+'0';
                for(int j=d+1;j<sz;j++)
                {
                    str[j]='9';
                }
                if(i==0)
                    break;
                i=0;
               // cout<<i<<endl;
            }

        }

        if(str[0]=='0')
            str.erase(0,1);
        cout<<"Case #"<<t<<": "<<str<<endl;


    }
    return 0;
}
