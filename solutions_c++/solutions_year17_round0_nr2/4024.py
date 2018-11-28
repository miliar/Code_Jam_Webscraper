#include<bits/stdc++.h>
#include<stdio.h>
using namespace std;

int main()
{
    freopen("In.txt", "r", stdin);
    freopen("Out.txt", "w", stdout);

    int t;
    cin>>t;

    for(int i = 0; i < t; ++i)
    {
        string s;
        cin>>s;

        int index = -1;
        for(int j = 0; j < s.length()-1; ++j)
        {
            if(s[j] > s[j+1])
            {
                index = j;
                break;
            }
        }

        if(index != -1)
        {
            for(int j = index; j >0; --j)
            {
                if(s[j] != s[j-1]) break;
                index = j-1;
            }
            s[index]--;
            for(int j = index+1; j < s.length(); ++j)
            {
                s[j] = '9';
            }
            if(s[index] == '0') s = s.substr(1,s.length()-1);
        }
        cout<<"Case #"<<i+1<<": "<<s<<endl;
    }
    return 0;
}
