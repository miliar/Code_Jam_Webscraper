#include <bits/stdc++.h>

using namespace std;

int test;
long long N,ans;
vector <long long> F;

void init()
{
    F.push_back(1);
    long long x = 1;
    for (int i=2; i <= 18; i++) x = (x*10)+1, F.push_back(x);
    reverse(F.begin(),F.end());
}

int main()
{
    freopen("googlejam.inp","r",stdin);
    freopen("googlejam.out","w",stdout);
    init();
    cin >> test;
    for (int t=1; t <= test; t++)
    {
        cout << "Case #" << t << ": ";
        cin >> N; ans = 0;
        int cur = 9;
        for (int i=0; i < F.size(); i++)
            while (cur)
            {
                if (ans + F[i] > N) break;
                ans += F[i]; cur--;
            }
        cout << ans << endl;
    }
}
