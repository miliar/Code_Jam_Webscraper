
/*
 * Michael V. Antosha
 * 2017
 * Michael.Antosha@gmail.com
 * http://mivael.in.ua
 */

#include <iostream>
using std::endl;
// using std::clog;
using std::istream;

#include <map>
using std::map;
using std::make_pair;

#include <cstdint>

#include <cassert>

typedef int64_t vol_t;
typedef int_fast32_t cnt_t;
typedef map< vol_t, cnt_t, std::greater<vol_t> > DescendingMap;

static inline void set_result_from_len(
    const vol_t len,
    vol_t& minOfChosen, vol_t& maxOfChosen)
{
    minOfChosen = (len - 1) / 2;
    maxOfChosen = (len - 0) / 2;
}

static inline void update_cnts(
    DescendingMap& smap,
    const vol_t len, const cnt_t cnt)
{
    DescendingMap::iterator it = smap.find(len);
    if (it == smap.end())
    {
        smap.insert(make_pair(len, cnt));  return;
    }
    it->second += cnt;
}

static void solve(const vol_t N,
                  vol_t K,
                  vol_t& minOfChosen, vol_t& maxOfChosen)
{
    assert(1 <= K  &&  K <= N);

    DescendingMap smap;  smap.insert(make_pair(N, 1));
    for (;;)
    {
        assert(!smap.empty());
        const vol_t len = smap.begin()->first;
        const cnt_t cnt = smap.begin()->second;
        smap.erase(smap.begin());

        if (K <= cnt)
        {
            set_result_from_len(len, minOfChosen, maxOfChosen);
            return;
        }
        K -= cnt;

        assert(len > 1);
        const vol_t rest = len - 1;
        update_cnts(smap, (rest + 1) / 2, cnt);
        update_cnts(smap, (rest + 0) / 2, cnt);
        assert(smap.size() < 10);  // TODO
    }
}

int main(void)
{
    using std::cin;
    std::ios_base::sync_with_stdio(false);  cin.tie(0);

    int T;  cin >> T;
    for (int tc = 1;  tc <= T;  ++tc)
    {
        vol_t N, K;  cin >> N >> K;

        vol_t minOfChosen, maxOfChosen;
        solve(N, K, minOfChosen, maxOfChosen);

        std::cout << "Case #" << tc << ": "
                  << maxOfChosen << " " << minOfChosen << endl;
    }
    return 0;
}
