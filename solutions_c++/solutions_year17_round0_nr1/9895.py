#include <bits/stdc++.h>

using namespace std;
int t,k,cnt;
string s;
int main()
{
    freopen("A-small-attempt0.out","w",stdout);
    cin >>t;
    for (int i=1;i<=t;i++)
    {
        cin >>s>>k;
        cout <<"Case #"<<i<<":"<<" ";
        for (int j=0;j<s.size()-k;j++)
        {
            if (s[j]=='-')
                 {
                     for (int q=j;q<=j+k-1;q++)
                     {
                         s[q]=='-'?s[q]='+':s[q]='-';
                     }
                     cnt++;
                 }
        }
        for (int j=s.size()-k;j<s.size()-1;j++)
        {
            if (s[j]!=s[j+1]){
            cout <<"IMPOSSIBLE\n";
            goto ss;
            }
        }
        if (s[s.size()-1]=='-') cnt++;
        cout <<cnt<<"\n";
        ss:
        cnt=0;
    }
    return 0;
}
