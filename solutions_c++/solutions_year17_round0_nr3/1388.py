#include <fstream>
#include <cstring>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

ifstream cin("date.in");
ofstream cout("date.out");

long long k;

long long ct[1005][1005];

long long inq[1005];

struct p{
    long long val;
    long long key;
};

p sc[1005];

bool sorti(p a, p b) {
    return a.key > b.key;
}

map<long long, long long> h;

priority_queue<long long> q;

void nebuneala(long long x) {
    if (h[x]) {
        return;
    }
    h[x] = ++k;
    inq[k] = x;
    if(x >= 2) {
        nebuneala(x / 2);
        nebuneala((x - 1) / 2);
        for (int i = 1; i <= 1000; ++i) {
            ct[h[x]][i] += ct[h[x / 2]][i] + ct[h[(x - 1) / 2]][i];
        }
        ct[h[x]][h[x / 2]]++;
        ct[h[x]][h[(x - 1) / 2]]++;
    }
}

int main() {
    int t, nrt = 0;
    cin>>t;
    while (t){
        for (int i = 1; i <= 1002; ++i) {
            sc[i].key = -1;
        }
        memset(ct, 0, sizeof(ct));
        memset(inq, 0, sizeof(inq));
        h.clear();
        k = 0;
        ++nrt;
        --t;
        cout<<"Case #"<<nrt<<": ";
        long long n, ka;
        cin>>n>>ka;
        nebuneala(n);
        for (int i = 1; i <= 1000; ++i) {
            sc[i].val = ct[h[n]][i];
            if (sc[i].val) {
                sc[i].key = inq[i];
            }
        }
        sort(sc + 1, sc + 1001, sorti);
        /*for (int i = 1; i <= 1000; ++i) {
            cout<<sc[i].key<<" ";
        }*/
        if (ka == 1) {
            cout<<n / 2<<" "<<(n - 1) / 2<<"\n";
        } else {
            --ka;
            int i = 1;
            while (ka > 0) {
                ka -= sc[i].val;
                ++i;
            }
            --i;
            cout<<sc[i].key / 2<<" "<<(sc[i].key - 1) / 2<<"\n";
        }
    }
    return 0;
}
