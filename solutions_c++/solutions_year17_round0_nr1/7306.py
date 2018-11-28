#include<bits/stdc++.h>
using namespace std;

string flip(string s, int start, int end)
{
    for(int i=start; i<start+end; i++)
        if(s[i]=='+')s[i]='-';
        else
            s[i]='+';
    return s;
}

void pancakeFlipper(string s, int k, int t)
{
    int n = s.length(), cnt = 0, flag = 1;
    for(int i=0; i+k-1<n; i++)
    {
        //cout<<s[i]<<' '<<i<<' '<<i+k-1<<' '<<s;
        if(s[i]=='-')
        {
            s = flip(s, i, k);
            cnt++;
        }
        //cout<<'\t'<<s<<endl;
    }
    for(int i=0; i<n; i++)
        if(s[i]=='-')flag=0;
    if(flag)
        cout<<"Case #"<<t<<": "<<cnt<<endl;
    else
        cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
}

int main()
{
    long T;
    cin>>T;
    for(int t=1; t<=T; t++)
    {
        string s;
        int k;
        cin>>s>>k;
        pancakeFlipper(s, k, t);
    }
}
