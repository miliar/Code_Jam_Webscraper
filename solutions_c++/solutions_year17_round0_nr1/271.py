#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);
    ios::sync_with_stdio(false);
    int tc;
    cin >> tc;
    for(int case_no=1; case_no<=tc; case_no++)
    {
        printf("Case #%d: ", case_no);
        string s;
        int K;
        cin >> s >> K;
        int n = s.size();

        int nb_switches=0;
        for(int i=n-1; i-K+1>=0; i--)
        {
            if(s[i]=='-')
            {
                nb_switches++;
                for(int j=0; j<K; j++)
                {
                    if(s[i-j]=='-') s[i-j]='+';
                    else s[i-j]='-';
                }
            }
        }
        bool all_plus=true;
        for(int i=0; i<n; i++)
        {
            if(s[i] != '+')
            {
                all_plus=false;
                break;
            }
        }
        if(!all_plus)
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            printf("%d\n", nb_switches);
        }
    }
    return 0;
}
