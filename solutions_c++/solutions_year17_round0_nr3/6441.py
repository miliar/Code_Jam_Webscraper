#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Kofola {
    long long n;
    long long cnt;
    bool operator<(const Kofola& k) const { return n > k.n; }
    Kofola() {}
    Kofola(long long n, long long cnt) : n(n), cnt(cnt) {}
};


void trans(vector<Kofola>& kv) {
    vector<Kofola> ktmp;
    for (auto k : kv) {
        ktmp.push_back(Kofola(k.n/2, k.cnt));
        ktmp.push_back(Kofola((k.n-1)/2, k.cnt));
    }
    
    sort(ktmp.begin(), ktmp.end());

    kv.clear();
    for (int i=0; i<int(ktmp.size()); i++) {
        if (i+1 < int(ktmp.size()) && ktmp[i].n == ktmp[i+1].n)
            ktmp[i+1].cnt += ktmp[i].cnt;
        else
            kv.push_back(ktmp[i]);
    }
}


void process(const vector<Kofola>& kv, long long& last) {
    for (auto k : kv) {
        if (last <= k.cnt)
            throw k.n;
        else
            last -= k.cnt;
    }
}


int main(int argc, char* argv[]) {
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        
        try {
            Kofola k;
            long long last;
            cin >> k.n >> last;
            k.cnt = 1;
            
            vector<Kofola> kv(1, k);
            
            while (true)
                process(kv, last), trans(kv);
        }

        catch (long long n) {
            cout<<"Case #"<<t<<": ";
            if (n&1) cout<<(n/2)<<" "<<(n/2)<<endl;
            else cout<<(n/2)<<" "<<(n/2-1)<<endl;
        }
    }

    return 0;
}

