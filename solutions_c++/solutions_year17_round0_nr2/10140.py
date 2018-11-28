#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
    int tc, tt = 1;
    cin >> tc;
    while(tt <= tc) {
        long long num, ans = 0;
        cin >> num;
        while(1) {
            long long n = num;
            vector<int> v;
            while(n != 0) {
                v.push_back(n%10);
                n = n/10;
            }
            vector<int> v1 = v;
            sort(v1.rbegin(), v1.rend());
            if(v == v1) {
                ans = num;
                break;
            }
            num--;
        }
        cout << "Case #" << tt <<": " << ans << "\n";
        tt++;
    }
    return 0;
}
