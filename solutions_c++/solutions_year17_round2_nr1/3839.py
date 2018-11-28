#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
#include <map>

using namespace std;

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    for (int i=0;i<T;i++)
    {
        int D, N;
        cin >> D >> N;
        vector<int> K(N), S(N);
        double ans = 0;
        for (int j=0;j<N;j++)
        {
            int k, s;
            cin >> k >> s;
            double tm = (double)(D-k)/s;
            ans = max(tm, ans);
        }
        ans = (double)(D) / ans;
        printf("Case #%d: %.6f\n", (i+1), ans);
    }




 return 0;
}
