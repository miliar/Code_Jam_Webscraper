#include <iostream>
#include <string>
#include <vector>
#include <tuple>

int calc_left_empty(const std::vector<bool>& stalls, int pos) {
    int i;
    for (i = pos; !stalls[i]; --i);
    return pos-i-1;
}

int calc_right_empty(const std::vector<bool>& stalls, int pos) {
    int i;
    for (i = pos; !stalls[i]; ++i);
    return i-pos-1;
}

int calc_max_stall(const std::vector<bool>& stalls, int pos) {
    int l = calc_left_empty(stalls, pos);
    int r = calc_right_empty(stalls, pos);
    return ((l > r) ? l : r);
}

int calc_min_stall(const std::vector<bool>& stalls, int pos) {
    int l = calc_left_empty(stalls, pos);
    int r = calc_right_empty(stalls, pos);
    return ((l < r) ? l : r);
}

std::tuple<int, int> populate_stalls(std::vector<bool>& stalls, int people) {
    std::vector<int> avaibleMin;
    std::vector<int> avaibleMax;
    int i, j, tempmax, tempmin, lastmax, lastmin;
    tempmax = tempmin = lastmax = lastmin = 0;
    /* Iterations for all empty stalls. */
    for (i = 0; i < stalls.size(); ++i) {
        if (!stalls[i]) {
            /* Populate minimums */
            tempmin = calc_min_stall(stalls, i);
            if (tempmin >= lastmin) {
                if (tempmin > lastmin) {
                    avaibleMin.clear();
                }
                lastmin = tempmin;
                avaibleMin.push_back(i);
            }
        }
    }
    /* Check minimums */
    if (avaibleMin.size() == 1) {
        lastmax = calc_max_stall(stalls, avaibleMin[0]);
        stalls[avaibleMin[0]] = true;
    }
    else {
        /* Populate maximums */
        for (j = 0; j < avaibleMin.size(); ++j) {
            tempmax = calc_max_stall(stalls, avaibleMin[j]);
            if (tempmax >= lastmax) {
                if (tempmax > lastmax) {
                    avaibleMax.clear();
                }
                lastmax = tempmax;
                avaibleMax.push_back(avaibleMin[j]);
            }
        }
        stalls[avaibleMax[0]] = true;
    }
    /* End function. */
    if (people == 1) {
        return std::make_tuple(lastmax, lastmin);
    }
    return populate_stalls(stalls, people - 1);
}

void initilize_stalls(std::vector<bool>& stalls, int stallNum) {
    int i;
    stalls.push_back(true);
    for (i = 0; i < stallNum; ++i) {
        stalls.push_back(false);
    }
    stalls.push_back(true);
}

int main() {
    int testCases, currentCase, i, stallNum, peopleNum;
    std::tuple<int, int> lastPos;
    std::string inpLine;
    std::vector<bool> stalls;
    std::getline(std::cin, inpLine);
    testCases = stoi(inpLine);
    inpLine.clear();
    for (currentCase = 0; currentCase < testCases; ++currentCase) {
        std::getline(std::cin, inpLine);
        for (i = 0; inpLine[i] != ' '; ++i);
        stallNum = std::stoi(inpLine.substr(0, i));
        peopleNum = std::stoi(inpLine.substr(i+1));
        stalls.reserve(stallNum+2);
        initilize_stalls(stalls, stallNum);
        lastPos = populate_stalls(stalls, peopleNum);
        std::cout << "Case #" << currentCase+1 << ": ";
        std::cout << std::get<0>(lastPos) << ' ' << std::get<1>(lastPos);
        std::cout << std::endl;
        stalls.clear();
        inpLine.clear();
    }
    return 0;
}