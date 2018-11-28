#include <iostream>

int T;
std::string tidy;

int main(){
    std::cin >> T;
    for (int t = 1; t <= T; t++){
        std::cin >> tidy;
        for (unsigned int i = tidy.size() - 1; i > 0; i--){
            if (tidy[i] < tidy[i-1]){
                tidy[i] = '9';
                tidy[i-1]--;
                for (unsigned int j = i; j < tidy.size(); j++){
                    if (tidy[j] > tidy[j+1]){
                        tidy[j+1] = '9';
                    }
                }
            }
        }
        if (tidy[0] <= '0'){
            tidy.erase(tidy.begin());
        }
        std::cout << "Case #" << t << ": " << tidy << std::endl;
    }
    return 0;
}
