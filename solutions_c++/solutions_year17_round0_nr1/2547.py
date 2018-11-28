#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

constexpr int SAD        = -1;
constexpr int HAPPY      = 1;
constexpr int IMPOSSIBLE = -1;

template <typename T>
size_t numBits(T num) {
    size_t bits = 0;
    while (num != 0) {
        bits += num % 2;
        num /= 2;
    }
    return bits;
}

template <typename T, typename U>
bool isBitSet(T byte, U bit) {
    return (byte & (1 << bit)) > 0;
}

int dynamicProgramming(vector<int> s, int k) {
    // where the actual head of our list to consider is, start with the full list
    int flips = 0;

    size_t head = 0;
    for (; head < s.size() - k + 1; ++head) {
        // {
        //     for (size_t i = head; i < s.size(); ++i) {
        //         cout << ((s[i] == HAPPY) ? '+' : '-');
        //     }
        //     cout << endl;
        // }

        // if head is + we can't flip it, else we must flip it
        if (s[head] == HAPPY) {
            continue;
        }

        // head is '-' means we must flip
        for (size_t i = head; i < head + k; ++i) {
            s[i] = -s[i];
        }
        ++flips;

        // {
        //     cout << "flip\n";
        //     for (size_t i = head; i < s.size(); ++i) {
        //         cout << ((s[i] == HAPPY) ? '+' : '-');
        //     }
        //     cout << endl;
        // }
    }

    if (head > 0) {
        --head;
    }
    // {
    //     cout << "last group\n";
    //     for (size_t i = head; i < s.size(); ++i) {
    //         cout << ((s[i] == HAPPY) ? '+' : '-');
    //     }
    //     cout << endl;
    // }
    // we should be left with the last size k
    // if they're all of 1 type then doable, else impossible
    auto lastC = s[head];
    for (auto i = head; i < s.size(); ++i) {
        if (s[i] != lastC)
            return IMPOSSIBLE;
    }
    return flips;
}

int bruteForce(const vector<int>& s, int k) {
    // guaranteed |s| < 10 so number of choices < 2^10
    auto choices     = s.size() - k + 1;
    size_t maxChoice = 1 << choices;

    int minFlips = IMPOSSIBLE;

    for (size_t choice = 0; choice < maxChoice; ++choice) {
        // {
        //     cout << choice << ":";
        //     // print choice bits
        //     for (int c = 0; c < (int)choices; ++c) {
        //         cout << isBitSet(choice, c);
        //     }
        //     cout << endl;
        // }

        auto bits = s;
        for (size_t bit = 0; bit < choices; ++bit) {
            // set following K bits
            if (isBitSet(choice, bit)) {
                for (size_t i = bit; i < bit + k; ++i) {
                    bits[i] = -bits[i];
                }
            }
        }

        // {
        //     // print happy or not
        //     for (const auto& b : bits) {
        //         cout << ((b == HAPPY) ? '+' : '-');
        //     }
        //     cout << endl << endl;
        // }

        // check if all happy
        bool allHappy = true;
        for (const auto& pancake : bits) {
            if (pancake == SAD) {
                allHappy = false;
            }
        }

        if (allHappy) {
            auto flips = numBits(choice);
            if (minFlips == IMPOSSIBLE || (int)flips < minFlips) {
                minFlips = flips;
            }
        }
    }

    return minFlips;
}

int main() {
    int T;
    cin >> T;

    for (int c = 1; c <= T; ++c) {
        string s;
        int k;
        cin >> s >> k;

        vector<int> bits;
        for (const char c : s) {
            if (c == '+') {
                bits.push_back(HAPPY);
            } else {
                bits.push_back(SAD);
            }
        }

        auto minFlips = dynamicProgramming(bits, k);

        cout << "Case #" << c << ": ";
        if (minFlips == IMPOSSIBLE) {
            cout << "IMPOSSIBLE";
        } else {
            stringstream ss;
            ss << minFlips;
            cout << ss.str();
        }
        cout << endl;
    }
}