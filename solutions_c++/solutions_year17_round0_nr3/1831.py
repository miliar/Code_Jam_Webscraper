#include <iostream>
#include <queue>

main() {
    int T;
    std::cin >> T;
    for(int t = 1; t <= T; t++) {
        std::cout << "Case #" << t << ": ";
        long long N, K;
        std::cin >> N >> K;
        long long peopleLeft = K - 1;
        long long bigGap = (long long) ((N)/2);
        long long smallGap = (long long) ((N-1)/2);
        long long bigCount = 1;
        long long smallCount = 1;
        if(bigGap == smallGap) {
            bigCount = 2;
            smallCount = 0;
        }
        long long level = 1;
        while((1LL<<level) < peopleLeft) {
            peopleLeft -= (1LL<<level);
            level++;
            long long newBig = (long long) ((bigGap) / 2);
            long long newSmall = (long long) ((smallGap - 1) / 2);
            if( (long long) ( (bigGap - 1) / 2 ) == newSmall ) {
                smallCount = 2 * smallCount + bigCount;
            } else {
                bigCount = 2 * bigCount + smallCount;
            }
            bigGap = newBig;
            smallGap = newSmall;

            if(bigGap == smallGap) {
                bigCount = bigCount + smallCount;
                smallCount = 0;
            }
        }
        if(peopleLeft == 0) {
            std::cout << bigGap << ' ' << smallGap << '\n';
        }
        else {
            if(bigCount >= peopleLeft) {
                std::cout << bigGap / 2 << ' ' << (bigGap - 1) / 2 << '\n';
            }
            else {
                std::cout << smallGap / 2 << ' ' << (smallGap - 1) / 2 << '\n';
            }
        }
    }
    return 0;
}
