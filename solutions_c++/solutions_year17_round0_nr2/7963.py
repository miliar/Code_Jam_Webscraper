

#include <iostream>
#include <string>
#include <cstdint>
#include <cmath>

uint64_t int_pow(int b, uint16_t e){
    uint64_t ans=1;
    for(uint16_t i=1; i<=e; ++i){
        ans = ans * b;
    }
    return ans;
}

uint64_t Solve(uint64_t n){
    
    uint64_t ans = 0;
    uint64_t lastDigit = 9;
    int digitCount = 0;
    
    // iterate through each digit
    while(n > 0){
        
        uint64_t digit = n % 10;
        
        if (digit <= lastDigit){    // still tidy
            ans = ans + (digit* int_pow(10,digitCount));
            lastDigit=digit;
        } else {                    // not tidy anymore
            ans = (digit* int_pow(10,digitCount))-1;
            lastDigit=digit-1;
        }
        //std::cout << digitCount << ":" << digit << ", " << ans << std::endl;
        n = n / 10;
        digitCount++;
    }
    return ans;
}

int main() {

    std::string basePath = "/Users/damienwintour/Documents/workspace/CodeJam2017/CodeJam2017/";
    std::string inFile = basePath + "B-large.in";
    std::string outFile = basePath + "output2.txt";
    
    freopen(inFile.c_str(),"r",stdin);
    freopen(outFile.c_str(),"w",stdout);
    
    int T;
    uint64_t N;
    
    std::cin >> T;
    
    for (int caseNo = 1; caseNo <= T; caseNo++)
    {
        std::cin >> N;
        
        std::cout << "Case #" << caseNo << ": " << Solve(N) << std::endl;
    }
    return 0;
}
