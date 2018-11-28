#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct stru{
    long double dist;
    long double speed;
};

int main()
{
    cout.precision(30);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        long double d,n;
        long double ans;
        cin >> d >> n;
        vector<stru> A;
        vector<long double> times;
        stru horse;
        for (int i = 0; i < n; i++){
            cin >> horse.dist;
            cin >> horse.speed;
            times.push_back((d-horse.dist)/horse.speed);
            A.push_back(horse);
        }
        sort(times.begin(),times.end());
        ans = d/times[n-1];
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
