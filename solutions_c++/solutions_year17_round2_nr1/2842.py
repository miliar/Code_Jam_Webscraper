#include<bits/stdc++.h>

using namespace std;
int count1 ;
void solve()
{
    count1++;
    long long int d,k;
    int n,s;
    double max = 0;
    cin >> d >> n;
    for(int i=0;i<n;i++)
    {
        cin >> k >> s;
        if((double)(d-k)/s > max)
            max = (double)(d-k)/s;

    }
     cout << fixed;
    cout << setprecision(6);
    cout << "Case #" <<count1 <<": " << (double)d/max << endl;
}
int main()
{
    count1 = 0;
    int t;
    cin >> t;
    while(t--)
        solve();
}
