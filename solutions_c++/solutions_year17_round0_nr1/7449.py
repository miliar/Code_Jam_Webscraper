#include        <bits/stdc++.h>

using           namespace       std;

#define         trace1(x)       cout << #x << " = " << x << '\n';
#define         trace2(x,y)     cout << #x << " = " << x << " | " << #y << " = " << y << '\n';
#define         trace3(x,y,z)   cout << #x << " = " << x << " | " << #y << " = " << y << " | " << #z << " = " << z << '\n';

typedef         long long       ll;
typedef         vector<int>     vi;
typedef         pair<int, int>  pi;
typedef         map<int, int>   mp;

const int N = 1e6 + 5;
const int MOD = 1e9 + 7;
const long long inf = 1e15 + 1;
const long double eps = pow(2, -32);

int main()
{
        freopen("INPUT.txt", "r", stdin);
        freopen("ANSWER.txt", "w", stdout);
        int t, k, tests = 1;
        string s;
        scanf("%d", &t);
        while(t--)
        {
                cin >> s >> k;
                int ans = 0;
                int len = s.length();
                for(int i = 0; i < len-k+1; i++)
                {
                        if(s[i] == '-')
                        {
                                ans++;
                                for(int j = i; j < i+k; j++)
                                {
                                        if(s[j] == '-')s[j] = '+';
                                        else s[j] = '-';
                                }
                        }
                }
                for(int i = 0; i < len; i++)if(s[i] == '-')ans = -1;
                if(ans == -1)printf("Case #%d: IMPOSSIBLE\n", tests++);
                else printf("Case #%d: %d\n", tests++, ans);
        }
        return 0;
}
