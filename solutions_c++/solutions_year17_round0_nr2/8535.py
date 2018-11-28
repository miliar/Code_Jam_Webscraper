#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>

using namespace std;

long long powarr[19];
int digit[19];

int main()
{
    ifstream in("input.in");
    ofstream out("output.txt");
    int T;

    in >> T;
    for(int i = 0;i < 19;++i)
        powarr[i] = powl(10LL, i);
    for(int c = 0;c < T;++c)
    {
        long long n;
        in >> n;
        memset(digit, 0, sizeof(digit));
        int idx = 0;
        while(n > 0)
        {
            digit[idx++] = n % 10;
            n /= 10;
        }
        for(int i = 0;i < idx - 1;++i)
        {
            if(digit[i] < digit[i + 1])
            {
                for(int j = 0;j <= i;++j)
                    digit[j] = 9;
                --digit[i + 1];
            }
        }
        long long ans = 0LL;
        for(int i = 0;i < 19;++i)
            ans += powarr[i] * digit[i];
        out << "Case #" << c + 1 << ": " << ans << endl;
    }

    return 0;
}
