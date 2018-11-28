#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("input.txt");
    ofstream cout("salida.txt");
    long long int t, t2 = 1, caballos, pos;
    double tiempo, distancia, velocidad, tmax;
    cin >> t;
    while(t2<=t)
    {
        tmax = 0;
        cin >> distancia >> caballos;
        //cout << distancia << " " << caballos << endl;
        while(caballos--)
        {
            cin >> pos >> velocidad;
            tiempo = (double)(distancia-pos)/velocidad;
            tmax = max(tmax,tiempo);
        }
        cout << "Case #" << t2++ << ": " << fixed << setprecision(6) << distancia/tmax << endl;
    }
    return 0;
}
