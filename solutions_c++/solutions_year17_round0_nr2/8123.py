#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen ("B-large (1).in", "r", stdin);
    freopen ("output.txt", "w", stdout);
    //ifstream F("prefix.in");   //for eof problem
    char c;
    int T;
    string s;
    cin>>T;
    for(int t = 1; t<=T;t++)
    {
        cin>>s;
        int n = s.length();

        for(int i = 0;i<n-1;i++)
        {
            if(s[i] == '1' && s[i+1] =='0')
            {
                s = "";
            for(int x = 0; x<n-1;x++)
                s+='9';
            break;
            }


            if(s[i]-'0' > s[i+1]-'0')
            {
                int l = i;
                string t = s;
                for(int x = i;x>=0;x--)
                {
                    if(s[x]==s[i])l=x;
                    else break;
                }
                s = t.substr(0,l);
                if(t[l]!='1')
                s+=(t[l]-1);
                for(int x = 0; x<n-l-1;x++)
                    s+='9';
                break;
            }

        }
        printf("Case #%d: ", t);
        cout<<s<<endl;

    }
    return 0;
}
