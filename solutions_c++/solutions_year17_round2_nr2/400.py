#include <bits/stdc++.h>

struct Color {
    char c;
    int k;
};

void test(int t) {
    int N, R, O, Y, G, B, V;
    
    std::cin >> N >> R >> O >> Y >> G >> B >> V;
    
    assert(O == 0 && G == 0 && V == 0);
    
    std::priority_queue<std::pair<double, char>> pq;
    pq.push(std::make_pair(R-0.1, 'R'));
    pq.push(std::make_pair(Y-0.1, 'Y'));
    pq.push(std::make_pair(B-0.1, 'B'));
    
    std::string ans;
    std::cout << "Case #" << t << ": ";
    
    std::pair<double, char> op = std::make_pair(-1, 0);
    bool first = true;
    for(int i=0; i<N; ++i){
        auto pr = pq.top();
        pq.pop();
        
        if(pr.first < 0){
            std::cout << "IMPOSSIBLE" << std::endl;
            return;
        }
        
        if(op.first != -1) {
            if(first) pq.push(std::make_pair(op.first-0.9, op.second));
            else pq.push(std::make_pair(op.first-1, op.second));
            first = false;
        }
        
        ans += pr.second;
        
        op = pr;
    }
    
    if(ans.back() == ans.front()) {
        std::cout << "IMPOSSIBLE" << std::endl;
        return;
    }
    
    std::cout << ans << std::endl;
}

int main() {
    int T;
    std::cin >> T;
    for(int i=1; i<=T; ++i) {
        test(i);
    }
}
