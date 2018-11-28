#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>

int main(){
    long long unsigned int t, n, flag, x, temp;
    std::string s;
    scanf("%llu", &t);
    for(int i = 1; i <= t; i++){
        flag = x = 0;
        scanf("%llu", &n);
        for(long long unsigned int j = n; j >= 1; j--){
            s.clear();
            temp = j;
            if(j <= 9){
                s = j + '0';
                break;
            }
            while(true){
                x = temp % 10;
                s += x + '0';
                if(temp / 10 == 0)
                    break;
                temp = temp / 10;
            }
            std::reverse(s.begin(), s.end());
            for(int k = 0; k < s.size(); k++){
                if(k + 1 < s.size() && s[k] <= s[k + 1])
                    flag = 1;
                else if(k + 1 < s.size()){
                    flag = 0;
                    break;
                }
            }
            if(flag == 1)
                break;
        }
        std::cout << "Case #" << i << ": " << s << std::endl;
    }
    return 0;
}
