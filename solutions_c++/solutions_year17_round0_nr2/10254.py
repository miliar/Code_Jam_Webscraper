#include <iostream>
#include <string>

int main(){
    long T, temp, N, actual_value;

    std::cin >> T;

    for(int i = 0; i < T; ++i){
        std::cin >> N;
        temp = N;
        actual_value = 10;

        while(true){
            while(temp > 0){
                if(actual_value >= temp % 10){
                    actual_value = temp % 10;
                    temp /= 10;                    
                }

                else{
                    --N;
                    temp = N;
                    actual_value = 10;
                    break;
                }
            }

            if(actual_value != 10){
                break;
            }
        }

        std::cout << "Case #" << i + 1 << ": " << N << "\n";
    }

    return 0;
}
