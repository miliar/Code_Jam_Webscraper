#include <bits/stdc++.h>

using namespace std;

int N, P;
int A[50];
int B[50][50];
vector<pair<int, int>> V[50];
multiset<int> S[50];

int maxi(int x, int a)
{
    int lo=0, mid, hi=2000000;
    while(lo<hi)
    {
        mid=(lo+hi+1)/2;
        if(9LL*a*mid<=10LL*x)
            lo=mid;
        else
            hi=mid-1;
    }
    return lo;
}

int mini(int x, int a)
{
    int lo=0, mid, hi=2000000;
    while(lo<hi)
    {
        mid=(lo+hi)/2;
        if(10LL*x<=11LL*a*mid)
            hi=mid;
        else
            lo=mid+1;
    }
    return lo;
}

void _main(int TEST)
{
    scanf("%d%d", &N, &P);
    for(int i=0; i<N; i++)
        scanf("%d", A+i);
    for(int i=0; i<N; i++)
    {
        V[i].clear();
        S[i].clear();
        for(int j=0; j<P; j++)
        {
            scanf("%d", B[i]+j);
            int l=mini(B[i][j], A[i]), r=maxi(B[i][j], A[i]);
            if(l<=r)
                V[i].push_back({l, r});
        }
        sort(V[i].rbegin(), V[i].rend());
    }
    int ans=0;
    while(1)
    {
        int idx=-1;
        for(int i=0; i<N; i++) if(!V[i].empty() && (idx==-1 || V[i].back().first<V[idx].back().first))
            idx=i;
        if(idx==-1)
            break;
        int t=V[idx].back().first;
        S[idx].insert(V[idx].back().second);
        V[idx].pop_back();
        bool ok=true;
        for(int i=0; i<N; i++)
        {
            while(!S[i].empty() && *S[i].begin()<t)
                S[i].erase(S[i].begin());
            if(S[i].empty())
                ok=false;
        }
        if(ok)
        {
            for(int i=0; i<N; i++)
                S[i].erase(S[i].begin());
            ans++;
        }
    }
    printf("%d\n", ans);
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        //cerr << i << endl;
        printf("Case #%d: ", i);
        _main(i);
    }
    return 0;
}
