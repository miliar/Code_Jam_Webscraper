#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstring>
#include <bitset>
#include <functional>
#include <map>

using namespace std;

typedef pair<int, int> pii;
typedef pair<pair<int, int>, pair<int, int>> piii;
typedef long long ll;
#define ff first.first
#define fs first.second
#define sf second.first
#define ss second.second

int t;
int d, n;
int loc[1001], speed[1001];

int main(void)
{
    freopen("A-large.in", "r", stdin);
    freopen("output-large-A.txt", "w", stdout);
    scanf("%d", &t);
    for(int o=1;o<=t;o++)
    {
        scanf("%d %d", &d, &n);
        double temp = 0;
        for(int i=0;i<n;i++)
        {
            scanf("%d %d", &loc[i], &speed[i]);
            temp = max(temp, ((double)d-(double)loc[i])/(double)speed[i]);
        }

        printf("Case #%d: %.7lf\n", o, (double)d/temp);
    }
}
