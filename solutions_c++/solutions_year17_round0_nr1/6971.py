#include <algorithm>
#include <iostream>

using namespace std;

int k, len;
char s[1001];

inline void flip(int pos)
{
    for(int i = pos; i < min(len, pos + k); ++i)
        s[i] = s[i] == '+' ? '-' : '+';
}

void solve()
{
    scanf("%s", s);
    scanf("%d", &k);
    len = strlen(s);
    int count = 0;
    for(int i = 0; i < len - k + 1; ++i)
    {
        if(s[i] == '-')
        {
            flip(i);
            count++;
        }
    }
    
    bool valid = true;
    for(int i = 0; i < len; ++i)
    {
        if(s[i] == '-')
        {
            valid = false;
            break;
        }
    }
    if(!valid)
        printf("IMPOSSIBLE\n");
    else
        printf("%d\n", count);
}

int main(int argc, char* argv[])
{
#ifdef LOCAL_JAM
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int T;
    scanf("%d", &T);
    for(int i = 0; i < T; ++i)
    {
        printf("Case #%d: ", i+1);
        solve();
    }
}

