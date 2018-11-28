#include<iostream>

using namespace std;
int main()
{
    int t;
    cin >> t;
    for (int cs = 1; cs <= t; cs++) {
        long long n;
        long long k;
        cin >> n >> k;
        long long  i;
        long long  a = 1;
        long long  b = 0;
        long long  result;
        for (i = 1; ; i++) {
            //cout << i << endl;
            if (k < (1LL << i))
            {
                if (k - ((1LL << (i - 1LL)) - 1LL) <= a) {
                    result = n;
                } else {
                    result = n - 1;
                }
                break;
            } else {
                if (n & 1) {
                    a = a * 2 + b;
                } else {
                    b = a + b * 2;
                }
                n = (n >> 1);
            }
        }

        cout << "Case #" << cs << ": " << result / 2 << " " << result - 1 - result / 2 << endl;
    }
}
