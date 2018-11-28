#include <bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define debug(x) cerr << #x << " = " << x << endl;

string flipper(string s, int l, int k)
{
    for(int i = 0; i < k; i++)
    {
        if(s[l+i] == '-')
        {
            s[l+i] = '+';
        }
        else
        {
            s[l+i] = '-';
        }
    }
    //debug(s);
    return s;
}

int main() {

    freopen("input.txt", "r",stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin>>t;

    for(int i = 0; i < t; i++)
    {
        string s;
        int k;
        cin>>s>>k;
        int c=0;
        for (int j=0; j < s.length()-k+1 ;j++)
        {
            if(s[j]=='-')
            {
                s = flipper(s,j,k);
                c++;
            }
        }

        bool flag = false;
        for(int j = s.length() - k ; j < s.length(); j++)
        {
            if(s[j] == '-')
            {
                flag = true;
                break;
            }
        }
        //debug(m);
        cout<<"Case #"<<i+1<<": ";
        if(flag)
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            cout<<c<<endl;
        }
    }
    return 0;
}
