#include <iostream>
//#include <math.h>
//#include <stdlib.h>
#include <iomanip>
//#include <queue>
//#include <utility>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int test=0;test<t;test++)
    {
        int d,n;
        cin >> d >> n;
        double mx = 0;
        for(int i=0;i<n;i++)
        {
            int k,s;
            cin >> k >> s;
            mx = max(mx,(double)(d-k)/s);
        }
        cout << "Case #" << test+1 << ": ";
        cout << fixed << setprecision(6) << d/mx << endl;
    }
    return 0;
}
