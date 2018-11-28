#include<iostream>
#include<string>
using namespace std;
void palat(string &s,int start,int range)
{
    for(int i=start;i<start+range;i++)
    {
        if(s[i]=='+')
            s[i]='-';
        else
            s[i]='+';
    }
}
bool check(string str,int s,int r)
{
    if(str[s]=='-')
       if(str[s+r]=='-'||str[s+r-1]=='-')
          return true;
    if(str[s+r-1]=='-')
       if(str[s-1]=='-')
          return true;
    if((str[s-1]==str[s+r])&&(str[s-1]=='-'))
          return true;
    if((str[s]=='-')&&(str[s+r-1]=='+'))
        return true;
    return false;
}
bool isplus(string s)
{
    for(int i=0;i<s.length();i++)
    {
        if(s[i]=='-')
            return false;
    }
    return true;
}
int main()
{
    int t,n;
    string s;
    bool tmp=false;
    cin>>t;
    int k=0,num;
    while(t--)
    {
        k++;
        cin>>s>>n;
        cout<<"Case #"<<k<<": ";
        tmp=true;
        num=0;
        while(!isplus(s))
        {
            tmp=false;
            for(int i=0;i<s.length()-n+1;i++)
            {
                if(check(s,i,n))
                {
                    palat(s,i,n);
                    tmp=true;
                    num++;
                }
            }
            if(!tmp)
                break;
        }
        if(!tmp)
            cout<<"IMPOSSIBLE\n";
        else cout<<num<<'\n';
    }
    return 0;
}
