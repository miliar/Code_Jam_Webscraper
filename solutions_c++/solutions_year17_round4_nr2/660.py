#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1e3 + 5;
const int M = 1e3 + 5;

int n, m, C, p[M], c[M], num[1005], sv[1005], id[M];

bool cmp(int i, int j)
{
    return p[i] < p[j];
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int Case = 1; Case <= T; ++Case)
    {
        int mi = 0;
        memset(num, 0, sizeof(num));
        memset(sv, 0, sizeof(sv));
        scanf("%d%d%d", &n, &C, &m);
        for(int i = 1; i <= m; ++i)
        {
            scanf("%d%d", &p[i], &c[i]);
            ++num[c[i]];
            mi = max(mi, num[c[i]]);
        }
        int now = mi, rem = 0;
        
        for(int i = 1; i <= m; ++i) id[i] = i;
        sort(id + 1, id + m + 1, cmp);
     
        int curp = 0;
        for(int ii = 1; ii <= m; )
        {
            ++curp;
            int jj = ii - 1;
            while(jj < m && p[id[jj + 1]] == curp) ++jj;
            sv[curp] = jj - ii + 1;
            //cout<<curp<<" "<<ii<<" "<<jj<<"..."<<endl;
            if(ii <= jj)
            {
                if(rem + now >= (jj - ii + 1)) rem = rem + now - (jj - ii + 1);
                else
                {
                    int cursum = (curp - 1) * now - rem;
                    cursum += (jj - ii + 1);
                    now = cursum / curp + (cursum % curp == 0 ? 0 : 1);
                    rem = now * curp - cursum;
                }
            }
            else
            {
                rem += mi;
            }
            ii = jj + 1;
        }
        int ans1 = now;
        int ans2 = 0;
        for(int i = n; i >= 1; --i)
        {
            //cout<<sv[i]<<"....hah"<<endl;
            if(sv[i] > ans1) ans2 += sv[i] - ans1;
        }
        printf("Case #%d: %d %d\n", Case, ans1, ans2);
    }
    
    return 0;
}
