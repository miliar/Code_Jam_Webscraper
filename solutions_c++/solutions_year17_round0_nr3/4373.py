#include <algorithm>
#include <iostream>
#include <queue>
#include <list>
#include <map>
using namespace std;

typedef long long ll;


void handleCase(ll _left, ll _right, ll K) {
    struct SubProb {
        ll left;
        ll right;
        ll count;
        ll location;
        ll sizeLeft;
        ll sizeRight;
        bool better(SubProb &other) {
            ll size = (sizeLeft < sizeRight ? sizeLeft : sizeRight);
            ll otherSize = (other.sizeLeft < other.sizeRight ? other.sizeLeft : other.sizeRight);
            return size > otherSize;
        }
    };
    std::list<SubProb> queue;
    
    auto pushSubProblem = [&queue](ll left_, ll right_, ll count_) {
        if(left_ <= right_) {
            ll location_ = (right_-left_)/2 + left_;
            queue.push_back({left_, right_, count_, location_, location_ - left_, right_ - location_});
        }
    };
    
    pushSubProblem(_left, _right, 1);
    
    while(true) {
        auto bestIter = queue.begin();
        for(auto iter = queue.begin(); iter != queue.end(); iter++) {
            if(iter->better(*bestIter)) {
                bestIter = iter;
            }
        }
        
        SubProb p = std::move(*bestIter);
        queue.erase(bestIter);

        K -= p.count;
        
        if(K <= 0) {
            if(p.sizeLeft < p.sizeRight) std::swap(p.sizeLeft, p.sizeRight);
            std::cout << p.sizeLeft << " " << p.sizeRight << "\n";
            return;
        }
        
        if(p.sizeLeft == p.sizeRight) {
            pushSubProblem(p.left, p.location-1, p.count*2);
        } else {
            // favor the larger side first!
            if(p.sizeLeft > p.sizeRight) {
                pushSubProblem(p.left, p.location-1, p.count);
                pushSubProblem(p.location+1, p.right, p.count);
            } else {
                pushSubProblem(p.location+1, p.right, p.count);
                pushSubProblem(p.left, p.location-1, p.count);
            }
        }
    }
}


int main() {
    int T;
    std::cin >> T;
    
    for(int i = 1;i <= T; i++) {
        std::cout << "Case #" << i << ": ";
        ll N, K;
        std::cin >> N >> K;
        
        
        handleCase(1, N, K);
    }
    return 0;
}