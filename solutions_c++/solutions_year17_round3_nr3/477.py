#include <bits/stdc++.h>
using namespace std;

typedef long double rl;

const int MX=59;

int N, K;
rl U;
rl P[MX];

const rl EPS=1E-9;

rl solve()
{
    if(N!=K) return -1337;

    map<double, int> M;
    for(int i=0; i<N; i++) M[P[i]]++;

    sort(P, P+N);

    while(U>EPS)
    {
        cerr << U << ' ' << M.begin()->first << endl;

        if(M.size()==1)
        {
            rl p=M.begin()->first;
            return pow(p+U/N, N);
        }
        else
        {
            cerr << "HERE" << endl;

            rl p1=M.begin()->first;
            rl p2=(++M.begin())->first;
            rl k=M.begin()->second;
            M.erase(M.begin());

            cerr << p1 << ' ' << p2 << endl;

            if((p2-p1)*k>U)
            {
                rl pp=p1+U/k;
                M[pp]=k;

                U=0.0;
                break;
            }
            else
            {
                M[p2]+=k;
                U-=(p2-p1)*k;
            }
        }
    }

    rl prob=1.0;
    for(auto bla: M)
    {
        for(int i=0; i<bla.second; i++)
        {
            prob*=bla.first;
        }
    }
    return prob;
}


int main()
{
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    cout << setprecision(20);

    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        //int N;
        //cin >> N;
        //int result=solve(N);
        cin >> N >> K;
        cin >> U;
        for(int i=0; i<N; i++) cin >> P[i];
        rl ans=solve();
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
