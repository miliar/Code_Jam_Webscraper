#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, k, i, j, l, r, p;
    char s[10000];
    cin>>t;
    for(i=1;i<=t;i++)
    {
        r = 0;
        p = 1;
        scanf(" %s %i", s, &k);
        for(j=0;j<strlen(s);j++)
        {
            if(s[j]=='-')
            {
                if(j+k-1<strlen(s))
                {
                    r++;
                    for(l=0;l<k;l++)
                    {
                        if(s[j+l]=='-')
                            s[j+l] = '+';
                        else
                            s[j+l] = '-';
                    }
                }
                else
                {
                    p = 0;
                }
            }
        }
        cout<<"Case #"<<i<<": ";
        if(p==1)
        {
            cout<<r<<endl;
        }
        else
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
    }
    return 0;
}
