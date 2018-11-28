#include <iostream>
#include <cmath>

using namespace std;

typedef unsigned long long ull;

struct LevelEntry
{
    ull l, r, c; // Ls, Rs, count
};

void calculate(ull &, ull &, ull, ull);

int main()
{
    int T; // Number of test cases
    cin >> T;
    for(int i = 1; i <= T; ++i)
    {
        ull N, K, LS, RS;
        cin >> N >> K;
        calculate(LS, RS, N, K);
        cout << "Case #" << i << ": " << max(LS, RS) << ' ' << min(LS, RS) << '\n';
    }
    return 0;
}

void calculate(ull &LS, ull &RS, ull N, ull K)
{
    int maxLvls = ceil(log2(N));
    ull cnt = 0;
    LevelEntry one, two;
    one.l = (N-1) >> 1;
    one.r = one.l + 1 - (1 & N);
    one.c = 1;
    for(int lvl = 0; lvl <= maxLvls; ++lvl)
    {
        //cout << "Level " << lvl << "(" << cnt << ")\n";
        //cout << one.l << ", " << one.r << ", " << one.c << '\n';
        //cout << two.l << ", " << two.r << ", " << two.c << "\n\n";
        ull pwr = 1 << lvl;
        if(cnt + pwr >= K) // solution is on this level
        {
            if(one.c < pwr && !(one.l > two.l || one.r > two.r || one.l > two.r || one.r > two.l)) // Ugh.
            {
                LevelEntry temp = one;
                one = two;
                two = temp;
            }
            //cout << "Count: " << cnt << ", one.c: " << one.c << ", K: " << K << '\n';
            //cout << one.l << ", " << one.r << ", " << one.c << '\n';
            //cout << two.l << ", " << two.r << ", " << two.c << "\n\n";
            if(cnt + one.c >= K)
            {
                LS = one.l;
                RS = one.r;
                return;
            }
            LS = two.l;
            RS = two.r;
            return;
        }
        LevelEntry newOne, newTwo;
        // Get products from first group.
        newOne.l = one.l > 1 ? ((one.l - 1) >> 1) + 1 - (1 & one.l) : 0;
        newOne.r = one.l == 0 ? 0 : one.l - 1 - newOne.l;
        if(one.l == one.r)
            newOne.c = one.c << 1;
        else
        {
            newOne.c = one.c;
            newTwo.l = one.r > 1 ? ((one.r - 1) >> 1) + 1 - (1 & one.r) : 0;
            newTwo.r = one.r == 0 ? 0 : one.r - 1 - newTwo.l;
            newTwo.c = one.c;
        }
        //cout << "**\n";
        //cout << newOne.l << ", " << newOne.r << ", " << newOne.c << '\n';
        //cout << newTwo.l << ", " << newTwo.r << ", " << newTwo.c << "\n\n";
        if(pwr > one.c) // Get products from second group
        {
            if(two.l == one.l)
                newOne.c += pwr - one.c;
            else if(two.l == one.r && one.l != one.r)
                newTwo.c += pwr - one.c;
            else
            {
                newTwo.l = two.l > 1 ? ((two.l - 1) >> 1) + 1 - (1 & two.l) : 0;
                newTwo.r = two.l == 0 ? 0 : two.l - 1 - newTwo.l;
            }
            if(two.r == one.l)
                newOne.c += pwr - one.c;
            else if(two.r == one.r && one.l != one.r)
                newTwo.c += pwr - one.c;
            else
            {
                newTwo.l = two.r > 1 ? ((two.r - 1) >> 1) + 1 - (1 & two.r) : 0;
                newTwo.r = two.r == 0 ? 0 : two.r - 1 - newTwo.l;
            }
        }
        //cout << "****\n";
        //cout << newOne.l << ", " << newOne.r << ", " << newOne.c << '\n';
        //cout << newTwo.l << ", " << newTwo.r << ", " << newTwo.c << "\n\n";
        one = newOne;
        two = newTwo;
        cnt += pwr;
    }
}
