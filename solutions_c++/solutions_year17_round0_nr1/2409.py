#include <cstdio>
#include <vector>
#include <string>

void flip(char& pancake) {
    if (pancake == '+') {
        pancake = '-';
    } else {
        pancake = '+';
    }
}

int flip(std::string pancakes, unsigned flipperSize) {

    unsigned flips = 0;
    for (unsigned flipStart = 0;
            flipStart + flipperSize <= pancakes.size();
            ++flipStart) {
        if (pancakes[flipStart] == '+') {
            continue;
        }
        for (unsigned i=0; i<flipperSize; ++i) {
            flip(pancakes[flipStart+i]);
        }
        ++flips;
    }

    for (unsigned i=pancakes.size()-flipperSize+1; i<pancakes.size(); ++i) {
        if (pancakes[i] == '-') {
            return -1;
        }
    }

    return flips;
}


int main(int argc, char **argv) {

    unsigned T;
    scanf("%u\n",&T);
    for (unsigned i=0; i<T; ++i) {
        char buf[1001];
        unsigned K;

        scanf("%s\n",buf);
        scanf("%u\n",&K);

        int flips = flip(buf,K);

        if (flips < 0) {
            printf("Case #%u: IMPOSSIBLE\n",i+1);
        } else {
            printf("Case #%u: %d\n",i+1,flips);
        }
    }

    return 0;
}







