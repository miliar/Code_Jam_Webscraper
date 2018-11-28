#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("inC.txt", "r", stdin);
    freopen("outC.txt", "w", stdout);
    int T;cin >> T;
    for(int cas=1;cas<=T;++cas){
        cout << "Case #" << cas << ": ";
        int64_t N, K;
        cin >> N >> K;
        map<int64_t, int64_t> inters;
        inters[N]=1;
        --K;
        while(K){
            assert(!inters.empty() && inters.rbegin()->first && inters.rbegin()->second);
            int64_t cnt = min(inters.rbegin()->second, K);
            int64_t l = inters.rbegin()->first;
            inters.rbegin()->second-=cnt;
            if(inters.rbegin()->second==0) inters.erase(prev(inters.end()));
            K-=cnt;
            inters[l/2]+=cnt;
            inters[(l-1)/2]+=cnt;
        }
        cout << inters.rbegin()->first/2 << " " << (inters.rbegin()->first-1)/2;
        cerr << inters.rbegin()->first/2 << " " << (inters.rbegin()->first-1)/2 << "\n";

        cout << "\n";
    }

    return 0;
}

