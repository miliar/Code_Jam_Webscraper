#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

const int MAX_N = 100;

int main(void)
{
    int T;  cin >> T;
    int N, P, val;  

    map<int, int> cnt;

    for (int t = 1; t <= T; t ++)
    {
        int res = 0;
        cnt.clear();
        scanf("%d %d", &N, &P);

        for (int i = 0; i < N; i ++)
        {
            scanf("%d", &val);

            if (val % P)
                cnt[val % P]++;
            else
                res++;
        }

        if (P == 2) 
        {
            res += (cnt[1] + 1) / 2;
        }
        else if (P == 3)
        {
            while (cnt[1] != 0 && cnt[2] != 0)
            {
                cnt[1]--;
                cnt[2]--;
                res++;
            }


            res += (cnt[1]+2) / 3 + (cnt[2]+2) / 3;
        }





        printf("Case #%d: %d\n", t, res);
    }
}
