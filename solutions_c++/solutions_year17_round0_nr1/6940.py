#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;
string s;
int k,t,ans;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    for (int i=0;i<t;i++)
    {
        bool e=0;
        cin >> s >> k;
        ans=0;
        cout << "Case #" << i+1 << ": ";
        for (int j=0;j<s.size();j++)
        {
            if (s[j]=='-')
            {
                ans++;
                if (j+k<=s.size())
                {
                    for (int l=j;l<j+k;l++)
                    {
                        if (s[l]=='+') s[l]='-';
                        else s[l]='+';
                    }
                }
                else e=1;
            }
        }
        if (e) cout << "IMPOSSIBLE\n";
        else cout << ans << "\n";
    }
    return 0;
}
