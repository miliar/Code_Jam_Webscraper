#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;
const double PI = acos(-1);

int main()
{
    ios_base::sync_with_stdio(false);
    int Testcase;
    cin >> Testcase;
    for(int tc=1;tc<=Testcase;tc++) {
        int N, K;
        cin >> N >> K;
        vector<pair<long long,int>> R, H;
        vector<pair<long long,long long>> pan;
        for(int i=0;i<N;++i) {
            long long r, h;
            cin >> r >> h;
            R.emplace_back(r*r, i);
            H.emplace_back(2*r*h, i);
            pan.emplace_back(r*r, 2*r*h);
        }
        sort(R.rbegin(), R.rend());
        sort(H.rbegin(), H.rend());
        long long ans = 0;
        for(int i=0;i<N;++i) {
            int tmp = 1;
            long long nulbi = R[i].first + pan[R[i].second].second;
            for(int j=0; j<N && tmp<K; ++j) {
                if(R[i].second!=H[j].second && R[i].first >= pan[H[j].second].first) {
                    nulbi += H[j].first;
                    tmp++;
                }
            }
            if(tmp == K) {
                ans = max(ans, nulbi);
            }
        }
        cout << "Case #" << tc << ": " << setprecision(10) << fixed << (double)(ans*PI) << '\n';
    }
    return 0;
}
