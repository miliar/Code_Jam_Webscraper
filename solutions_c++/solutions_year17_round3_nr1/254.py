#include <iostream>
#include <bits/stdc++.h>

const long double PI = 3.14159265359;

using namespace std;
typedef long long ll;

int main()
{
    ifstream cin("in.in");
    ofstream cout("out.out");
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        int N, K;
        cin >> N >> K;
        pair<ll,ll> P[N];
        for (int i = 0; i < N; i++)
        {
            cin >> P[i].first >> P[i].second;
        }
        sort(P, P+N);
        ll vs = 0;
        priority_queue<ll> faces;
        ll R = 0;
        for (int i = 0; i < N; i++)
        {
            ll s = P[i].second*P[i].first*2;
            ll t = P[i].first*P[i].first;
            if (faces.size() == K-1)
            {

                ll c = vs + s + t;
                cerr << c << endl;
                R = max(R, c);
            }
            vs += s;
            faces.push(-s);
            if (faces.size() >= K)
            {
                vs += faces.top(); faces.pop();
            }
        }
        cout << "Case #" << t+1 << ": " << setprecision(20) << (long double)R*PI << endl;
    }
}
