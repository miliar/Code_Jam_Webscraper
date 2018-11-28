#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ullong;

struct Stall {
    pair<ullong, ullong> clear;
    ullong index;
    ullong min;
    ullong max;
    char occupied;

    Stall() : occupied('.') {}

    Stall(const Stall &obj) {
        clear = obj.clear;
        index = obj.index;
        min = obj.min;
        max = obj.max;
        occupied = obj.occupied;
    }

};

void updateStalls(std::vector<Stall> &stalls, ullong index);

ullong findBestStalls(std::vector<Stall> stalls);

int main() {
    std::ifstream infile("C-small-1-attempt0.in");
    if (infile) {
        ullong numCases;
        infile >> numCases;
        std::vector<pair<ullong, ullong>> testCases(numCases);
        for (ullong i = 0; i < numCases; i++) {
            ullong numStalls, numPeople;
            infile >> numStalls >> numPeople;
            testCases[i] = make_pair(numStalls, numPeople);
        }

        std::ofstream outfile("C-small-1-solution.txt");

        for (ullong i = 0; i < testCases.size(); i++) {
            if (testCases[i].first == testCases[i].second) {
                outfile << "Case #" << i + 1 << ": 0 0" << std::endl;
                continue;
            }

            std::vector<Stall> stalls(testCases[i].first + 2);
            for (ullong j = 0; j < stalls.size(); j++) {
                stalls[j].index = j;
            }
            updateStalls(stalls, 0);
            updateStalls(stalls, stalls.size() - 1);

            ullong maxLast, minLast;
            for (ullong person = 0; person < testCases[i].second; person++) {
                ullong stallIndex = findBestStalls(stalls);
                updateStalls(stalls, stallIndex);
                if (person + 1 == testCases[i].second) {
                    maxLast = stalls[stallIndex].max;
                    minLast = stalls[stallIndex].min;
                }
            }
            outfile << "Case #" << i + 1 << ": " << maxLast << " " << minLast << endl;
        }

        outfile.close();
        infile.close();
    }
    return 0;
}

ullong findBestStalls(std::vector<Stall> stalls) {
    stalls.erase(remove_if(stalls.begin(), stalls.end(), [](const Stall &s) {
        return s.occupied == 'O';
    }), stalls.end());

    sort(stalls.begin(), stalls.end(), [](Stall a, Stall b) {
        return a.min > b.min;
    });

    if (stalls[0].min > stalls[1].min) {
        return stalls[0].index;
    }

    // remove all with min < index 0
    stalls.erase(remove_if(stalls.begin(), stalls.end(), [=](const Stall &s) -> bool {
        return s.min != stalls[0].min;
    }), stalls.end());

    sort(stalls.begin(), stalls.end(), [](Stall a, Stall b) {
        return a.max > b.max;
    });
    if (stalls[0].max > stalls[1].max) {
        return stalls[0].index;
    }
    // remove all with max < index 0
    stalls.erase(remove_if(stalls.begin(), stalls.end(), [=](const Stall &s) -> bool {
        return s.max != stalls[0].max;
    }), stalls.end());
    ullong index = stalls[0].index;
    for (auto i = 0; i < stalls.size(); i++) {
        if (stalls[i].index < stalls[0].index) {
            index = stalls[i].index;
        }
    }
    return index;
}

void updateStalls(std::vector<Stall> &stalls, ullong index) {
    stalls[index].occupied = 'O';
    for (ullong s = 0; s < stalls.size(); s++) {
        ullong clearLeft = 0, clearRight = 0;
        if (s - 1 < 0) {
            stalls[s].clear.first = 0;
        } else {
            for (ullong left = s - 1; left >= 0; left--) {
                if (stalls[left].occupied == '.') {
                    clearLeft++;
                } else {
                    break;
                }
            }
        }
        if (s + 1 == stalls.size()) {
            stalls[s].clear.second = 0;
        } else {
            for (ullong right = s + 1; right < stalls.size(); right++) {
                if (stalls[right].occupied == '.') {
                    clearRight++;
                } else {
                    break;
                }
            }
        }
        stalls[s].clear = make_pair(clearLeft, clearRight);
        stalls[s].min = min(stalls[s].clear.first, stalls[s].clear.second);
        stalls[s].max = max(stalls[s].clear.first, stalls[s].clear.second);
    }
}