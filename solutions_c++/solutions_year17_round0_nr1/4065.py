#include <bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define debug(x) cerr << #x << " = " << x << endl;

string flip(string s, int x, int k)
{
    for(int i = x; i < x+k; ++i)
    {
        if(s[i] == '-') s[i] = '+';
        else s[i] = '-';
    }
    //debug(s);
    return s;
}

int main() {

    freopen("Input.txt", "r",stdin);
    freopen("Out.txt", "w", stdout);
    int t;
    cin>>t;

    for(int j = 0; j < t; ++j)
    {   string s;
        int k;
        cin>>s>>k;
        int count=0;
        for (int i=0;i<s.length()-k+1;i++)
        {
            if(s[i]=='-')
            {
                s = flip(s,i,k);
                count++;
            }
        }

        int flag = 0;
        for(int i = s.length()-k; i < s.length(); ++i)
        {
            if(s[i] == '-')
            {
                flag = 1;
                break;
            }
        }
        //debug(m);
        cout<<"Case #"<<j+1<<": ";
        if(flag)
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            cout<<count<<endl;
        }
    }
    return 0;
}
