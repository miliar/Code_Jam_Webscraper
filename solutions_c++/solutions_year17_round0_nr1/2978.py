#include <iostream>
#include <string>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;


struct Case {
    vector<bool> pancakes;
    unsigned size;

    bool isSolved() const {
        return all_of(pancakes.begin(), pancakes.end(), [](bool i){return i;});
    }
    unsigned lastFlipIndex() const {
        return pancakes.size() - size;
    }
    void flip(unsigned index) {
        assert(index >= 0);
        assert(index + size <= pancakes.size());
        for (unsigned i = index; i < index + size; i++) {
            pancakes[i] = !pancakes[i];
        }
    }
};

ostream& operator<< (ostream& os, const Case &c) {
    for (const bool& b : c.pancakes) {
        os << (b ? '+' : '-');
    }
    return os;
}

Case parseCase() {
    Case c;
    string pancakeString;
    getline(cin, pancakeString, ' ');
    cin >> c.size;
    cin.ignore(1);

    c.pancakes.reserve(pancakeString.length());
    for (const char &p : pancakeString) {
        c.pancakes.push_back(p == '+');
    }
    return c;
}

int solveCaseRecursive(Case *c, unsigned start) {
    if (c->isSolved()) {
        return 0;
    }
    if (start > c->lastFlipIndex()) {
        return -1;
    }

    int outcome = -1;
    if (c->pancakes[start]) {
        outcome = solveCaseRecursive(c, start + 1);
        if (outcome != -1) {
            return outcome;
        }
    } else {
        c->flip(start);
        outcome = solveCaseRecursive(c, start + 1);
        if (outcome != -1) {
            cerr << start << ' ';
            return outcome + 1;
        }
        c->flip(start);
    }
    return -1;
}

bool passesSolveHeuristics(Case *c) {
    unsigned start = c->pancakes.size() - c->size;
    unsigned end = c->size;
    bool firstPancake = c->pancakes[start];
    for (unsigned i = start + 1; i < end; i++) {
        if (firstPancake != c->pancakes[i]) {
            return false;
        }
    }
    return true;
}

int solveCase(Case c) {
    cerr << c << endl;
    if (c.isSolved()) {
        return 0;
    }

    if (!passesSolveHeuristics(&c)) {
        return -1;
    }
    return solveCaseRecursive(&c, 0);
}

int main() {
    size_t numCases;
    cin >> numCases;
    cin.ignore(1);
    for (size_t i = 1; i <= numCases; i++) {
        int outcome = solveCase(parseCase());
        cerr << endl;
        cout << "Case #" << i << ": ";
        if (outcome == -1) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << outcome << endl;
        }
    }
}
