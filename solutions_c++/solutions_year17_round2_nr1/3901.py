#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    int cases, d, n;
    double pos, speed;
    double maxTime, t;
    ifstream cin;
    ofstream cout;
    cin.open("large.in");
    cout.open("large.out");
    cin >> cases;
    for (int i = 1; i <= cases; i++) {
        maxTime = 0;
        cin >> d >> n;
        for (int j = 0; j < n; j++) {
            cin >> pos >> speed;
            t = (d - pos) / speed;
            if (t > maxTime) {
                maxTime = t;
            }
        }
        cout << "Case #" << i << ": " << fixed << setprecision(6) << d / maxTime << endl;
    }
    cin.close();
    cout.close();
    return 0;
}
