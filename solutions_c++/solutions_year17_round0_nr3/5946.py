
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <exception>
#include <utility>
#include <tuple>

using namespace std;

struct Stalls
{
    int64_t minLR=0;
    int64_t maxLR=0;
    int64_t n=0;
    int64_t i=0;
};

Stalls build(int64_t n, int64_t ii){
    //count<< "build: n: "<<n<<", ii: " << ii<< endl;
    int64_t i = (n-1)/2;

    //if(n-i-1 < 0) throw runtime_error("build");
    int64_t minLR = min(i, n-i-1 < 0 ? 0: n-i-1);
    //int64_t minLR = min(i, n-i-1);
    int64_t maxLR = max(i, n-i-1);

    return Stalls{minLR, maxLR, n, ii};
}

template<class T>
void dumpV(T& v, string comment){
    //count<< comment<<"minLR: "<<v.minLR << endl;
    //count<< comment<<"maxLR: "<<v.maxLR << endl;
    //count<< comment<<"n: "<<v.n << endl;
    //count<< comment<<"i: "<<v.i << endl;
}

template<class T>
void dump(T& t, string comment){
    //count<< "Container["<<comment<<"] of size " << t.size() <<":" << endl;
    for(auto&v: t){
        dumpV(v, comment);
        //count<< "---" << endl;
    }
    //count<< "END" << endl;
}

Stalls solve(int64_t n, int64_t k){

    auto sortFn = [](const Stalls& a, const Stalls& b) { 


        return tie(a.minLR, a.maxLR, a.i, a.n) < tie(b.minLR, b.maxLR, b.i, b.n);
        //return make_pair(a.minLR, a.maxLR, a.i, a.n) < make_pair(b.minLR, b.maxLR, b.i, b.n);
    };

    multiset<Stalls, decltype(sortFn)> os(sortFn);

    os.insert(build(n, 0));

    while(k > 1){
        //count<< "k ="<<k<<endl;
        dump(os, "all");

        auto it_n = prev(os.end());
        Stalls stall = *it_n;
        dumpV(stall, "largest");

        auto sz = os.size();
        os.erase(it_n);
        //dump(os, "all-post-remove");
        if(sz <= os.size()) throw runtime_error("bad size");

        //count<< "n pick: " << stall.n << endl;

        int64_t i = (stall.n-1)/2;
        int64_t l = i;
        int64_t r = stall.n-i-1;

        //count<< "i: " << i << endl;
        //count<< "l: " << l << endl;
        //count<< "r: " << r << endl;

        // reverse i for sorting order (prefer left).
        os.insert(build(l, -(stall.i)));
        os.insert(build(r, -(stall.i+i+1)));

        --k;
    }

     return *prev(os.end());
}

int main(int len, const char** args){
    string file;
        
    if(len > 1){
        file = string(args[1]);
    }
    else{
        file = "tiny.in";
    }

    ifstream fh(file.c_str());

    string line;
    fh >> line;
    int ncases = stoi(line);

    string num;
    ofstream out(file + ".out");
    for(int i = 0; i < ncases; ++i){
        string sn,sk;
        fh >> sn;
        fh >> sk;

        int64_t n = strtoll(sn.c_str(), nullptr, 10);
        int64_t k = strtoll(sk.c_str(), nullptr, 10);


        auto ans = solve(n, k); 

        stringstream ss;
        ss<< "Case #" << i+1 << ": " << ans.maxLR << " " << ans.minLR << endl;
        string sans = ss.str();
        cout << sans;
        out << sans;
    }

    return 0;
}
