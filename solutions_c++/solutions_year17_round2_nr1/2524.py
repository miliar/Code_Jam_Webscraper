#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int k = 0; k < T; k++)
    {
        double D;
        int N;
        cin >> D >> N;
        double velocity;
        double K;
        double S;
        cin >> K >> S;
        double time = (D-K)/S;
        double aux;
        for (int i = 1; i < N; i++)
        {
            cin >> K >> S;
            aux = (D-K)/S;
            if (aux > time)
                time = aux;
        }
        cout << "Case #" << k+1 << ": ";
        aux = D/time;
        printf("%f\n",aux);
    }
    return 0;
}
