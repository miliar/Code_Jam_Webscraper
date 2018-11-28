#include<bits/stdc++.h>
typedef long long ll;
using namespace std;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int CNO = 1; CNO <= T; CNO++)
    {
        ll N, K;
        cin >> N >> K;
        map<ll, ll> freq;
        freq[N]++;
        while(K > 0)
        {
            auto i = freq.rbegin();
            while(i->second == 0)
                i++;
            if (i->second >= K)
                break;
            else
            {
                K -= i->second; 
                ll num = i->first;
                ll times = i->second; 
                if (num % 2)
                    freq[num/2] += times*2;
                else
                {
                    
                    if (num>1) freq[num/2] += times;
                    if (num>2) freq[num/2-1] += times;
                }
                freq[num] = 0;
            }
        }
        auto i = freq.rbegin();
        while(i->second == 0)
            i++;
        ll num = i->first;
        if (num % 2)
            printf("Case #%d: %lld %lld\n", CNO, num/2, num/2);
        else
            printf("Case #%d: %lld %lld\n", CNO, num/2, num/2-1);
    }
    return 0;
}