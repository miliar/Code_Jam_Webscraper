#include<iostream>
#include<string>
#include <queue>
#include <fstream>
#include<vector>
#include<map>
#include <algorithm>

using namespace std;

vector<unsigned long> get_keys(map<unsigned long, unsigned long> m) {
    vector<unsigned long> v;
    for(map<unsigned long,unsigned long>::iterator it = m.begin(); it != m.end(); ++it) {
        v.push_back(it->first);
    }
    return v;
}

unsigned long stall(map<unsigned long,unsigned long> m, unsigned long K) {
    vector<unsigned long> keys = get_keys(m);
    unsigned long sum = 0;
    sort(keys.rbegin(), keys.rend());
    map<unsigned long,unsigned long> new_m;
    for(unsigned i=0; i < keys.size(); i++) {
        unsigned long val = m.find(keys[i])->second;
        if( val >= K )
            return keys[i];
        K -= val;
        unsigned long v = (keys[i]-1)/2, v1 = keys[i]/2;
        if(new_m.find(v) != new_m.end())
            new_m.find(v)->second = new_m.find(v)->second + val;
        else
            new_m.insert(make_pair(v, val));
        if(new_m.find(v1) != new_m.end())
            new_m.find(v1)->second = new_m.find(v1)->second + val;
        else
            new_m.insert(make_pair(v1, val));
    }
    return stall(new_m, K);
}

int main() {
    ofstream cop("op1.txt");
    ifstream cinp("in1.txt", ios::binary);
    int T, t=1;
    cinp >> T;
    for(;t <= T;t++){
        unsigned long N, K;
        cinp >> N >> K;
        map <unsigned long, unsigned long> m;
        m.insert(make_pair(N,1));
        unsigned long val = stall(m, K);
        if(val == 0)
            val = 1;
        cop << "Case #" << t << ": " << val/2 << " " << (val-1)/2 << endl;
    }
    return 0;
}
