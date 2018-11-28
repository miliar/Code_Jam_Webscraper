#include <iostream>
#include <string>
#include <vector>

int main(void){

    int test_case = 0;

    int tmp_k = 0;
    std::string tmp_s;

    int toggle_cnt = 0;

    size_t start_offset= 0;

    std::cin >> test_case;

    std::vector<std::string> s;
    std::vector<int> k;

    s.reserve(test_case);
    k.reserve(test_case);

    for(int i = 0; i < test_case; ++i){
        std::cin >> tmp_s >> tmp_k;
        s.push_back(tmp_s);
        k.push_back(tmp_k);
    }

    for(int idx = 0; idx < test_case; ++idx){
        toggle_cnt = 0;

        start_offset = s[idx].find('-');
        if(start_offset != std::string::npos){

            for(int offset = start_offset; offset < s[idx].length() - (k[idx]-1); ++offset){
                if(s[idx].at(offset) == '-'){
                    for(int range = offset; range < offset + k[idx]; range++)
                        s[idx][range] = s[idx][range] == '-' ? '+' : '-';
                    toggle_cnt++;
                }
            }

            if(s[idx].find('-') == std::string::npos)
                std::cout << "Case #" << idx + 1 << ": " << toggle_cnt << std::endl;
            else
                std::cout << "Case #" << idx + 1 << ": IMPOSSIBLE" << std::endl;

        }else{
            std::cout << "Case #" << idx + 1 << ": 0" << std::endl;
        }
    }

    return 0;
}
