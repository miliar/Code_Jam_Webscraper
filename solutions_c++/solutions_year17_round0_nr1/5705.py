#include <cstdio>
#include <set>
#include <cstring>
#include <queue>
#include <algorithm>
#include <utility>
#include <limits>

#define MAXS 1001
using namespace std;

struct Bitset
{
    unsigned long long *buf;
    unsigned len;
    unsigned qlen;
    
    Bitset(char *str)
        {
            len = strlen(str);
            qlen = (len+63)/64;
            buf = new unsigned long long[qlen];
            memset(buf, 0, qlen * sizeof(unsigned long long));
            for (int i = 0; i < len; ++i)
            {
                if (str[i] == '+')
                {
                    set(i);
                }
            }
            
        }

    Bitset(const Bitset &bs) : len(bs.len), qlen(bs.qlen)
        {
            buf = new unsigned long long[qlen];
            memcpy(buf, bs.buf, qlen * sizeof(unsigned long long));
        }

    Bitset& operator=(Bitset &bs)
        {
            if (this == &bs)
            {
                return bs;
            }

            swap(buf, bs.buf);
            swap(len, bs.len);
            swap(qlen, bs.qlen);
            return *this;
        }

    ~Bitset()
        {
            if (buf)
            {
                delete buf;
            }
        }

    void set(int idx)
        {
            buf[idx/(sizeof(unsigned long long)*8)] |= 1ULL << (idx % (sizeof(unsigned long long)*8));
        }

    void unset(int idx)
        {
            buf[idx/(sizeof(unsigned long long)*8)] &= ~(1ULL << (idx % (sizeof(unsigned long long)*8)));
        }

    unsigned long long get(int idx) const
        {
            return buf[idx/(sizeof(unsigned long long)*8)] & (1ULL << (idx % (sizeof(unsigned long long)*8)));
        }

    void flip(int idx)
        {
            buf[idx/(sizeof(unsigned long long)*8)] ^= 1ULL << (idx % (sizeof(unsigned long long)*8));
        }

    bool is_full()
        {
            for (int i = 0; i < qlen - 1; ++i)
            {
                if (numeric_limits<unsigned long long>::max() != buf[i])
                {
                    return false;
                }
            }

            if (buf[qlen-1] != (1ULL << (len % 64))-1)
            {
                return false;
            }

            return true;
        }

    bool operator<(const Bitset & bs) const
        {
            for (int i = 0; i < len; ++i)
            {
                if (bs.get(i) && !get(i))
                {
                    return true;
                }
                else if (!bs.get(i) && get(i))
                {
                    return false;
                }
            }

            return false;
        }

    
};


int bfs(Bitset &bs, int k)
{
    set<Bitset> st;
    queue<pair<Bitset,int>> q;
    st.insert(bs);
    q.push(make_pair(bs,0));

    if (bs.is_full())
    {
        return 0;
    }

    while (!q.empty())
    {
        pair<Bitset,int> crt = q.front();
        q.pop();

        for (int i = 0; i <= crt.first.len - k; ++i)
        {
            Bitset tmp(crt.first);
            for (int j = i; j < i + k; ++j)
            {
                tmp.flip(j);
            }

            if (tmp.is_full())
            {
                return crt.second + 1;
            }
            
            auto it = st.find(tmp);
            if (it == st.end())
            {
                st.insert(tmp);
                q.push(make_pair(tmp, crt.second + 1));
            }
        }       
    }

    return -1;
}

int main()
{
    freopen("flip.in", "r", stdin);
    freopen("flip.out", "w", stdout);

    int n;scanf("%d", &n);

    for (int i = 1; i <= n; ++i)
    {
        int k;
        char buf[MAXS];
        scanf("%s %d\n", buf, &k); 

        Bitset bs(buf);

        int result = bfs(bs, k);
        if (-1 == result)
        {
            printf("Case #%d: IMPOSSIBLE\n", i);
        }
        else
        {
            printf("Case #%d: %d\n", i, result);
        }
    }
    
    return 0;
}
