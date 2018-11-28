#include <iostream>
#include <string>
#include <queue>
#include <list>
#include <tuple>

using namespace std;

struct seat {
    long long pos;
    long long max;
    long long min;
    
    seat() = default;
    
    seat(const long long a, const long long b, const long long c) {
        pos = a;
        max = b;
        min = c;
    }
    
    bool operator< (const seat & b) const {
        if (min < b.min) {
            return true;
        } else if (min > b.min)
            return false;
        if (max < b.max) {
            return true;
        } else if (max > b.max)
            return false;
        return pos > b.pos;
    }
};

pair<seat, seat> split(seat & s) {
    seat s1, s2;
    
    s1.pos = s.pos - s.min + (s.min - 1) / 2;
    s2.pos = s.pos + (s.max+1) / 2;
    
    s1.min = s1.pos - (s.pos - s.min);
    s2.min = s2.pos - s.pos - 1;
    
    s1.max = s.pos - s1.pos - 1;
    s2.max = s.pos + s.max - s2.pos;
    
    return make_pair(s1, s2);
}

int main()
{
    int t;
    cin >> t;
    
    for (int i=1; i<=t; ++i) {
        long long n, k;
        cin >> n >> k;
        
        priority_queue<seat, vector<seat>> pq;
        
        pq.push( seat( n/2, n/2, (n-1)/2 ) );
        
        for (int j=0; j<k-1; j++) {
            seat s = pq.top();
            pq.pop();
            
            pair<seat, seat> p = split(s);
            
            pq.push(p.first);
            pq.push(p.second);
        }
        seat s = pq.top();
        cout << "Case #" << i << ": " << s.max << ' ' << s.min << endl;
    }

    return 0;
}
