#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int m=1;m<=t;++m)
    {
        int n,k;
        cin >> n >> k;
        int msb = k;
        msb |= msb >> 1;
        msb |= msb >> 2;
        msb |= msb >> 4;
        msb |= msb >> 8;
        msb |= msb >> 16;
        msb = msb - (msb>>1);
        n -= msb-1;
        int mod = n%msb;
        if (k+1-msb<=mod) k = n/msb;
        else k = (n/msb)-1;
        cout << "Case #" << m << ": " << (k+1)/2 << ' ' << k/2 << endl;
    }
    return 0;
}
