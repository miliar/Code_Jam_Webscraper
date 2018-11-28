#include<bits/stdc++.h>
#define inf 1000000000
using namespace std;

string str, s;
int k;

int method()
{
    int len= s.size(), res= 0;

    for(int i=0; i<=len-k; i++)
    {
        if(s[i]=='-')
        {
            res++;
            for(int j=i; j<i+k; j++)
            {
                if(s[j]=='-')
                    s[j]= '+';
                else
                    s[j]= '-';
            }
        }
    }

    for(int i=max(len-k, 0); i<len; i++)
    {
        if(s[i]=='-')
        {
            res= inf;
            break;
        }
    }

    return res;
}

int main()
{
    int t, cs= 0, res;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &t);
    while(t--)
    {
        cin>>str>>k;

        s= str;

        res= method();

        reverse(str.begin(), str.end());

        s= str;

        res= min(res, method());

        if(res==inf)
            printf("Case #%d: IMPOSSIBLE\n", ++cs);
        else
            printf("Case #%d: %d\n", ++cs, res);
    }

    return 0;
}
