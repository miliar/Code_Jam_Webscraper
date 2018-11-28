#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    cout << setprecision(6) << fixed;
    int d, n;
    for(int j = 1; j<=t; j++){
        cin >> d;
        cin >> n;
        double temp = 0;
        for(int i = 0; i<n; i++){
            int k, s;
            cin >> k;
            cin >> s;
            double time = (double)(d-k)/(double)s;
            if(time > temp)
                temp = time;
        }
        double res = (double)d/temp;
        cout << "Case #"<< j << ": "<< res << "\n";
    }
    return 0;
}
