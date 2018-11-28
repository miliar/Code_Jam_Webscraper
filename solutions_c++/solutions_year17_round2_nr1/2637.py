#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

struct HORSE {
    long double speed;
    long long int dis;
} horse[1001];

int main(){
    int cases;
    int c_counter;
    long long int destination, horse_count;

    cin >> cases;
    for (int i = 1; i <= cases; i++) {
        cin >> destination >> horse_count;
        long double max_hr = 0.0;
        for (int j = 0; j < horse_count; j++) {
            cin >> horse[j].dis >> horse[j].speed;
            max_hr = max ( max_hr, ((destination-horse[j].dis) / horse[j].speed));
        }
        long double ans = destination / max_hr;
        // cout << ans << endl;
        printf("Case #%d: %.6Lf\n",i,ans);

    }
}
