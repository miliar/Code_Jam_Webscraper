#include <iostream>

int main(){
    //std::ios::sync_with_stdio(false);
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small.out", "w", stdout);

    int T, N, P;
    int remainder[4];
    std::cin >> T;
    for(int t = 1; t <= T; t++){
        int ans = 0;
        for(int i = 0; i < 4; i++) remainder[i] = 0;

        std::cin >> N >> P;
        for(int i = 0, input; i < N; i++){
            std::cin >> input;
            remainder[input%P]++;
        }

        ans = remainder[0];
        switch(P){
        case 2:
            ans += (remainder[1]+1)/2;
            break;
        case 3:
            int groups = std::min(remainder[1], remainder[2]);
            int remnants = std::max(remainder[1], remainder[2]) - groups;

            ans += groups + (remnants + 2)/3;
            break;
        }

        std::cout << "Case #" << t << ": " << ans << "\n";
    }
}
