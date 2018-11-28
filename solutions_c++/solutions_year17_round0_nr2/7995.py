//
// Created by Explo on 4/7/2017.
//

#ifndef CODEJAMPROJECTS_TIDYNUMBER_H
#define CODEJAMPROJECTS_TIDYNUMBER_H

#include <string>

class TidyNumber {
private:

    // 55554
    // 49999
    // size = 5
    // last index = 4
public:
    std::string solve(const std::string& original) {
        if (isTidy(original))
            return original;

        std::string max = "";
        char topChar = '0';
        std::string precedent = "";

        for (unsigned i = 0; i < original.size(); i++) {
            if (topChar > original.at(i))
                break;


            char frontChar;

            if (i == original.size() - 1) {
                frontChar = original.at(i);
                max = maxOfTwoStrings(max, std::string(1, frontChar));
            } else if (original.at(i) > '1') {
                frontChar = original.at(i);
                frontChar--;
                if (frontChar >= topChar) {
                    std::string temp = precedent + frontChar + std::string(original.size() - i - 1, '9');
                    max = maxOfTwoStrings(max, temp);
                }
            } else if (original.at(i) > '0') {
                std::string temp = precedent + std::string(original.size() - i - 1, '9');
                max = maxOfTwoStrings(max, temp);
            } else {
                //nothing?
            }

            if (topChar < original.at(i))
                topChar = original.at(i);

            precedent += original.at(i);
        }

        return max;
    }

private:
    bool isTidy(const std::string& str) {
        char top = '0';
        for (int i = 0; i < str.size(); i++) {
            if (str.at(i) < top) {
                return false;
            }
            if (str.at(i) > top) {
                top = str.at(i);
            }
        }

        return true;
    }

    std::string maxOfTwoStrings(const std::string& rhs, const std::string& lhs) {
        if (rhs.size() > lhs.size()) {
            return rhs;
        } else if (rhs.size() < lhs.size()) {
            return lhs;
        } else {
            for (unsigned i = 0; i < rhs.size();i++) {
                if (rhs.at(i) > lhs.at(i)) {
                    return rhs;
                } else if (rhs.at(i) < lhs.at(i)) {
                    return lhs;
                }
            }
            return rhs;
        }
    }
};

#endif //CODEJAMPROJECTS_TIDYNUMBER_H
