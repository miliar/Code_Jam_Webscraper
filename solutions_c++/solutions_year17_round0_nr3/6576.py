#include <iostream>

bool accessStall(bool* stalls, int n, int i) {
    if (i == -1 || i == n)
        return true;
    return stalls[i];
}

int lDistCalc(bool* stalls, int n, int i) {
    int dist = 0;
    while (!accessStall(stalls, n, --i))
        dist++;
    return dist;
}

int rDistCalc(bool* stalls, int n, int i) {
    int dist = 0;
    while (!accessStall(stalls, n, ++i))
        dist++;
    return dist;
}

int min(int a, int b) {
    return a<b? a: b;
}

int max(int a, int b) {
    return a>b? a: b;
}

int main() {
    int t;
    std::cin >> t;

    for (int i = 0; i < t; i++) {
        int n, p;
        std::cin >> n >> p;

        bool *stalls = new bool[n];
        for (int j = 0; j < n; j++) {
            stalls[j] = false;
        }

        int idealStall;
        int minStallDist;
        int maxStallDist;

        for (int j = 0; j < p; j++) {
            idealStall = -1;
            minStallDist = -1;
            maxStallDist = -1;

//            std::cout << "Person " << j << std::endl;

            for (int k = 0; k < n; k++) {
                if (accessStall(stalls, n, k))
                    continue;

                int lDist = lDistCalc(stalls, n, k);
                int rDist = rDistCalc(stalls, n, k);

                int currMinStallDist = min(lDist, rDist);
                int currMaxStallDist = max(lDist, rDist);

//                std::cout << "Stall " << k << " ; l: " << lDist << " ; r: " << rDist << std::endl;

                if (currMinStallDist > minStallDist || (currMinStallDist == minStallDist && currMaxStallDist > maxStallDist)) {
                    idealStall = k;
                    minStallDist = currMinStallDist;
                    maxStallDist = currMaxStallDist;
                }
            }

            stalls[idealStall] = true;

//            std::cout << "Selected " << idealStall << std::endl;
        }

        std::cout << "Case #" << (i+1) << ": " << maxStallDist << " " << minStallDist << std::endl;
    }
}