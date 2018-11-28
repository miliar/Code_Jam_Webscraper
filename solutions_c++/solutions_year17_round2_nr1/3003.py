#include <iostream>
#include <fstream>
#include <stdexcept>
#include <vector>
#include <limits>
#include <iomanip>

using namespace std;

using size_type = string::size_type;
const auto infinity = numeric_limits<double>::max();

istream *getInStream(int argc, char **args, ifstream *infile) {
    if (argc == 1)
        return &cin;
    else {
        infile->open(args[1]);
        if (!infile->is_open())
            throw runtime_error(string("could not open file: ") + args[1]);
        return infile;
    }
}

int main(int argc, char **args) {
    int numTests;
    ifstream infile;
    istream &is(*getInStream(argc, args, &infile));
    // Read in number of tests
    is >> numTests;
    for (int testId = 1; testId <= numTests; ++testId) {
        cout << "Case #" << testId << ": ";
        // Read in parameters of the test
        double trackLen;
        size_type numHorses;
        size_type gridSize, numModels;
        is >> trackLen >> numHorses;
        // Solve test problem
        double timeToEnd = 0.0;

        for (size_type horseId = 0; horseId != numHorses; horseId++) {
            size_type horsePos, horseSpeed;
            is >> horsePos >> horseSpeed;
            auto distToEnd = trackLen - horsePos;
            double timeThisHorse = static_cast<double>(distToEnd)/horseSpeed;
            if (timeThisHorse > timeToEnd)
                timeToEnd = timeThisHorse;
        }
        auto annieSpeed = static_cast<double>(trackLen)/timeToEnd;

        // Output solution to test problem

        cout << setprecision(10) << fixed << annieSpeed << endl;

        // Now go back and pick up another test
    }
    return 0;
}
