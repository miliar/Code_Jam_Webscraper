#include <bits/stdc++.h>

using namespace std;

int N, P;
int A[4];
vector<vector<int>> rules[5];
map<vector<int>, int> cache;

int rec(vector<int> state)
{
    if(cache.count(state))
        return cache[state];
    int& ret=cache[state];
    vector<int> nstate;
    for(auto& v: rules[P])
    {
        for(int i=0; i<P-1; i++) if(v[i]>state[i])
            goto bad;
        nstate=state;
        for(int i=0; i<P-1; i++)
            nstate[i]-=v[i];
        ret=max(ret, 1+rec(nstate));
        bad:;
    }
    return ret;
}

void _main(int TEST)
{
    scanf("%d%d", &N, &P);
    for(int i=0; i<P; i++)
        A[i]=0;
    int a;
    for(int i=0; i<N; i++)
        scanf("%d", &a), A[a%P]++;
    int s=0;
    for(int i=0; i<P; i++)
        s+=i*A[i];
    int ans=1;
    if(s%P==0)
        ans--;
    ans+=A[0];
    cache.clear();
    vector<int> init;
    for(int i=1; i<P; i++)
        init.push_back(A[i]);
    printf("%d\n", ans+rec(init));
}

int main()
{
    int P=2;
    for(int i=0; i<=P; i++) if(i && 1*i%P==0)
        rules[2].push_back({i});
    P=3;
    for(int i=0; i<=P; i++) for(int j=0; j<=P; j++) if((i || j) && (1*i+2*j)%P==0)
        rules[3].push_back({i, j});
    P=4;
    for(int i=0; i<=P; i++) for(int j=0; j<=P; j++) for(int k=0; k<=P; k++) if((i || j || k) && (1*i+2*j+3*k)%P==0)
        rules[4].push_back({i, j, k});
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
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
