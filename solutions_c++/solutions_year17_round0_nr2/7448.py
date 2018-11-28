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

bool check(ll x)
{
        int mini = x%10;
        while(x)
        {
                int temp = x % 10;
                if(temp > mini)return false;
                mini = min(temp, mini);
                x /= 10;
        }
        return true;
}
ll fun(ll x)
{
        for(ll i = x; i >= 0; i--)
        {
               ll temp = i;
               if(check(temp))return i;
        }
}
bool ok(char s[])
{
        int len = strlen(s);
        for(int i = 0; i < len-1; i++)
                if(s[i] > s[i+1])
                        return false;
        return true;
}
int main()
{
        freopen("INPUT.txt", "r", stdin);
        freopen("ANSWER.txt", "w", stdout);
        int t, tests = 1;
        scanf("%d", &t);
        while(t--)
        {
                ll x = 0;
                char s[105];
                scanf("%s", s);
                int len = strlen(s);

                while(!ok(s))
                {
                        int in = 100;
                        for(int i = 1; i < len; i++)
                        {
                                if(s[i] < s[i-1])
                                {
                                        in = i;
                                        break;
                                }
                        }
                        for(int i = in; i < len; i++)s[i] = '9';
                        s[in-1]--;
                }
                int index;
                for(int i = 0; i < len; i++)
                {
                        if(s[i] != '0')
                        {
                                index = i;
                                break;
                        }
                }
                printf("Case #%d: ", tests++);
                for(int i = index; i < len; i++)printf("%c", s[i]);
                printf("\n");
        }
        return 0;
}
