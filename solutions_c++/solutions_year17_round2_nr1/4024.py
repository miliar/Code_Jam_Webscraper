#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i = 0; i < t; i++)
    {
        int n;
        double d, k[n], s[n], h[n];
        cin >> d >> n >> k[0] >> s[0];
        h[0] = (d - k[0]) / s[0];
        int max = 0;
        for(int j = 1; j < n; j++)
        {
            cin >> k[j] >> s[j];
            h[j] = (d - k[j]) / s[j];
            if(h[j] > h[max] && k[max] + h[max] * s[max] >= k[j] + h[j] * s[j])
                max = j;
        }
        std::cout << "Case #" << i + 1 << ": " << std::fixed << std::setprecision(6) << d / h[max] << "\n";
    }
    return 0;
}
