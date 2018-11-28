#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

template<class T>
inline T read() {
    T value;
    std::cin >> value;
    return value;
}

int N, R, O, Y, G, B, V;

std::string solve() {
    std::string result;
    result.reserve(N);
    if (R >= Y && R >= B) {
        // red is primary
        if (R > Y + B) {
            return "IMPOSSIBLE";
        }
        while (R > 0) {
            if (Y + B > R) {
                result.push_back('Y'); --Y;
                result.push_back('B'); --B;
            } else if (Y > 0) {
                result.push_back('Y'); --Y;
            } else if (B > 0) {
                result.push_back('B'); --B;
            }
            result.push_back('R'); --R;
        }
    } else if (Y >= R && Y >= B) {
        // yellow is primary
        if (Y > R + B) {
            return "IMPOSSIBLE";
        }
        while (Y > 0) {
            if (R + B > Y) {
                result.push_back('R'); --R;
                result.push_back('B'); --B;
            } else if (R > 0) {
                result.push_back('R'); --R;
            } else if (B > 0) {
                result.push_back('B'); --B;
            }
            result.push_back('Y'); --Y;
        }
    } else {
        // blue is primary
        if (B > R + Y) {
            return "IMPOSSIBLE";
        }
        while (B > 0) {
            if (R + Y > B) {
                result.push_back('R'); --R;
                result.push_back('Y'); --Y;
            } else if (R > 0) {
                result.push_back('R'); --R;
            } else if (Y > 0) {
                result.push_back('Y'); --Y;
            }
            result.push_back('B'); --B;
        }
    }
    return result;
}

int main() {
    auto T = read<int>();
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        std::cin >> N >> R >> O >> Y >> G >> B >> V;
        std::cout << "Case #" << caseNum << ": " << solve() << std::endl;
    }
    return 0;
}
