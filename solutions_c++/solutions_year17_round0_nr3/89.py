#include <iostream>
#include <algorithm>
#include <limits>
#include <queue>
#include <string>

using namespace std;

void doCase()
{
    int64_t N, K;
    cin >> N >> K;

    int64_t val = N;

    while(K > 1)
    {
        val--;
        int64_t remainder = val % int64_t(2);
        val /= int64_t(2);
        if((K % int64_t(2)) == 0)
           val += remainder;
        //cout << K << " " << val << " " << remainder << endl;
        K /= 2;
    }
    val--;
    int64_t half = val/int64_t(2);

    cout << val-half << " " << half << endl;
}

int main()
{
    int T;
    cin >> T;
    for(int i=0; i<T; i++)
    {
        cout << "Case #" << i+1 << ": ";
        doCase();
    }
}
