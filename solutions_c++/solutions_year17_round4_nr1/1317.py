#include <bits/stdc++.h>

void test(int t){
    int N, P;
    std::cin >> N >> P;
    
    int ans = 0;
    if(P == 2) {
        int ot = 0;
        for(int i=0; i<N; ++i) {
            int k; 
            std::cin >> k;
            if((k%P) == 0) ++ans;
            else {
                ++ot;
            }
        }
        ans += ot/2+ot%2;
    } else if (P == 3) {
        int ot[3];
        ot[0] = 0; ot[1] = 0; ot[2] = 0;
        for(int i=0; i<N; ++i) {
            int k; 
            std::cin >> k;
            if((k%P) == 0) ++ans;
            else {
                ++ot[k%P];
            }
        }
        
        int p = std::min(ot[1], ot[2]);
        ans += p;
        ot[1] -= p;
        ot[2] -= p;
        p = std::max(ot[1], ot[2]);
        if((p%3) != 0) ans++;
        ans += p/3;
        
    } else if (P == 4) {
        int ot[4];
        ot[0] = 0; ot[1] = 0; ot[2] = 0; ot[3] = 0;
        for(int i=0; i<N; ++i) {
            int k; 
            std::cin >> k;
            if((k%P) == 0) ++ans;
            else {
                ++ot[k%P];
            }
        }
        
        // combine 2
        ans += ot[2]/2;
        ot[2] = ot[2] % 2;
        // combine 1/3
        int p = std::min(ot[1], ot[3]);
        ans += p;
        ot[1] -= p;
        ot[3] -= p;
        // combine 2 and 1/3
        int r = std::max(ot[1], ot[3]);
        p = std::min(ot[2], r/2);
        r -= 2*p;
        ot[2] -= p;
        ans += p;
        // combine four times 1/3
        ans += r/4;
        // add last if it is there
        if((r%4) != 0 || ot[2]) ++ans;
    }
    
    std::cout << "Case #" << t << ": " << ans << std::endl;
}

int main() {
    int T;
    std::cin >> T;
    for(int i=1; i<=T; ++i) test(i);
}
