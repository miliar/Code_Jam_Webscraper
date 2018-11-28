#include <iostream>
#include <string>
using namespace std;
char inv(string as)
{
    if(as=="-")
    {
        return '+';
    }
    else
    {
        return '-';
    }
}
bool check(string asd)
{
    int c=0;
    string s12;
    for(int j=0;j<asd.size();j++)
    {
        s12=asd[j];
        if(s12=="-")
        {
            c=1;
            break;
        }
    }
    return c;
}
int main()
{
    string s,s1,s2;
    int n,q,c;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        c=0;
        cin>>s>>q;
        for(int j=0;j<s.size();j++)
        {
            s1=s[j];
            if((s1=="-"))
            {
                if((j+q)<=s.size())
                {
                    for(int k=j;k<j+q;k++)
                    {
                        s2=s[k];
                        s[k]=inv(s2);
                    }
                    c++;
                }
                else
                {
                    break;
                }
            }
        }
        if(check(s))
        {
            cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            cout<<"Case #"<<i+1<<": "<<c<<endl;
        }
    }
    return 0;
}