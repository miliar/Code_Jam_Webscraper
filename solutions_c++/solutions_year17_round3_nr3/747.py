#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
typedef long long LL;
const double PI = acos(-1);
int T, n, k;
double p[102], U;

int main()
{
    
    freopen("/Users/RUSH_D_CAT/Desktop/in.txt", "r", stdin);
    freopen("/Users/RUSH_D_CAT/Desktop/out.txt", "w", stdout);
    

    cin >> T;
    int cas = 0;
    while(T--)
    {
        scanf("%d %d", &n, &k);
        cin >> U;
        for(int i=1;i<=n;i++)
        {
            cin >> p[i];
        }
        sort(p+1, p+1+n);
        p[n+1] = 1;
        int cnt = 1;
        
        for(int i=1;i<=n;i++)
        {
            double need = (p[i+1] - p[i]) * i;
            if(need < U)
            {
                for(int j=1;j<=i;j++)
                {
                    p[j] = p[i+1];  
                }
                U -= need;
            } else {
                for(int j=1;j<=i;j++)
                {
                    p[j] = p[j] + U/i;
                }
                break;
            }
        }

        double ans = 1;
        for(int i=1;i<=n;i++)
        {
            ans *= p[i];
        }
        printf("Case #%d: %.8f\n", ++cas, ans);
    }
}











