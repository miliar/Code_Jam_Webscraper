#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

typedef long long LL;

int main()
{
    #ifdef FILE_IO
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    #endif

    int T;
    scanf("%d", &T);
    for(int test = 1; test <= T; test++)
    {
        printf("Case #%d: ", test);

        LL x;
        vector <int> v;
        scanf("%lld", &x);
        while(x > 0)
        {
            v.push_back(x % 10);
            x /= 10;
        }
        reverse(v.begin(), v.end());

        for(int i = 0; i + 1 < v.size(); i++)
            if(v[i] > v[i + 1])
            {
                int pos = i - 1;
                while(pos >= 0 && v[pos] == v[i])
                    pos--;
                pos++;
                v[pos]--;
                for(int i = pos + 1; i < v.size(); i++)
                    v[i] = 9;
                break;
            }

        while(!v.empty() && v[0] <= 0)  v.erase(v.begin());

        for(auto x: v)
            printf("%d", x);
        printf("\n");
    }

    return 0;
}
