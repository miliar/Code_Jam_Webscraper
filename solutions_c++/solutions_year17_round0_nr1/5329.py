#include <bits/stdc++.h>
using namespace std;
int notenoughcharforplus(string s,int i,int a)
{
    int rem=s.size()-i-1;
    //cout<<"rem "<<rem<<endl;
    return (rem<a)?1:0;
}
int notenoughcharforminus(string s,int i,int a)
{
    int rem=s.size()-i;
    //cout<<"rem "<<rem<<endl;
    return (rem<a)?1:0;
}
int func(string s,int i,int a)
{
     for(int index=i;index<(i+a);index++)
        if(s[index]!='-')return 0;
    return 1;
}
string convert(string s,int i,int a)
{
    for(int index=i;index<(i+a);index++)
        s[index]='+';
    return s;
}
string flip(string s,int i,int a)
{
    for(int index=i;index<(i+a);index++)
    {
        if(s[index]=='+')
            s[index]='-';
        else s[index]='+';
    }
    return s;
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;
    for(int p=1;p<=t;p++)
    {
    int a;
    string s;
    cin>>s;
    cin>>a;
    int flag=0,cnt=0;
    for(int i=0;i<s.size();)
    {
        if(s[i]=='-')
        {
            if(notenoughcharforminus(s,i,a))
            {
                flag=1;
                break;
            }
            else if(func(s,i,a))
            {
                s=convert(s,i,a);
                //cout<<"convert "<<s<<endl;
                cnt+=1;
            }
            else
            {
                if(notenoughcharforplus(s,i,a))
                {
                    flag=1;
                    break;
                }
                //cout<<"else 1 "<<s<<endl;
                s=flip(s,i+1,a);
                cnt+=1;
                //cout<<"else 2 "<<s<<endl;
                s=flip(s,i,a);
                cnt+=1;
                //cout<<"else 3 "<<s<<endl;
            }
            //cout<<s<<endl;
        }
        else i++;
    }
    cout<<"Case #"<<p<<": ";
    if(flag==1)
        cout<<"IMPOSSIBLE"<<endl;
    else
        cout<<cnt<<endl;
    }
}
