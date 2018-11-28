#include <iostream>
#include <fstream>
using namespace std;

int main(void)
{
     freopen("B-small-attempt1.in","r",stdin);
     freopen("B-small-attempt1.out","w",stdout);
    int T, a[20];
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int j = 0, k = 0, ct = 1;
        unsigned long long int n, c;
        cin >> n;
        c = n;
        while (ct)
        {
            while (c)
            {
                a[j] = c % 10;
                c /= 10;
                j++;
            }
            while (1)
            {
                if (k == j - 1 || k == j)
                {
                    ct = 0;
                    break;
                }
                if (a[k + 1] <= a[k])
                {
                    k++;
                    continue;
                }
                else
                {
                    --n;
                    c = n;
                    j = 0;
                    k = 0;
                    break;
                }
                if (k == j - 2)
                {
                    ct = 0;
                    break;
                }
            }
        }
        cout << "Case #" << i + 1 << ": " << n << endl;
    }
    return 0;
}
