#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin>>tc;
    int cs = 0;
    while(tc--)
    {
        cs++;
        string str;
        cin>>str;
        //cout<<str<<endl;
        int sz = (int)str.size() ;
        int pos = -1;
        for(int i = sz - 1; i > 0 ; i--)
        {
            if(str[i] == '0')
            {
                pos = i;
                str[i] = '9';
                if(str[i-1]!='0')
                    str[i-1] -=1;
            }
            else if(str[i] < str[i-1])
            {
                pos = i;
                str[i] = '9';
                if(str[i-1]!=0)
                str[i-1] -=1;
            }
        }
        if(pos!=-1)
        {
        for(int i = pos; i < sz ; i++)
            str[i] = '9';
        }
        unsigned long long int ans = 0 , p = 10;
        for(int i = 0 ; i < sz ; i++)
        {
            ans *=p;
            ans += (str[i] - '0');
        }
        cout<<"Case #"<<cs<<": "<<ans<<endl;
    }
    return 0;
}
