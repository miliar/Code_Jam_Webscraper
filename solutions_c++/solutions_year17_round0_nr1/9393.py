#include <iostream>
#include <string>

int main() {
    int i;
    std::cin >> i;
    for(int x = 1; x <= i; x++){
        int verdict = 0;
        std::string s_raw;
        std::cin >> s_raw;
        //put characters in array
        int s [1001];
        for(int j = 0; j < s_raw.length(); j++){
            s[j] = s_raw.at(j);
        }
        int k;
        std::cin >> k;
        if(k <= s_raw.length()){
            for(int m = 0; m <= s_raw.length() - k; m++){
                if(s[m] == '-'){
                    //flip k
                    for(int y = 0; y < k; y++){
                        if(s[m+y] == '+'){
                            s[m+y] = '-';
                        }else
                            s[m+y] = '+';
                    }
                    verdict++;
                }
            }
            //check last k-1 places to see if they are all +
            for(int a = s_raw.length() - k; a < s_raw.length(); a++){
                if(s[a] == '-'){
                    verdict = -1;
                    break;
                }
            }
        }else {
            for(int i = 0; i < s_raw.length(); i++){
                if(s[i] == '-'){
                    verdict = -1;
                    break;
                }
            }
        }
        std::cout << "Case #" << x << ": ";
        if(verdict == -1){
            std::cout << "IMPOSSIBLE" << std::endl;
        }else{
            std::cout << verdict << std::endl;
        }
    }
    return 0;
}