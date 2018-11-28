#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int tc = 1; tc <= T; ++tc){
        int N;
        double D;
        cin >> D >> N;
        double mn = 1e14;
        double K, S;
        for(int i = 0; i < N; ++i){
            cin >> K >> S;
            mn = min(mn, D / ((D - K) / S));
        }
        cout << fixed;
        cout << "Case #" << tc << ": " << mn << endl;
    }
}
