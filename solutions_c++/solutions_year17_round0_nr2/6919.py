#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;
int l=0,p=-1,t;
string s;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    string s;
    for (int q=0;q<t;q++)
    {
        cout << "Case #" << q+1 << ": ";
        cin >> s;
        l=0;
        p=-1;
        for (int i=1;i<s.size();i++)
        {
            if (s[i]>s[i-1]) l=i;
            if (s[i]<s[i-1])
            {
                p=i;
                break;
            }
        }
        if (p==-1)
        {
            cout << s << "\n";
            continue;
        }
        for (int i=0;i<l;i++)
        {
            cout << s[i];
        }
        if (!(s[l]=='1' && l==0))
            cout << int(s[l]-'0')-1;
        for (int i=l+1;i<s.size();i++)
        {
            cout << "9";
        }
        cout << "\n";
    }
    return 0;
}

