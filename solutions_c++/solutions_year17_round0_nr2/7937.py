#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
bool check(string s)
{
    for(int i=0;i<s.size()-1;i++)
    {
        ll a=s[i]-'0',b=s[i+1]-'0';
        if(a>b)
            return false;
    }
    return true;
}
int main()
{
	cin.tie(NULL);
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	ll t,n;
	cin>>t;
	for(int qq=1;qq<=t;qq++)
    {
        string s;
        cin>>n;
        stringstream ss;
        ss<<n;
        s=ss.str();
        while(!check(s))
        {
            if(s.size()==1)
                break;
            int flag=0;
            for(int i=0;i<s.size()-1;i++)
            {
                ll a=s[i]-'0',b=s[i+1]-'0';
                if(a>b)
                {
                    if(a==9&&flag==1)
                    {
                        s[i+1]='9';
                    }
                    else if(a==1)
                        {
                            char c='9';
                            s[i]='0';
                            s[i+1]=c;
                            flag=1;
                        }
                    else
                        {
                            a--;
                            char c=a+'0';
                            s[i]=c;
                            s[i+1]='9';
                            flag=1;
                        }
                }
            }
        }
        ll k=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]!='0')
                break;
            else
                k++;
        }
        cout<<"Case #"<<qq<<": ";
        for(int i=k;i<s.size();i++)
        {
            cout<<s[i];
        }
        cout<<"\n";
    }
	return 0;
}
