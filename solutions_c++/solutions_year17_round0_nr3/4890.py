#include <bits/stdc++.h>

using namespace std;

priority_queue<int> q;
void solve()
{
    bool chk = false;
    int n, k, L, R, N, cnt=1;
    scanf("%d %d", &n, &k);

    N = n-1;L = N/2;R = N-L;
    if(k == 1)
    {
        printf("%d %d\n", max(L, R), min(L, R));
        return ;
    }
    q.push(L);q.push(R);
    while(!q.empty())
    {
        for(int x=0; x<1; x++)
        {
            N = q.top()-1;q.pop();
            L = N/2;R = N-L;
            cnt++;
            q.push(L);q.push(R);

            if(cnt == k)
            {
                printf("%d %d\n", max(L, R), min(L, R));
                chk = true;
                break;
            }

        }
        if(chk)
            break;
    }
    while(!q.empty())
        q.pop();

}

int main()
{
    freopen("C-in.txt","r",stdin);
	freopen("C-out.txt","w",stdout);
    int T;
    scanf("%d", &T);
    for(int t=0; t<T; t++)
    {
        printf("Case #%d: ", t+1);
        solve();
    }
    return 0;
}
