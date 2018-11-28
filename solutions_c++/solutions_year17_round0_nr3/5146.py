#include <iostream>

#define FALSE   0
#define TRUE    1

#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <stdint.h>
#include <unistd.h>
using namespace std;

#define MAX_STALL   (1000000 + 2)

class maxt
{
private:
    int c[1000000+1];
    uint64_t pos;
public:
    maxt(uint64_t p)
    {
        for(uint64_t i = 0; i < 1000000+1; i++)
            c[i] = 0;
        c[p] += 1;
        pos = p;
    }

    void put(uint64_t i)
    {
        c[i] += 1;
    }

    int getMax()
    {
        for(; pos > 0; pos --)
        {
            if(c[pos] > 0)
            {
                c[pos] -= 1;
                return pos;
            }
        }

        return pos;
    }
};

class bathroom
{
private:

    uint64_t man_k;
    maxt mt;
    int flag;
    uint64_t max;
    uint64_t kill_m;
    uint64_t kill_c;
    uint64_t max_c;
public:
    bathroom(uint64_t n, uint64_t k);
    virtual ~bathroom();

    string solve();
    string solve2();
};

bathroom::bathroom(uint64_t n, uint64_t k)
    : man_k(k),
      mt(n)
{
    flag = 0;
    kill_m = 1;
    kill_c = kill_m;
    //printf("N = %lu, K = %lu\n", max, man_k);
}

bathroom::~bathroom()
{

}

string bathroom::solve()
{
    string a;
    return a;
}

string bathroom::solve2()
{
    uint64_t save = 0,left = 0, right = 0;
    uint64_t res, m, m2;
    uint64_t big = 0, small = 0;

    for(uint64_t i = 0; i < man_k; i++)
    {
        res = mt.getMax();
        //printf("max: %lu\n", res);
        if(res == 1)
        {
            m = m2 = 0;
            break;
        }
        m = res / 2;
        if(res % 2 == 0)
            m2 = m - 1;
        else
            m2 = m;

        mt.put(m);
        mt.put(m2);
    }

    //printf("%lu, %lu\n", m, m2);

    string ans("");
    char tmp[128] = {0,};
    sprintf(tmp, "%lu %lu", m, m2);
    ans.append(tmp);
    return ans;
}

int main()
{
    int t;
    uint64_t k, n;

    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n >> k;
        bathroom br(n, k);
//        br.solve2();
        cout << "Case #" << i << ": " << br.solve2() << endl;

    }
    return 0;
}

