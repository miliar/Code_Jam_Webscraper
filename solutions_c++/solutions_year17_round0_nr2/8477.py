#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

int main()
{
    int T;
    freopen("B-large.in","r",stdin);
    freopen("bout2.txt","w",stdout);
    cin>>T;
    for (int j=1;j<=T;j++)
    {
        string s;
        cin>>s;
        bool chk=false;
        long long flag=0;
        long long l = s.length();
        if (l==1)
        {
            cout<<"Case #"<<j<<": "<<s<<endl;
        }
        else
        {
            for (long long i=1;i<l;i++)
            {
                if(s[i]<s[i-1])
                {
                    chk = true;
                    i=i-1;
                    while(s[i]==s[i-1])
                        i--;
                    s[i] = s[i] - 1;
                    flag=i+1;
                    break;
                }
            }
            int x=0;
            if (s[0]=='0')
                x=1;
            cout<<"Case #"<<j<<": ";
            if (!chk)
                cout<<s;
            else
            {
                for (long long i=x;i<l;i++)
                {
                    if(i<flag)
                        cout<<s[i];
                    else
                        cout<<9;
                }
            }

            cout<<endl;
        }
    }
    return 0;
}
