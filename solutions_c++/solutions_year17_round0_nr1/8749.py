#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ullong;
void pancakeManeuvers(string pancakes, int flipperSize, long& maneuvers);
string flipFromPos(string pancakes, int flipperSize);

int main() {
    std::ifstream infile("A-large.in");
    if (infile) {
        ullong numCases;
        infile >> numCases;
        vector<pair<string, int>> testCases;
        for (ullong i = 0; i < numCases; i++) {
            string pancakes;
            int flipperSize;
            infile >> pancakes >> flipperSize;
            testCases.push_back(make_pair(pancakes, flipperSize));
        }

        std::ofstream outfile("A-large-solution.txt");

        for (ullong i = 0; i < testCases.size(); i++) {
            long maneuvers = 0;
            pancakeManeuvers(testCases[i].first, testCases[i].second, maneuvers);
            if(maneuvers >= 0) {
                outfile << "Case #" << i + 1 << ": " << maneuvers << endl;
            }
            else {
                outfile << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
            }
        }

        outfile.close();
        infile.close();
    }
    return 0;
}

void pancakeManeuvers(string pancakes, int flipperSize, long& maneuvers) {
    if(!pancakes.length())
    {
        return;
    }

    if(pancakes.length() < flipperSize) {
        for(int i = 0; i < pancakes.length(); i++) {
            if(pancakes[i] == '-') {
                maneuvers = -1;
                // a sad but flipper too big
                return;
            }
        }
        // all remaining happy
        return;
    }

    string newPancakes(pancakes);
    if(pancakes.back() == '-') {
        if(pancakes.length() - flipperSize >= 0)
        {
            newPancakes = flipFromPos(newPancakes, flipperSize);
            maneuvers++;
        }
    }

    pancakeManeuvers(newPancakes.substr(0, newPancakes.length() - 1), flipperSize, maneuvers);
}

string flipFromPos(string pancakes, int flipperSize)
{
    for(int i = 0, index = pancakes.length() - 1; i < flipperSize; i++) {
        char c = pancakes[index - i];
        if(c == '-') {
            c = '+';
        }
        else {
            c = '-';
        }

        pancakes[index - i] = c;
    }
    return pancakes;
}