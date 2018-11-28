#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cmath>

struct A {
    int start;
    int end;
    char who;
};

const int M = 1440;

bool operator< (const A& a1, const A& a2) {
    return (a1.start + M) % M <= (a2.start + M) % M;
}

int main(int argc, char** argv) {
    int T;
    std::cin >> T;
    for (int i = 0; i < T; ++i) {
        int64_t Ac, Aj;
        std::cin >> Ac >> Aj;
        std::vector<A> ac(Ac);
        std::vector<A> aj(Aj);
        std::vector<A> a(Aj + Ac);
        int tj(720);
        int tc(720);
        for (int j = 0; j < Ac; ++j) {
            std::cin >> a[j].start >> a[j].end;
            a[j].who = 'c';
            tc -= (a[j].end - a[j].start);
        }
        for (int j = 0; j < Aj; ++j) {
            std::cin >> a[Ac + j].start >> a[Ac + j].end;
            a[Ac + j].who = 'j';
            tj -= (a[Ac + j].end - a[Ac + j].start);
        }
        std::sort(a.begin(), a.end());
        int changes(0);
        std::vector<int> removableC;
        std::vector<int> removableJ;
        for (size_t j = 0; j < a.size(); ++j) {
            //std::cerr << "who: " << a[j].who << " " << a[(j+1) % a.size()].who << std::endl;
            if (a[j].who != a[(j+1) % a.size()].who) {
                //std::cerr << "+" << std::endl;
                changes++;
            } else {
                if (a[(j+1) % a.size()].start == a[j].end)
                    continue;
                if (a[j].who == 'j')
                    removableJ.push_back(((a[(j+1) % a.size()].start < a[j].end) ? M : 0) +  a[(j+1) % a.size()].start - a[j].end);
                else
                    removableC.push_back(((a[(j+1) % a.size()].start < a[j].end) ? M : 0) +  a[(j+1) % a.size()].start - a[j].end);
                //std::cerr << "++" << std::endl;
                changes += 2;
            }
        }
        //std::cerr << "changes: " << changes << std::endl;
        std::sort(removableC.begin(), removableC.end());
        std::sort(removableJ.begin(), removableJ.end());
        for (auto& r : removableC) {
            if (r <= tc) {
                tc -= r;
                changes -= 2;
            }
            else {
                break;
            }
        }
        for (auto& r : removableJ) {
            if (r <= tj) {
                tj -= r;
                changes -= 2;
            }
            else {
                break;
            }
        }
        std::cout << "Case #" << (i + 1) << ": " << changes << std::endl;
    }
}
