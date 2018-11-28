//
//  main.cpp
//  test
//
//  Created by kevin on 2017/4/9.
//  Copyright © 2017年 kaiwen. All rights reserved.
//

#include <iostream>
int main(int argc, const char * argv[]) {
    int t;
    std::cin >> t;
    std::string s1;
    for(int i = 1;i <= t;i++){
        std::cin >> s1;
        int re = 0;
        int size = (int)s1.length();
        bool tf = 1;
        while(1){
            tf = 1;
            for(re = 0;re < size - 1;re++){
                if(s1[re] - '0' > s1[re + 1] - '0'){
                    s1[re] = (s1[re] - '0' - 1) + '0';
                    tf = 0;
                    break;
                }
            }
            if(tf){
                break;
            }
            size = re + 1;
        }
        std::cout << "Case #" << i << ": ";
        for(int j = 0;j < size;j++){
            if(j == 0 && s1[j] == '0'){
                continue;
            }
            std::cout << s1[j];
        }
        int count = (int)s1.length() - size;
        for(int j = 0;j < count;j++){
            std::cout << "9";
        }
        std::cout << "\n";
    }
    return 0;
}
