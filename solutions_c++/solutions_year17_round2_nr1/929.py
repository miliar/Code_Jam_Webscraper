#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int test = 1;test<=t;test++)
    {
        long long  D,N;
        cin >> D >> N;

        long long K[N];
        long long S[N];
        for(int i = 0;i<N;i++)
        {
            cin >> K[i] >> S[i];
        }

        double T = 0;
        for(int i = 0;i<N;i++)
        {
            T = max(T,(D-K[i] + 0.0) / S[i]);
        }

        double answer = D/T;
        cout << "Case #" << test << ": " << setprecision(15) << answer << endl;
    }
}
