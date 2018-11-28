#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <climits>
#include <algorithm>
#include <cstring>
#include <map>
#include <queue>
#include <cmath>

using namespace std;

int t;
int a, b;
pair<double, double> p[1234];
int d, n;

int main(void)
{
    freopen("A-large.in", "r", stdin);
    freopen("ALoutput.txt", "w", stdout);

    cin >> t;


    for(int test=1;test<=t;test++){
        cin >> d >> n;
        for(int j=0;j<n;j++){
            cin >> a >> b;
            p[j].first = a;
            p[j].second = b;
        }

        double longTime = 0;
        for(int i=0;i<n;i++){
            longTime = max(longTime, (d-p[i].first) / p[i].second);
        }

        printf("Case #%d: %0.7f\n", test, d/longTime);
    }

    return 0;
}
