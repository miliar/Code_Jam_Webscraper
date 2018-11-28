#include<iostream>
#include<map>
#include<vector>
using namespace std;


long long N, K;

void read() {
    cin >> N >> K;
}


void work(int cases) {
    map<long long, long long, greater<long long> > val2cnt;
    val2cnt[N] = 1;
    
    while (1) {
        long long space = val2cnt.begin()->first;
        long long cnt = val2cnt.begin()->second;
        
        val2cnt.erase(val2cnt.begin());
        
        if (K <= cnt) {
            cout << "Case #" << cases << ": " << space / 2 << ' ' << (space - 1) / 2 << endl;
            break;
        }

        K -= cnt;
        
        val2cnt[space / 2] += cnt;
        val2cnt[(space - 1) / 2] += cnt;
    }
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
