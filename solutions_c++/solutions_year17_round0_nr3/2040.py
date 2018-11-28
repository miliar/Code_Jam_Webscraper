#include <bits/stdc++.h>

using namespace std;

int test;
long long N,K;
set <long long, greater<long long> > seta;
map <long long, long long> mapa;

void solve(long long N, long long K)
{
    seta.clear(); mapa.clear();
    mapa[N] = 1; seta.insert(N);
    while (K)
    {
        long long x = *seta.begin();
        seta.erase(x);
        if (K <= mapa[x])
        {
            cout << x/2 << " " << (x-1)/2 << endl;
            return;
        }
        seta.insert(x/2); seta.insert((x-1)/2);
        mapa[x/2] += mapa[x];
        mapa[(x-1)/2] += mapa[x];
        K -= mapa[x];
    }
}

int main()
{
    freopen("googlejam.inp","r",stdin);
    freopen("googlejam.out","w",stdout);
    cin >> test;
    for (int t=1; t <= test; t++)
    {
        cout << "Case #" << t << ": ";
        cin >> N >> K;
        solve(N,K);
    }
}
