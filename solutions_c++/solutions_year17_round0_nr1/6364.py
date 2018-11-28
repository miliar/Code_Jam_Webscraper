#include <map>
#include <set>
#include <stack>
#include <cmath>
#include <queue>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define maxn  100000+10
#define FOR(i, j, k) for(int i = j;i<= k;i++)
char s[1010];
int main(){
    freopen("/Users/hermione/Desktop/in.txt","r",stdin);
    freopen("/Users/hermione/Desktop/temp.txt", "w", stdout);
    int T;
    cin>>T;
    FOR(z, 1, T){
        int k;
        scanf("%s%d", s, & k);
        int n = strlen(s);
        int ans = 0;
        FOR(i, 0, n-1)
        {
            if(s[i] == '-')
            {
                if(ans != -1)
                    ans ++;
                FOR(j, 0 ,k-1)
                {
                    if(i+j < n)
                    {
                        if(s[i+j] == '-')
                            s[i+j] ='+';
                        else s[i+j] ='-';
                    }
                    else ans = -1;
                }
            }
        }
        printf("Case #%d: ", z);
        if(ans== -1)printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}