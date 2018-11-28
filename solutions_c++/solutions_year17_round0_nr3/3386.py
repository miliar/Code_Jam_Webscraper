#include <bits/stdc++.h>
using namespace std;

int t, n, k;

class Interval {
public:
    int x, y;

    Interval() {
        x = 1;
        y = -1;
    }

    Interval(int x, int y) {
        this->x = x;
        this->y = y;
    }

    int mid() const {
        return (x+y) / 2;
    }

    int size() const {
        return y - x - 1;
    }

    int minDist() const {
        return min(leftHalf().size(), rightHalf().size());
    }

    int maxDist() const {
        return max(leftHalf().size(), rightHalf().size());
    }

    Interval leftHalf() const {
        return Interval(x, mid());
    }

    Interval rightHalf() const {
        return Interval(mid(), y);
    }

    bool operator<(const Interval& other) const {
        if(minDist() != other.minDist())
            return minDist() < other.minDist();

        if(maxDist() != other.maxDist())
            return maxDist() < other.maxDist();

        return mid() > other.mid();
    }

};

Interval solve(int n, int k) {
    multiset <Interval> intervals;
    intervals.insert(Interval(0, n+1));

    Interval chosenInterval;
    for(int user=1; user<=k; user++) {
        chosenInterval = *(intervals.rbegin());
        intervals.erase(chosenInterval);

        if(chosenInterval.leftHalf().size() > 0)
            intervals.insert(chosenInterval.leftHalf());

        if(chosenInterval.rightHalf().size() > 0)
            intervals.insert(chosenInterval.rightHalf());
    }

    return chosenInterval;
}

int main() {
    cin>>t;

    for(int test=1; test<=t; test++) {
        cin>>n>>k;

        Interval kth = solve(n, k);

        cout<<"Case #"<<test<<": "<<kth.maxDist()<<" "<<kth.minDist()<<"\n";
    }

    return 0;
}
