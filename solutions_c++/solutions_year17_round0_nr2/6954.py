#include <algorithm>
#include <iostream>

using namespace std;


void solve()
{
    char s[20];
    scanf("%s", s);
    int len = strlen(s);
    if(len == 1) goto end;
    int i = 0;
    while(i < len - 1 && s[i] <= s[i+1] ) ++i;
    if (i == len - 1) goto end;
    while(i > 0 && s[i] == s[i - 1]) --i;
    s[i++]--;
    while(i < len) s[i++] = '9';
end:
    unsigned long long n;
    sscanf(s, "%llu", &n);
    printf("%llu\n", n);
}

int main(int argc, char* argv[])
{
#ifdef LOCAL_JAM
    freopen("B-large.in", "r", stdin);
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

