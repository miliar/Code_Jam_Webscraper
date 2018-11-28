#include <cstdio>
#include <set>
using namespace std;

struct Gap
{
    int ldx, rdx;
    Gap(int l, int r) : ldx(l), rdx(r)
        { }

    bool operator<(const Gap &gp) const
        {
            if (rdx - ldx > gp.rdx - gp.ldx)
            {
                return true;
            }

            if (gp.rdx - gp.ldx > rdx - ldx)
            {
                return false;
            }

            if (ldx < gp.ldx)
            {
                return true;
            }

            return false;
        }
};

int main()
{
    freopen("bath.in", "r", stdin);
    freopen("bath.out", "w", stdout);
    int t; scanf("%d", &t);

    for (int i = 1; i <= t; ++i)
    {
        long long n, k;
        scanf("%lld%lld", &n, &k);

        set<Gap> s;
        s.insert(Gap(1, n));
        for (int j = 1; j < k; ++j)
        {
            Gap gp = *(s.begin());
            s.erase(s.begin());

            if (gp.ldx != gp.rdx)
            {
                int mid = (gp.ldx+gp.rdx)/2;

                if (mid > gp.ldx)
                {
                    s.insert(Gap(gp.ldx, mid-1));
                }

                if (mid < gp.rdx)
                {
                    s.insert(Gap(mid+1, gp.rdx));
                }
                
                //s.insert(Gap(gp.ldx, (gp.ldx+gp.rdx)/2-1));
                //s.insert(Gap((gp.ldx+gp.rdx+1)/2, gp.rdx));
            }
        }

        Gap last = *(s.begin());
        int mid = (last.rdx + last.ldx)/2;
        printf("Case #%d: %d %d\n", i, last.rdx -mid, mid-last.ldx);
    }
    
    return 0;
}
