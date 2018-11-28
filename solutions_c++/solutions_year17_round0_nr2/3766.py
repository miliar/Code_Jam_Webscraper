#include<bits/stdc++.h>
using namespace std;

int main()
{

    int t;
    cin >> t;
    for(int T = 1; T <= t; T++)
    {
        long long n;
        cin >> n;
        long long ans = 0;
        for(int i = 1; i <= 9; i++)
        {
            long long plus = (long long)1;
            for(int j = 0; j < 18; j++)
            {
                if(ans + plus <= n) ans += plus;
                else break;
                plus *= 10;
            }
        }
        cout << "Case #" << T << ": ";
        cout << ans << endl;
    }
}
