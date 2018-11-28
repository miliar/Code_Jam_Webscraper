#include <bits/stdc++.h>
#include <string>
using namespace std;
long long int n;
//unordered_map<int,int> m;
bool check(string s)
{
    for(int i=0;i+1<s.size();i++)
    {
        if(s[i]>s[i+1])return false;
    }
    return true;
}
string fun(string s)
{
    for(int i=0;i+1<s.size();i++)
        {
            if(s[i]>s[i+1])
            {
                if(s[i]=='1')
                {
                    for(int j=0;j+1<s.size();j++)
                    {
                        s[j]='9';
                    }
                    s.pop_back();
                    //cout<<22222222<<endl;
                    break;
                }
                s[i]=s[i]-1;
                for(int j=i+1;j<s.size();j++)
                {
                    s[j]='9';
                }
                break;
            }
        }
       // cout<<s<<endl;
    return s;
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int test;cin>>test;
    int mn=1;
    while(test--)
    {
        string s;cin>>s;
        cout<<"Case #"<<mn++<<": ";
        while(!check(s))s=fun(s);
        cout<<s<<endl;
    }
    return 0;
}
/*
10
23651
62986
123665
462389

23599
59999
123599   123659
459999
*/
