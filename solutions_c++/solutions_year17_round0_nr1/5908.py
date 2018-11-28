#include <bits/stdc++.h>
using namespace std;
char cake[1005];
bool cnt[1005];
int main()
{
    int T, s, n, ans;
    //ofstream fout("Output.txt");
    char c;
    scanf("%d", &T);
    getchar();
    for(int i = 1 ; i <= T ; i++)
    {
        n = 0;
        while((c = getchar()) != ' ')
        {
            cake[n] = c;
            if(c == '+') cnt[n] = 1;
            else cnt[n] = 0;
            n++;
        }
        scanf("%d", &s);
        getchar();
        ans = 0;
        for(int i = 0 ; i <= n-s ; i++)
        {
            if(!cnt[i])
            {
                ans++;
                for(int j = i ; j < s+i ; j++) cnt[j] = !cnt[j];
            }
        }
        for(int i = n-s+1 ; i < n ; i++) if(!cnt[i]) ans = -1;
        printf("Case #%d: ", i);
        //fout << "Case #" << i << ": ";
        if(ans == -1) printf("IMPOSSIBLE\n"); //fout << "IMPOSSIBLE\n";}
        else printf("%d\n", ans);//fout << ans << "\n";}
    }
    return 0;
}
