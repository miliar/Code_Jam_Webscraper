#include <bits/stdc++.h>

using namespace std;

int main()
{
    char s[100];
    int t, i, a, j, l;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        scanf("%s", s);
        a = strlen(s);
        for(j=1;j<a;j++)
        {
            if(j>0 && s[j]<s[j-1])
            {
                for(l=j;l<a;l++)
                    s[l] = '9';
                s[j-1]--;
                j-=2;
            }
        }
        while(s[0]=='0')
        {
            for(j=0;j<a;j++)
            {
                s[j] = s[j+1];
            }
            a--;
        }
        cout<<"Case #"<<i<<": "<<s<<endl;
    }
    return 0;
}
