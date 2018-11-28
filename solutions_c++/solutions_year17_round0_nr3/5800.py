#include <iostream>
#include <utility>

using namespace std;

long min(long a, long b) {
    if (a < b) {
        return a;
    }
    
    return b;
}

long max(long a, long b) {
    if (a > b) {
        return a;
    }
    
    return b;
}

string initialState(long n) {
    string stalls = "o";
    
    for (long i = 0; i < n; i++) {
        stalls.push_back('.');
    }
    
    stalls.push_back('o');
    
    return stalls;
}

long emptyStallsToTheLeft(string stalls, long i) {
    long index = i - 1;
    long count = 0;
    
    while (stalls[index] != 'o') {
        count++;
        index--;
    }
    
    return count;
}

long emptyStallsToTheRight(string stalls, long i) {
    long index = i + 1;
    long count = 0;
    
    while (stalls[index] != 'o') {
        count++;
        index++;
    }
    
    return count;
}

bool changePair(pair<long, long> current, pair<long, long> newPair) {
    long newMin = min(newPair.first, newPair.second);
    long currentMin = min(current.first, current.second);
    
    long newMax = max(newPair.first, newPair.second);
    long currentMax = max(current.first, current.second);
    
    if (newMin > currentMin) {
        return true;
    } else if (newMin == currentMin) {
        if (newMax > currentMax) {
            return true;
        }
    }
    
    return false;
}

pair<long, long> findStall(string &stalls) {
    pair<long, long> bestStall(stalls.size(), stalls.size());
    long bestIndex = 0;
    
    //cout << "  Current stalls: " << stalls << endl;
    
    for (long i = 0; i < stalls.size(); i++) {
        if (stalls[i] == 'o') {
            continue;
        }
        
        long leftS = emptyStallsToTheLeft(stalls, i);
        long rightS = emptyStallsToTheRight(stalls, i);
        
        //cout << "    New pair: <" << leftS << ", " << rightS << ">" << endl;
        pair<long, long> candidate(leftS, rightS);
        
        if (changePair(bestStall, candidate) || bestStall.first == stalls.size()) {
            //cout << "    Changing pair! [" << i << "]" << endl;
            bestStall = candidate;
            bestIndex = i;
        }
    }
    
    stalls[bestIndex] = 'o';
    
    return bestStall;
}

void solve(long n, long k) {
    if (n == k) {
        cout << "0 0" << endl;
        return;
    }
    
    string stalls = initialState(n);
    pair<long, long> last(-1, -1);
    
    for (long i = 0; i < k; i++) {
        last = findStall(stalls);
    }
    
    long lastMin = min(last.first, last.second);
    long lastMax = max(last.first, last.second);
    
    cout << lastMax << " " << lastMin << endl;
}

int main(int argc, const char * argv[]) {
    
    int t;
    cin >> t;
    
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        
        long n;
        cin >> n;
        
        long k;
        cin >> k;
        
        solve(n, k);
    }
    
    
    return 0;
}
