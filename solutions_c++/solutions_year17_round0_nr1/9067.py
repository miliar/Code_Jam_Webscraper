#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve(string s, int k)
{
        int i, j, res = 0, flag = 1;

        for(i=0; i<=s.length()-k; i++)
        {
            if(s[i]=='-')
            {
            //    cout<<i<<endl;
                res++;

                for(j=i; j<i+k; j++)
                {
                    if(s[j]=='-')   s[j]='+';
                    else s[j]='-';
                }
            }
        }

     //   cout<<s<<endl;
        for(i=0; i<s.length(); i++)
        {
            if(s[i]=='-')   flag = 0;
        }

        if(flag==0) puts("IMPOSSIBLE");
        else cout<<res<<endl;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.txt", "w", stdout);
    int test, cs = 0;

    scanf("%d", &test);

    while(test--)
    {
        string s;

        int k;

        cin>>s;

        cin>>k;
        printf("Case #%d: ", ++cs);

        solve(s, k);
    }

}
/*
1
---+-++- 3
*/
