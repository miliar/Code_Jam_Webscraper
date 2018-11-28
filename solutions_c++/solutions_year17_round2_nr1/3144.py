#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int t, n;
    long double s, k, d, tempo, ultimo, velocidade;
    cin >> t;
    for(int a=1; a<=t; a++){
        cin >> d >> n;
        ultimo = 0;
        for(int b=0; b<n; b++){
            cin >> k >> s;
            tempo = (d - k)/s;
            if (tempo > ultimo)
                ultimo = tempo;
        }
        velocidade = d / ultimo;
        cout << "Case #" << a << ": " << fixed << setprecision(6) << velocidade << endl;
    }
    return 0;
}
