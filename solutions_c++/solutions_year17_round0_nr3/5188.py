#include <iostream>
#include <queue>

using namespace std;
using ll = long long;

struct Interval {
    ll Ls, Rs;

    Interval(ll L, ll R) : Ls(L), Rs(R) {}

    bool operator<(const Interval& I) const
    {
        auto size = Rs - Ls + 1;
        auto sizeI = I.Rs - I.Ls + 1;

        if (size != sizeI)
            return size < sizeI;

        return Ls < I.Ls;
    }
};

int main()
{
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test)
    {
        ll n, k;
        cin >> n >> k;

        priority_queue<Interval> pq;

        pq.push(Interval(1, n));

        ll Ls, Rs;

        while (k--)
        {
            auto next = pq.top();
            pq.pop();

            ll mid = (next.Rs + next.Ls) / 2;
//printf("Next = [%lld, %lld], mid = %lld\n", next.Ls, next.Rs, mid);
            Ls = mid - next.Ls;
            Rs = next.Rs - mid;
//printf("Ls = %lld, Rs = %lld\n", Ls, Rs);
            pq.push(Interval(next.Ls, mid - 1));
            pq.push(Interval(mid + 1, next.Rs));
        }

        printf("Case #%d: %lld %lld\n", test, max(Ls, Rs), min(Ls, Rs));
    }

    return 0;
}
