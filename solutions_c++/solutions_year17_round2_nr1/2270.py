#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
#include <queue>
#include <iomanip>

using namespace std;

const long double eps = 0.000001;
const long double eps2=eps;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    freopen("large.out", "w", stdout);
    freopen("t.in", "r", stdin);



    long long nbT;
    cin >> nbT;
    long long speed[1000], dist[1000], D;
    int n;


    for (long long t = 1; t <= nbT; t++)
    {
        cin >> D >> n;
        long double minSpeed = 1e40, minTime = 1e40;
        for (int i = 0; i < n; i++)
        {
            cin >> dist[i] >> speed[i];
            minTime = min(minTime, (D-dist[i])/(long double)speed[i]);
            minSpeed = min(minSpeed, (long double)speed[i]);

        }


        long double deb, fin, mid;
        deb = minSpeed;
        fin++;
        fin =D/minTime+1;

        while (fin - deb > eps)
        {
            //cout << mid << endl;

            mid = (fin+deb)/2;
            bool isOk = true;
            for (int i = 0; i < n; i++)
            {
                if (D*speed[i] < mid*(D-dist[i]))
                {
                    isOk = false;
                    break;
                }
            }

            if (isOk)
                deb = mid;
            else
                fin = mid;
        }


		std::cout << "Case #" << t << ": ";
		std::cout << std::fixed;
        std::cout << std::setprecision(7);
		cout << mid << endl;

    }

    return 0;
}
