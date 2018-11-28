#include <stdio.h>
#include <algorithm>

class act{
    public:
    int start, finish, person;
    int operator < (const act & that) const {
        return this->start < that.start;
        }

    };

act a[210];
int gaps[2][210]; // gaps between same

int main()
{
int tc, tt;
    scanf("%d", &tt);
    for (tc = 0; tc < tt; tc++){
        printf("Case #%d: ", tc + 1);
        int apc[2], ac;
        scanf("%d%d", &apc[0], &apc[1]);
        ac = apc[0] + apc[1];
        for (int p = 0, i = 0; p<2; ++p){
            for (int j = 0; j < apc[p]; ++j, ++i){
                //int s, f;
                scanf("%d%d", &a[i].start, &a[i].finish);
                a[i].person = p;
                }
            }
        std::sort(a, a + ac);
        a[ac] = a[0];
        a[ac].start += 24*60;
        int gaps_c[2] = {0};
        int tm_free[2] = {0};
        int tm_spare = 0; // gaps between different
        int n_swinches = 0;
        for (int i= 0; i < ac; i++){
            int gap = a[i+1].start - a[i].finish;
            tm_free[a[i].person] += a[i].finish - a[i].start;
            if(a[i].person == a[i+1].person) {
                gaps[a[i].person][gaps_c[a[i].person]++] = gap;
                tm_free[a[i].person] += gap;
                }
            else {
                tm_spare += gap;
                ++n_swinches;
                }
            }
        for (int p = 0; p<2; ++p){
            std::sort(gaps[p], gaps[p] + gaps_c[p]);
            for (int i = gaps_c[p] - 1; tm_free[p] > 720 && i>= 0; --i){
                tm_free[p] -= gaps[p][i];
                n_swinches += 2;
                }
            }
        printf("%d\n", n_swinches);
        }
    return 0;
}
