#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);
    ios::sync_with_stdio(false);
    int tc;
    cin >> tc;
    for(int case_no=1; case_no<=tc; case_no++)
    {
        cerr << "Case " << case_no << " solved" << endl;
        printf("Case #%d: ", case_no);
        long long N, K;
        cin >> N >> K;
        map<long long, long long> ma;
        ma[N]=1LL;

        long long min_dist;
        long long max_dist;

        int debug_max=-1;
        while(true)
        {
            debug_max=max(debug_max, (int)ma.size());
            auto it = ma.end();
            it--;
            long long space = it->first;
            long long amount = it->second;
            //cerr << space << " " << amount << " " << K << endl;
            ma.erase(it);
            if(amount >= K)
            {
                min_dist=(space+1)/2;
                max_dist=(space+2)/2;
                break;
            }
            else
            {
                ma[(space-1)/2] += amount;
                ma[space/2] += amount;
                K -= amount;
            }
        }
        cerr << "debug_max: " << debug_max << endl;
        min_dist--;
        max_dist--;
        printf("%lld %lld\n", max_dist, min_dist);
    }
    return 0;
}
