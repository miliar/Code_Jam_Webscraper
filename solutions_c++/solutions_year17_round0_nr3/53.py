//
// Created by XelaPi.
//
#include <iostream>
#include <map>

using namespace std;

int main() {

    int num;

    cin >> num;

    for (int i = 0; i < num; i++) {
        cout << "Case #" << (i + 1) << ": ";

        unsigned long long stalls, people;

        cin >> stalls;
        cin >> people;

        map<unsigned long long, unsigned long long> numberQueue;

        numberQueue[stalls] = 1;

        unsigned long long left, right;

        unsigned long long numDecided = 0;

        while (numDecided < people) {
            auto biggest = numberQueue.rbegin();

            unsigned long long numEmpty = biggest->first;
            unsigned long long decisions = biggest->second;
            numberQueue.erase(biggest->first);

            left = (numEmpty - 1) / 2;
            right = numEmpty - 1 - left;

            auto previousAmountLeft = numberQueue.find(left);

            if (previousAmountLeft == numberQueue.end()) {
                numberQueue[left] = decisions;
            } else {
                numberQueue[left] += decisions;
            }

            auto previousAmountRight = numberQueue.find(right);

            if (previousAmountRight == numberQueue.end()) {
                numberQueue[right] = decisions;
            } else {
                numberQueue[right] += decisions;
            }

            numDecided += decisions;
        }

        cout << right << " " << left << endl;
    }

    return 0;
}