#include <bits/stdc++.h>
using namespace std;

string S;

char flip(char x)
{
    if(x=='-')
        return '+';

    return '-';
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output4.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int test=1; test<=T; test++)
    {
        int K;
        cin >> S >> K;

        int ans = 0;

        for(int i=0; i+K-1<S.size(); i++)
        {
            if(S[i]=='-')
            {
                ans++;

                for(int j=0; j<K; j++)
                    S[i+j] = flip(S[i+j]);
            }
        }

        for(int i=0; i<S.size(); i++)
            if(S[i]=='-')
                ans = -1;

        if(ans==-1)
            printf("Case #%d: IMPOSSIBLE\n", test);
        else
            printf("Case #%d: %d\n", test, ans);
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
