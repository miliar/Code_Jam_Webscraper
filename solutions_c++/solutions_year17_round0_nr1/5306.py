#include<iostream>
using namespace std;
int main()
{
    string s;
    int l,c,tc,tc2,cnt,flag,test;
    cin>>test;
    for(int kk=0;kk<test;kk++)
    {
        cout<<"Case #"<<kk+1<<": ";
        cin>>s;
        cin>>l;
        cnt=0;
        for(c=0;c<s.length()-l+1;c++)
        {
            if(s[c]=='-')
            {
                cnt++;
                for(tc=0,tc2=c;tc<l;tc++,tc2++)
                {
                    if(s[tc2]=='+')
                        s[tc2]='-';
                    else
                        s[tc2]='+';
                }
            }
        }
        flag=0;
        for(c=0;c<s.length();c++)
        {
            if(s[c]=='-')
            {
                flag=1;
                break;
            }
        }
        if(flag==1)
            cout<<"IMPOSSIBLE";
        else
            cout<<cnt;
        cout<<endl;
    }
}
