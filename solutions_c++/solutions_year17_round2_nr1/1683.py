#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
using namespace std;

pair<int, int> horses[1000];
int main()
{
    int T;cin>>T;
    for(int TT = 1; TT <= T; ++TT)
    {
        printf("Case #%d: ", TT);
        int D, N; cin>>D>>N;
        for (int i = 0; i < N; ++i)
        {
            cin>>horses[i].first>>horses[i].second;
        }
        sort(horses, horses+N, greater<pair<int, int> >());
        double ans = 0;
        for (int i = 0; i < N; ++i)
        {
            ans = max(ans, (D - horses[i].first)*1.0 / horses[i].second);
        }
        printf("%.6f\n", D/ans);
    }
    return 0;
}