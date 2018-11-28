
#include<bits/stdc++.h>
using namespace std;
#define D(x)        cout << #x " = " << (x) << endl
#define MAX         1000
typedef long long int LL;

vector<double> v;
double U;
const double eps = 1e-9;

void fix(double rem)
{
    int segSize = 1;
    while(segSize < v.size())
    {
        double nxt = v[segSize];
        double diff = nxt - v[segSize - 1];
        double need = diff * segSize;

        if(need < rem + eps){
            for(int i = 0; i < segSize; i++)
                v[i] = v[segSize];
            segSize = segSize + 1;
            rem -= need;
        }
        else{
            double perHead = rem / segSize;
            for(int i = 0; i < segSize; i++)
                v[i] += perHead;
            return;
        }
    }

    double perHead = rem / segSize;
    for(int i = 0; i < segSize; i++)
        v[i] += perHead;
    return;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int i, j, k, t, cs, n;
    double p;
    long double answer;

    scanf("%d", &t);
    for(cs = 1; cs <= t; cs++)
    {
        v.clear();

        scanf("%d %d", &n, &k);
        scanf("%lf", &U);
        for(i = 1; i <= n; i++)
        {
            scanf("%lf", &p);
            v.push_back(p);
        }

        sort(v.begin(), v.end());
        fix(U);

        answer = 1.0;
        for(auto x : v) answer = answer * x;
        printf("Case #%d: %0.10f\n", cs, (double) answer);
    }

    return 0;

}
