#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int t;

    cin >> t;

    for (int i = 1; i <= t; ++i) {
        unsigned long long int n;
        cin >> n ;

        unsigned long long int res = n;
        while (res) {
            vector<int> digits;
            n=res;
            while (n) {
                digits.push_back(n % 10);
                n /= 10;
            }
            reverse(digits.begin(), digits.end());
            vector<int> sorted = digits;
            sort(sorted.begin(), sorted.end());

            if (sorted == digits) {

                break;
            }
            else {
                --res;
            }
        }
        cout << "Case #" << i << ": " << res << endl;
    }

    return 0;
}
