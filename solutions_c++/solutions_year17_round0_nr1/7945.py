#include <algorithm>
#include <iostream>
#include <string>

int Solve(std::string s, int k){
    
    //std::cout << std::endl << s << "," << k << std::endl;
    
    // create binary representation
    std::replace(s.begin(), s.end(), '-','1'); // blank
    std::replace(s.begin(), s.end(), '+','0'); // happy

    std::bitset<1000> pancakes (s); // all other bits will be 0 (happy)
    
    size_t n = s.length();
    int ans=0;
    
    for(size_t i=0;i<n;++i){
        //std::cout << i << "..." << pancakes[i] << std::endl;
        
        if(pancakes[i]){
            // this pancake is blank so it needs to be flipped
            
            if (i > (n-k) ){
                return -1;
            }
            
            // flip the batch
            for(size_t j=i; j<i+k; ++j){
                pancakes.flip(j);
            }
            ans++;
        }
        
        // stop iterating if no blank pancakes left
        if (pancakes.none()){
            break;
        }
    }
    return ans;
}

int main() {
    
    std::string basePath = "/Users/damienwintour/Documents/workspace/CodeJam2017/CodeJam2017/";
    std::string inFile = basePath + "A-large.in";
    std::string outFile = basePath + "outputA2.txt";
    
    freopen(inFile.c_str(),"r",stdin);
    freopen(outFile.c_str(),"w",stdout);
    
    int T;
    std::string S;
    int K;
    
    std::cin >> T;
    
    for (int caseNo = 1; caseNo <= T; caseNo++)
    {
        std::cin >> S;
        std::cin >> K;
        
        int ans = Solve(S,K);
        if (ans>=0){
            std::cout << "Case #" << caseNo << ": " << ans << std::endl;
        } else {
            std::cout << "Case #" << caseNo << ": IMPOSSIBLE" << std::endl;
        }
    }
    return 0;
}
