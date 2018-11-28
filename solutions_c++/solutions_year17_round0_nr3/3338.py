#include <bits/stdc++.h>
#include <iostream>     // std::cout
#include <algorithm>    // std::min
//
//struct sort_pred {
//    bool operator()(const std::pair<int, int> &left, const std::pair<int, int> &right) {
//        return min(left.second - left.first, left.first + CURRENT_SIZE - left.second) <
//               min(right.second - right.first, right.first + CURRENT_SIZE - right.second);
//    }
//};
using namespace std;
long long int N,K,CURK;

struct classcomp {
    bool operator() (const long long int& lhs, const long long int& rhs) const
    {return lhs<rhs;}
};
long long value, key, ares, bres;

int main() {

    freopen("in", "r", stdin);
    puts("START");
    freopen("out", "w", stdout);
    int tt;
    scanf("%d", &tt);
    for (int qq = 1; qq <= tt; qq++) {
        printf("Case #%d: ", qq);

        cin >> N>> K;
        CURK=K;
        map<long long int, long long int, classcomp> squashmap;

        squashmap[N]=1;

        while(CURK>0) {
            key = squashmap.rbegin()->first;
            value = squashmap.rbegin()->second;
            squashmap.erase(key);
            ares = key/2;
            bres=ares;
            if(key%2==0) {
                bres--;
            }

            if(CURK<=value) {
            // TODO set value
                break;
            }
            CURK -=value;
            if(squashmap.count(ares)==0) {
                squashmap[ares]=value;
            } else {
                squashmap[ares]= squashmap[ares] + value;
            }

            if(squashmap.count(bres)==0) {
                squashmap[bres]=value;
            } else {
                squashmap[bres]= squashmap[bres] + value;
            }



        }


        printf("%lld %lld\n", ares,bres);

    }
    return 0;
}