#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    cin >> t;
    int cs=1;
    string s;
    int k,tt,j;

    while(t--)
    {
        cin >> s;
        cin >> k;
        int cnt=0;
        for(int i=0;i<=s.size()-k;i++)
        {
            if(s[i]=='-')
            {
                tt=k;
                j=i;
                while(tt--)
                {
                    if(s[j]=='+') s[j]='-';
                    else s[j]='+';
                    j++;
                }
                cnt++;
            }
        }
        bool hobe=true;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-')
                hobe=false;
        }
        printf("Case #%d: ",cs++);
        if(hobe) cout << cnt <<endl;
        else cout << "IMPOSSIBLE" <<endl;
    }

    return 0;
}
