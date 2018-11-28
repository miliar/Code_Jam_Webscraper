#include <iostream>
#include <string>
#include <iomanip>      // std::setprecision
using namespace std;

int main()
{
    int T;
    cin >> T;
    int D, N, Nidx;
    int K, S;
    double MaxMinSpeed, NewMMS;
    for (int Tidx=0; Tidx<T; Tidx++) {
       cin >> D >> N;
       MaxMinSpeed = 1e15;
       for (Nidx=0;Nidx<N;Nidx++) {
            cin >> K >> S;

            if (MaxMinSpeed<S)
                continue;
            else {
                NewMMS = double(D)/double(D-K)*double(S);
                if (NewMMS<MaxMinSpeed)
                    MaxMinSpeed = NewMMS;
            }
       }

       cout << "Case #" << Tidx+1 << ": ";
       cout << fixed;
       cout << setprecision(6) << MaxMinSpeed;
       cout << endl;
    }

    return 0;
}
