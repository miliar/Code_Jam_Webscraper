#include <cstdio>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>

#define MP make_pair
#define PB push_back

using namespace std;

int N;
pair<int, char> t[3];

int main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt2.out", "w", stdout);

    int nbT;
    scanf("%d", &nbT);

    for(int ct = 1; ct <= nbT; ct++)
    {
        int N, R, O, Y, G, B, V;
        scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
        int S = R+Y+B;
        t[0] = MP(R, 'R');
        t[1] = MP(Y, 'Y');
        t[2] = MP(B, 'B');

        sort(t, t+3);

        string ans;
        for(int i = 0; i < N; i++)
            ans += '?';

        printf("Case #%d: ", ct);
        if(t[2].first > S-t[2].first)
            printf("IMPOSSIBLE\n");
        else
        {
            for(int i = 0; i < 2*t[2].first; i += 2)
                ans[i] = t[2].second;
            int act = 1;
            for(int i = 2*t[2].first-1; i < N; i++)
            {
                ans[i] = t[act].second;
                t[act].first--;
                act = !act;
            }
            for(int i = 1; i < N; i += 2)
                if(t[0].first)
                {
                    ans[i] = t[0].second;
                    t[0].first--;
                }
                else if(t[1].first)
                {
                    ans[i] = t[1].second;
                    t[1].first--;
                }

            printf("%s\n", ans.c_str());
        }
    }

    return 0;
}
