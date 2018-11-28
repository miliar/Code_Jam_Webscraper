#include <stdio.h>
#include <bits/stdtr1c++.h>

#define clr(ar) memset(ar, 0, sizeof(ar))
#define read() freopen("lol.txt", "r", stdin)
#define write() freopen("out.txt", "w", stdout)
#define dbg(x) cout << #x << " = " << x << endl
#define ran(a, b) ((((rand() << 15) ^ rand()) % ((b) - (a) + 1)) + (a))

using namespace std;

typedef pair<long long, long long> Pair;

struct node{
    long long len, ls, rs;
    node(){}
    node(long long l){
        len = l;
        ls = len >> 1, rs = len - (len >> 1);
    }

    inline bool operator < (const node& other) const{
        if (min(ls, rs) != min(other.ls, other.rs)) return min(ls, rs) < min(other.ls, other.rs);
        if (max(ls, rs) != max(other.ls, other.rs)) return max(ls, rs) < max(other.ls, other.rs);
        return (len > other.len);
    }
};

int main(){
    read();
    write();
    long long T = 0, t, n, i, j, k, x, y, c, mid, len, h = 0;

    scanf("%lld", &t);
    while (t--){
        scanf("%lld %lld", &n, &k);
        priority_queue <node> PQ;
        tr1::unordered_map <long long, long long> mp;
        PQ.push(node(n - 1));
        i = 1, mp[n - 1]++;

        while (i <= k){
            node cur = PQ.top();
            PQ.pop();
            len = cur.len, mid = len >> 1;
            c = mp[len];
            i += c;

            if (mid != 0){
                x = mid - 1;
                if (!mp.count(x)) PQ.push(node(x));
                mp[x] += c;
            }
            if (mid < len){
                x = len - mid - 1;
                if (!mp.count(x)) PQ.push(node(x));
                mp[x] += c;
            }
        }
        x = max(mid, len - mid);
        y = min(mid, len - mid);
        printf("Case #%lld: %lld %lld\n", ++T, x, y);
        h = h * 666666667 + x + 13;
        h = h * 666666667 + y + 19;
    }

    fprintf(stderr, "hash = %llu\n", (unsigned long long)h);
    return 0;
}

/***

20
1000000000000000000 1000000000000000000
1000000000000000000 100000000000000000
1000000000000000000 10000000000000000
1000000000000000000 1000000000000000
1000000000000000000 100000000000000
1000000000000000000 10000000000000
1000000000000000000 1000000000000
1000000000000000000 100000000000
1000000000000000000 10000000000
1000000000000000000 1000000000
1000000000000000000 100000000
1000000000000000000 10000000
1000000000000000000 1000000
1000000000000000000 100000
1000000000000000000 10000
1000000000000000000 1000
1000000000000000000 100
1000000000000000000 10
1000000000000000000 1
1 1

***/
