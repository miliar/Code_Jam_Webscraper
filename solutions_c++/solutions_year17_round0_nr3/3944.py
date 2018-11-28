#include <iostream>
#include <set>
#include <vector>
#include <tuple>

typedef std::tuple<int, int, int> Answer;

int T, N, K;

void SmallTask() {
    std::set<int> BathSet;
    BathSet.insert(0);
    BathSet.insert(N + 1);
    for (int i = 0; i < K; i ++) {
        std::vector<int> BathVec;
        for (auto bath : BathSet) {
            BathVec.push_back(bath);
        }
        Answer k_answer(0, -1, 0);
        for (int i = 1; i < BathVec.size(); i ++) {
            int pos = (BathVec[i - 1] + BathVec[i]) / 2;
            Answer curr_answer(pos, pos - BathVec[i - 1] - 1, BathVec[i] - pos - 1);
            if (std::get<1>(k_answer) < std::get<1>(curr_answer)) {
                k_answer = curr_answer;
            } else if (std::get<1>(k_answer) == std::get<1>(curr_answer)) {
                if (std::get<2>(k_answer) < std::get<2>(curr_answer)) {
                    k_answer = curr_answer;
                }
            }
        }
        BathSet.insert(std::get<0>(k_answer));
        if (i == K - 1) {
            std::cout << std::get<2>(k_answer) << ' ' << std::get<1>(k_answer) << '\n';
        }
    }
}

void MiddelTask() {
    struct BathNode {
        int length, l, r;

        BathNode(int length, int l, int r) : length(length), l(l), r(r) {
        }

        bool operator < (const BathNode &next) const {
            if (length == next.length) {
                return l < next.l;
            }
            return length > next.length;
        }
    };
    std::set<BathNode> BathSet;
    BathSet.insert(BathNode(N + 1 - 0, 0, N + 1));
    for (int i = 0; i < K; i ++) {
        BathNode fbn = *BathSet.begin();
        int pos = (fbn.l + fbn.r) / 2;
        BathNode fbnr = BathNode(pos - fbn.l, fbn.l, pos);
        BathNode fbnl = BathNode(fbn.r - pos, pos, fbn.r);
        BathSet.erase(fbn);
        BathSet.insert(fbnr);
        BathSet.insert(fbnl);
        if (i == K - 1) {
            std::cout << (fbn.r - pos - 1) << ' ' << (pos - fbn.l - 1) << '\n';
        }
    }

}

void UnitTest(int CaseId) {
    std::cout << "Case #" << CaseId << ": ";
    std::cin >> N >> K;
 //   SmallTask();
    MiddelTask();
}

int main() {
    std::cin >> T;
    for (int i = 1; i <= T; i ++) {
        UnitTest(i);
    }
    return 0;
}
