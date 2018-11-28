#include <iostream>
#include <string>
#include <vector>

void flip_pancakes(std::vector<bool>& pancakes, int from, int to) {
    int i;
    for (i = from; i < to; ++i) {
        pancakes[i] = !pancakes[i];
    }
}

bool all_happy(const std::vector<bool>& pancakes) {
    int i = 0;
    int size = pancakes.size();
    while (i < size) {
        if (!pancakes[i++]) {
            return false;
        }
    }
    return true;
}

int calculate_moves(std::vector<bool>& pancakes, int flipLength) {
    int i, size, moveCount;
    size = pancakes.size();
    moveCount = 0;
    for (i = 0; i + flipLength <= size; ++i) {
        if (!pancakes[i]) {
            flip_pancakes(pancakes, i, i+flipLength);
            ++moveCount;
        }
    }
    if (all_happy(pancakes)) {
        return moveCount;
    }
    return -1;
}

int populate_pancakes(std::vector<bool>& pancakes, std::string& inpLine) {
    int i;
    for (i = 0; inpLine[i] != ' '; ++i) {
        if (inpLine[i] == '+') {
            pancakes.push_back(true);
        }
        else {
            pancakes.push_back(false);  
        }
    }
    return i;
}

int main() {
    int testCases, flipLength, spaceLocation, currentCase, moves;
    std::vector<bool> pancakes;
    std::string inpLine;
    std::getline(std::cin, inpLine);
    testCases = stoi(inpLine);
    inpLine.clear();
    for (currentCase = 0; currentCase != testCases; ++currentCase) {
        std::getline(std::cin, inpLine);
        pancakes.reserve(inpLine.length() - 2);
        spaceLocation = populate_pancakes(pancakes, inpLine);
        flipLength = std::stoi(inpLine.substr(spaceLocation+1));
        moves = calculate_moves(pancakes, flipLength);
        std::cout << "Case #" << currentCase+1 << ": ";
        if (moves < 0) {
            std::cout << "IMPOSSIBLE";
        }
        else {
            std::cout << moves; 
        }
        std::cout << std::endl;
        inpLine.clear();
        pancakes.clear();
    }
    return 0;
}