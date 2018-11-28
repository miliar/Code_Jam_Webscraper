#include <cmath>
#include <cstdio>
#include <vector>
#include <queue>
#include <iterator>
#include <numeric>
#include <memory>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <cstring>
#include <climits>
#include <iostream>
#include <algorithm>

// #define DEBUG
using namespace std;

struct pancakes{
    int len;
    uint8_t * data;
    string s;

    pancakes(int len, uint8_t * data){
        this->len = len;
        this->data = new uint8_t[len];
        int i;
        for (i = 0; i < len; ++i) {
            this->data[i] = data[i];
        }
        this->s =  string((char *)this->data, len);
    }

    pancakes(int len, string s){
        this->len = len;
        this->data = new uint8_t[len];
        int i;
        for (i = 0; i < len; ++i) {
            this->data[i] = (s[i] == '+') ? 1 : 0;
        }
        this->s =  string((char *)this->data, len);
    }

    string get_string() const {
        return s;
    }

    ~pancakes(){
        // delete data;
    }

    bool operator == (const pancakes & a) const{
        return a.get_string() == get_string();
    }

    int get_largest_consec(){
        int pancakes_consec[len];
        pancakes_consec[0] = !data[0];
        int i;
        int maximum_consec = pancakes_consec[0], maximum_index = 0;
        for (i = 1; i < len; ++i) {
            if (data[i] == 0) {
                pancakes_consec[i] = pancakes_consec[i-1] + 1;
                if (pancakes_consec[i] > maximum_consec) {
                    maximum_consec = pancakes_consec[i];
                    maximum_index = i;
                }
            } else {
                pancakes_consec[i] = 0;
            }
        }
        if (maximum_consec == 0) {
            // done
            return -1;
        }
        return maximum_index - maximum_consec + 1;
    }

    pancakes flip(int index, int K){
        uint8_t t[len];
        int i;
        for (i = 0; i < len; ++i) {
            t[i] = this->data[i];
        }
        for (i = index; i < index+K; ++i) {
            t[i] = !t[i];
        }
        return pancakes(this->len, t);
    }
};

int DONE = false;
pancakes greedy_flip(pancakes orig, int K){
    int index = orig.get_largest_consec();
    if (index == -1) {
        DONE = true;
        return orig;
    }
    index = max(0, index);
    if (index + K > orig.len) {
        index = orig.len - K;
    }
    #ifdef DEBUG
    cout << "flip start " << index << endl;
    #endif
    return orig.flip(index, K);
}

namespace std {

    template <>
        struct hash<pancakes>
        {
            std::size_t operator()(const pancakes& k) const
            {
                return hash<string>()(k.get_string());
            }
        };
}

void solve(int Tn){
    int ans = 0;

    string s;
    cin >> s;
    int K;
    cin >> K;

    int len = s.length();
    pancakes initial = pancakes(len, s);

#ifdef DEBUG
    cout << "input: " <<  s << endl;
#endif

    unordered_set<struct pancakes> set_p;

    set_p.insert(initial);
    DONE = false;
    while (true) {
        initial = greedy_flip(initial, K);
        if (DONE) {
            break;
        }
        if (set_p.find(initial) == set_p.end()) {
            set_p.insert(initial);
        } else {
            break;
        }
        ans +=1;
    }

    cout << "Case #" << Tn + 1 << ": ";
    if (DONE) {
        cout << ans << endl;
    } else {
        cout << "IMPOSSIBLE" << endl;
    }
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int T;
    cin >> T;

    int i;
    for (i = 0; i < T; ++i) {
        solve(i);
    }
    return 0;
}

