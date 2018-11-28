#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

string s;

int main ()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, n, i, j, k;
    cin >> t;
    int cs=0;
    while (t--)
    {
        cs++;
        cin >> s;
        n = s.size();
        if (n==1)
        {
            printf("Case #%d: %c\n", cs, s[0]);
            continue;
        }
        int flag=0;
        printf("Case #%d: ", cs);
        for (i=0; i<n-1; i++)
        {
            if (s[i]>s[i+1])
            {
                char ch = s[i];
                j = i;
                while (j>=0 && s[j]==ch)
                {
                    j--;
                }
                if (j==-1)
                {
                    if (s[0]=='1')
                    {
                        for (int k=0; k<n-1; k++)
                        {
                            printf("9");
                        }
                        printf("\n");
                        flag=1;
                        break;
                    }
                    else
                    {
                        int now = s[0]-'0';
                        now--;
                        printf("%d", now);
                        for (int k=0; k<n-1; k++)
                        {
                            printf("9");
                        }
                        printf("\n");
                        flag=1;
                        break;
                    }
                }
                else
                {
                    for (int k=0; k<=j; k++)
                    {
                        printf("%c", s[k]);
                    }
                    int now = s[j+1]-'0';
                    now--;
                    printf("%d", now);
                    for (int k=j+2; k<n; k++)
                    {
                        printf("9");
                    }
                    printf("\n");
                    flag=1;
                    break;
                }
            }
        }
        if (flag) continue;
        cout << s << endl;
    }












    return 0;
}
