#include <iostream>
#include <string>

bool tidy(int input){
    bool cont = true;
    int digits = 0;
    int temp = input;
    while(cont){
        if(temp != 0){
            temp = temp/10;
            digits++;
        }
        else{
            cont = false;
        }
    }
    for(int z = digits; z > 0; z--){
        int last = input%10;
        int secondtolast = (input/10)%10;
        if(last < secondtolast){
            return false;
        }
        input = input / 10;
    }
    return true;
}

int main() {
    int i;
    std::cin >> i;
    for(int j = 1; j <= i ; j++){
        int input;
        std::cin >> input;
        int final;
        for(int x = input; x > 0; x--){
            if(tidy(x)){
                final = x;
                break;
            }
        }
        std::cout << "Case #" << j << ": " << final << std::endl;
    }
    return 0;
}