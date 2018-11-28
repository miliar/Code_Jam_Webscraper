#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstring>

using namespace std;

int t;
long long n;
vector <int> vt;


int main(void)
{
    freopen("B-large.in", "r", stdin);
    freopen("codejam_outputB.txt", "w", stdout);

    scanf("%d\n", &t);
    for(int p=1;p<=t;p++)
    {
        scanf("%lld", &n);
        vt.clear();
        while(n)
        {
            vt.push_back(n%10);
            n/=10;
        }
        reverse(vt.begin(), vt.end());
        for(int i=0;i<vt.size()-1;i++)
        {
            if(vt[i] > vt[i+1])
            {
                int p = i+1;
                while(vt[p] < vt[p-1] && p > 0)
                {
                    for(int j=p;j<vt.size();j++)
                    {
                        vt[j] = 9;
                    }
                    p--;
                    vt[p]--;
                }
                break;
            }
        }
        printf("Case #%d: ", p);
        for(int i=0;i<vt.size();i++)
        {
            if(vt[i] == 0)
                continue;
            printf("%d", vt[i]);
        }
        printf("\n");
    }
    return 0;
}
