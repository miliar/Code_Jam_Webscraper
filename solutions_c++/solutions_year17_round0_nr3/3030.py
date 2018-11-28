#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;


struct Case {
    uint64_t n;
    uint64_t numArrivals;
};

struct Outcome {
    uint64_t v1;
    uint64_t v2;
};


Case parseCase() {
    Case c;
    cin >> c.n >> c.numArrivals;
    cin.ignore(1);

    return c;
}


typedef list<uint64_t> Ranges;
typedef Ranges::const_iterator RangeNode;

bool compare(RangeNode &n1, RangeNode &n2) {
    return *n1 < *n2;
}

class Stalls {
public:
    Stalls(uint64_t n) {
        emptyRanges.push_back(n);
        maxSizes.push_back(emptyRanges.begin());
        make_heap(maxSizes.begin(), maxSizes.end(), compare);
    }

    friend ostream& operator<<(ostream& out, const Stalls &stalls);

    void handleArrival() {
        pop_heap(maxSizes.begin(), maxSizes.end(), compare);
        RangeNode node = maxSizes.back();
        
        // Find the leftmost maximal node
        if (*node == *maxSizes.front()) {
            const RangeNode realMax = find(emptyRanges.begin(), emptyRanges.end(), *node);
            const auto &realMaxHeapIter = find(maxSizes.begin(), maxSizes.end(), realMax);

            // Put our original node back on the heap
            *realMaxHeapIter = node;
            maxSizes.pop_back();

            // Set our node to be the real maximum
            node = realMax;
        } else {
            maxSizes.pop_back();
        }

        uint64_t newLeftRange = (*node - 1) / 2;
        uint64_t newRightRange = (*node) / 2;

        if (newLeftRange > 0) {
            RangeNode leftNode = emptyRanges.insert(node, newLeftRange);
            maxSizes.push_back(leftNode);
            push_heap(maxSizes.begin(), maxSizes.end(), compare);
        }

        if (newRightRange > 0) {
            RangeNode rightNode = emptyRanges.insert(node, newRightRange);
            maxSizes.push_back(rightNode);
            push_heap(maxSizes.begin(), maxSizes.end(), compare);
        }

        emptyRanges.erase(node);
        if (newLeftRange > newRightRange) {
            lastArrival.v1 = newLeftRange;
            lastArrival.v2 = newRightRange;
        } else {
            lastArrival.v1 = newRightRange;
            lastArrival.v2 = newLeftRange;
        }
    }

    Outcome getLastArrival() const {
        return lastArrival;
    }
    
private:
    Ranges emptyRanges;
    vector<RangeNode> maxSizes;
    Outcome lastArrival;
};

ostream& operator<<(ostream& out, const Outcome &outcome) {
    out << outcome.v1 << ' ' << outcome.v2 << endl;
    return out;
}

ostream& operator<<(ostream& out, const Stalls &stalls) {
    out << 'O';
    for (uint64_t range : stalls.emptyRanges) {
        for (uint64_t i = 0; i < range; i++) {
            out << '.';
        }
        out << 'O';
    }
    out << endl;
    return out;
}

Outcome solveCase(Case c) {
    Stalls stalls(c.n);
    for (size_t i = 0; i < c.numArrivals; i++) {
        //cerr << stalls;
        stalls.handleArrival();
        //cerr << stalls.getLastArrival();
    }
    return stalls.getLastArrival();
}

int main() {
    size_t numCases;
    cin >> numCases;
    cin.ignore(1);
    for (size_t i = 1; i <= numCases; i++) {
        Outcome outcome = solveCase(parseCase());
        cout << "Case #" << i << ": ";
        cout << outcome.v1 << ' ' << outcome.v2 << endl;
    }
}
