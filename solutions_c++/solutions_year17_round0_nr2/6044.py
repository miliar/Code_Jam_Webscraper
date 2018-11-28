#include <bits/stdc++.h>


using namespace std;

int ascending(string s)
{

    for(int i=0;i<s.length();i++)
    {
        for(int j=i+1;j<s.length();j++)
        {
            if(s[i]>s[j])
                return 0;
        }
    }
    return 1;


}

string  prev_asc(string s)
{
int last_diff=0;
    for(int i=0;i<s.length()-1;i++)
    {

        if(s[i]>s[i+1])
        {
            s[last_diff]=(s[last_diff]-1);
        for(int j=last_diff+1;j<s.length();j++)
        {
            s[j]='9';
        }
        break;
        }
        else if(s[i]<s[i+1])
        {
            last_diff=i+1;

        }


    }
    if(s[0]=='0')
        return s.substr(1,s.length()-1);
    return s;

}


int main()
{

freopen("B-large.in","r",stdin);
freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int r=0;
    while(t--)
    {
        r++;
        //long long int n;
        //cin>>n;
        string s;
        cin>>s;
        if(ascending(s))
        {
            //cout<<"asc"<<endl;
            cout<<"Case #"<<r<<": "<<s<<endl;
        }
        else
        {
            string prev=prev_asc(s);
        cout<<"Case #"<<r<<": "<<prev<<endl;

        }

//cout<<"Case #"<<r<<": "<<"IMPOSSIBLE"<<endl;

    }

}
