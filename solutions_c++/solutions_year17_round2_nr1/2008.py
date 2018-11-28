#include <iostream>
#include <iomanip>

using namespace std;

typedef unsigned long long ull;

int main()
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i)
    {
        double arrivalTime = -1;
        ull D, N;
        cin >> D >> N;
        for(ull j = 0; j < N; ++j)
        {
            ull K, S;
            cin >> K >> S;
            if(K < D)
            {
                double tTime = (double(D - K))/S;
                arrivalTime = tTime > arrivalTime ? tTime : arrivalTime;
            }
        }
        cout << "Case #" << i << ": " << setprecision(7) << D/arrivalTime << '\n';
    }
    return 0;
}
