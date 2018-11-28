#include<bits/stdc++.h>
#define FILL(arr,n)memset((arr),n,sizeof((arr)))
typedef long long ll;
using namespace std;
const int MAXN = 100007;
bool arr[MAXN];
int l[MAXN], r[MAXN];
ll N,K;
int pos = 0;
int minp = N + 1;
int maxq = 0;
int findPos()
{
    FILL(l, 0);
    FILL(r, 0);
    int lp = 0;
    for(int i=1;i<=N;i++)
    {
        if(arr[i])
        {
            lp = i;
        }
        l[i] = i - lp - 1;
    }
    int rp = N+1;
    for(int i=N;i>=1;i--)
    {
        if(arr[i])
        {
            rp = i;
        }
        r[i] = rp - i - 1;
    }

    pos = 0;
    minp = 0;
    maxq = 0;
    for(int i=1;i<=N;i++)
    {
        if(!arr[i])
        {
            int ma = min(l[i], r[i]);
            int mb = max(l[i], r[i]);
            if(ma > minp)
            {
                minp = ma;
                maxq = mb;
                pos = i;
            }
            else if(ma == minp)
            {
                if(mb > maxq)
                {
                    minp = ma;
                    maxq = mb;
                    pos = i;
                }
            }
        }
    }
    return pos;
}
int main()
{
    ll t,cas=0;
    cin >> t;
    while(t--)
    {
        cin >> N >> K;
        FILL(arr, 0);
        arr[0] = true;
        arr[N+1] = true;
        for(int i=1;i<=K-1;i++)
        {
            int pos = findPos();
            arr[pos] = true;
        }
        findPos();
        cout<<"Case #"<<++cas<<": "<<maxq <<" "<<minp << endl;
    }
    return 0;
}
