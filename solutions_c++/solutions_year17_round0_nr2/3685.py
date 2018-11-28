#include <iostream>
#include <vector>
#include <string>

long long getBest(long long a) {
    std::string num = "";

    while(a > 0) {
        int rem = a % 10; a /= 10;
        num = char('0' + rem) + num;
    }
    std::vector< std::vector<long long> > dp(10, std::vector<long long> (2, -1));
    dp[0][0] = 0;
    for(int passed = 0; passed < num.size(); passed++) {
        std::vector < std::vector<long long> > ndp(10, std::vector<long long> (2, 0));
        for(int last = 0; last < 10; last++) {
            for(int less = 0; less < 2; less++) {
                if (dp[last][less] == -1) continue;
                int newDigit = num[passed] - '0';
                for(int nxt = last; nxt < 10; nxt++) {
                    if (!less && nxt > newDigit) continue;
                    else ndp[nxt][less | (nxt < newDigit)] = std::max(ndp[nxt][less | (nxt < newDigit)], dp[last][less] * 10ll + nxt);
                }
            }
        }
        dp = ndp;
    }

    long long ans = 0;
    for(int last = 0; last < 10; last++) {
        for(int less = 0; less < 2; less++) {
            if (dp[last][less] > ans) {
                ans = dp[last][less];
            }
        }
    }
    return ans;
}

int main() {
    int T; std::cin >> T; int test_id = 0;
    while (T > 0) { T--; test_id += 1; std::cout << "Case #" << test_id << ": ";
        long long a; std::cin >> a; int cnt = 0;
        std::cout << getBest(a) << std::endl;                  
    }
}
