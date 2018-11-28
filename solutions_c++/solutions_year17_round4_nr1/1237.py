#include <bits/stdc++.h>
using namespace std;
#define D(x) cerr<<#x " = "<<(x)<<endl
#define pb push_back
#define ff first
#define ss second
#define mem(a) memset(a,0,sizeof(a))
#define _set(a) memset(a,-1,sizeof(a))
typedef long long int ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
#define eps 1e-9
#define MAX 100000
#define MAXL 20
#define MAXE 100000
#define inf (1<<30)
//ll mod = 1000000000+7;
//int dx[] = {0,0,1,-1};
//int dy[] = {1,-1,0,0};
//int dx[] = {-1,-1,-1,0,0,1,1,1};
//int dy[] = {-1,0,1,-1,1,-1,0,1};

int ar[105];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    //ios_base::sync_with_stdio(false);
    int ncase, tcase = 1, n, p, i, j, k, l;
    scanf("%d", &ncase);
    while(ncase--)
    {
        scanf("%d %d", &n, &p);
        for(i = 0; i < n; i++)
        {
            scanf("%d", &ar[i]);
        }
        sort(ar, ar+n);
        int ans = 0;
        for(i = 0; i < n; i++)
        {
            if(ar[i]%p == 0)
            {
                ar[i] = 0;
                ans++;
            }
        }
        for(i = 0, j = 0; i < n; i++)
        {
            if(ar[i]) ar[j++] = ar[i];
        }
        n = j;
        for(i = 0; i < n; i++)
        {
            if(ar[i] == 0) continue;
            for(j = i+1; j < n; j++)
            {
                if(ar[j] == 0) continue;
                if((ar[i]+ar[j])%p == 0)
                {
                    ar[i] = 0;
                    ar[j] = 0;
                    ans++;
                }
            }
        }
        for(i = 0, j = 0; i < n; i++)
        {
            if(ar[i]) ar[j++] = ar[i];
        }
        n = j;
        for(i = 0; i < n; i++)
        {
            if(ar[i] == 0) continue;
            for(j = i+1; j < n; j++)
            {
                if(ar[j] == 0) continue;
                for(k = j+1; k < n; k++)
                {
                    if(ar[k] == 0) continue;
                    if((ar[i]+ar[j]+ar[k])%p == 0)
                    {
                        ar[i] = 0;
                        ar[j] = 0;
                        ar[k] = 0;
                        ans++;
                    }
                }
            }
        }
        for(i = 0, j = 0; i < n; i++)
        {
            if(ar[i]) ar[j++] = ar[i];
        }
        n = j;
        for(i = 0; i < n; i++)
        {
            if(ar[i] == 0) continue;
            for(j = i+1; j < n; j++)
            {
                if(ar[j] == 0) continue;
                for(k = j+1; k < n; k++)
                {
                    if(ar[k] == 0) continue;
                    for(l =k+1; l < n; l++)
                    {
                        if(ar[l] == 0) continue;
                        if((ar[i]+ar[j]+ar[k]+ar[l])%p == 0)
                        {
                            ar[i] = 0;
                            ar[j] = 0;
                            ar[k] = 0;
                            ar[l] = 0;
                            ans++;
                        }
                    }
                }
            }
        }
        for(i = 0, j = 0; i < n; i++)
        {
            if(ar[i]) ar[j++] = ar[i];
        }
        n = j;
        if(n) ans++;
        printf("Case #%d: %d\n", tcase++, ans);
    }
    return 0;
}



