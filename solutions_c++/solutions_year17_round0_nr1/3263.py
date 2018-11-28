#include <cstdlib>
#include <iostream>
#include <map>
#include <climits>

using namespace std;

void flip(string &s, long start, long K) {
    for(long i = start, n = start + K; i < n; ++i) {
        if(s[i] == '-') {
            s[i] = '+';
        }
        else {
            s[i] = '-';
        }
    }
}

bool sequence_ok(string &s) {
    for(long i = 0; i < s.size(); ++i) {
        if(s[i] == '-') {
            return false;
        }
    }
    
    return true;
}

map<string, long> visited;

long helper(string &current, long K) {
    long count_to_target = visited[current];
    if(count_to_target > 0) {
        return count_to_target;
    }
    visited[current] = LONG_MAX;
    
    long result;
    long min_result = LONG_MAX;
    
    for(long i = 0, n = current.size() - K + 1; i < n; ++i) {
        string *new_sequence = new string(current);
        flip(*new_sequence, i, K);

        result = helper(*new_sequence, K);
        if(result < LONG_MAX) {
            ++result;
            if(result > 0 && result < min_result) {
                min_result = result;
            }
        }
    }
    
    visited[current] = min_result;
    return min_result;
}

long solve(string &s, int K) {
    if(sequence_ok(s)) {
        return 0;
    }
    
    long i1, i2;
    i1 = s.size() - K;
    i2 = K - 1;
    if(i1 < i2) {
        for(long i = i1 + 1; i <= i2; ++i) {
            if(s[i] != s[i - 1]) {
                return LONG_MAX;
            }
        }
    }
    
    string target(s.length(), '+');
    visited[target] = 1;
    
    long result = helper(s, K);
    if(result == LONG_MAX) {
        return LONG_MAX;
    }
    
    return result - 1;
}

int main(int argc, char** argv) {
    int T;
    cin >> T;
    
    string s;
    int K;
    for(int i = 1; i <= T; ++i) {
        visited.clear();
        cin >> s >> K;
        
        cout << "Case #" << i << ": ";
        
        long result = solve(s, K);
        if(result == LONG_MAX) {
            cout << "IMPOSSIBLE";
        }
        else {
            cout << result;
        }
        
        cout << "\n";
    }
    
    return 0;
}

