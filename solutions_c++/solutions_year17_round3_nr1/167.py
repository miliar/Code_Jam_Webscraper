#include <bits/stdc++.h>
using namespace std;

vector< pair<int, int> > X;
priority_queue<long long, vector<long long>, greater<long long> > Q;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output2.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int test=1; test<=T; test++)
    {
        int N, K;
        scanf("%d %d", &N, &K);

        X.clear();

        while(!Q.empty())
            Q.pop();

        for(int i=1; i<=N; i++)
        {
            int r, h;
            scanf("%d %d", &r, &h);

            X.push_back({r, h});
        }

        sort(X.begin(), X.end());

        long double ans = 0;
        long double pi = acos((long double)-1);

        long long pro = 0;

        for(int i=0; i<K-1; i++)
        {
            pro += (long long)X[i].first*X[i].second;
            Q.push((long long)X[i].first*X[i].second);
        }

        for(int i=K-1; i<X.size(); i++)
        {
            pro += (long long)X[i].first*X[i].second;
            int radius = X[i].first;
            ans = max(ans, pi*radius*radius + pi*2*pro);

            Q.push((long long)X[i].first*X[i].second);

            pro -= Q.top();
            Q.pop();
        }

        printf("Case #%d: ", test);
        cout << fixed << setprecision(9) << ans << "\n";
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
