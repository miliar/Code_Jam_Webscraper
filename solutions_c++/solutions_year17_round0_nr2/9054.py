#include <iostream>
#include <math.h>
#include <vector>
#include <c++/algorithm>

using namespace std;
bool isValid(vector<int>res) {
    for (int i = 1 ;i<res.size(); i++)
        if (res[i] <res[i-1])
            return false;
    return true;
}
int main() {
    freopen("C:\\Users\\Administrator\\Downloads\\B-small-attempt2.in","r",stdin);
    freopen("C:\\Users\\Administrator\\Downloads\\B-small-attempt2.out","w",stdout);
    int num;
    cin >> num;
    long long k;
    long long temp;
    vector<int> res;
    for (int m=0; m<num; m++) {
        cin >> k;
        temp = k;
        cout << "Case #" << m+1 << ": ";
        if (k<10)  cout << k << endl;
        else {
            int maxs = 9;
            res.clear();
            while (k) {
                res.push_back(k%10);
                k /= 10;
            }
            reverse(res.begin(), res.end());
            while (!isValid(res)) {
                for (int i = 1; i < res.size(); i++) {
                    if (res[i]< res[i-1]) {
                        for (int j = i; j<res.size(); j++)
                            res[j] = 9;
                        res[i-1]--;
                    }
                }
            }

            long long ans = 0;
            for (int i=0; i<res.size(); i++)
                ans = ans*10 + res[i];
//            if (ans == 0 && temp>10)
//                ans = pow(10, log10(temp)) - 1;
            cout << ans << endl;
        }
    }
    return 0;
}