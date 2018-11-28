#include <algorithm>
#include <cassert>
#include <cstdio>
#include <iostream>
#include <vector>

#define RI 0
#define OI 1
#define YI 2
#define GI 3
#define BI 4
#define VI 5

std::vector<char> colors = {'R', 'Y', 'B'};

int main(int argc, char **argv) {
    int num_cases;
    scanf("%d", &num_cases);

    for (int c = 1; c <= num_cases; c++) {
        printf("Case #%d: ", c);

        unsigned int N, R, O, Y, G, B, V;
        scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);

        std::vector<unsigned int> horses = {R, O, Y, G, B, V};
        std::vector<unsigned int> single_colored_horses = {R, Y, B};
        std::vector<unsigned int> &sc = single_colored_horses;
        std::vector<char> output;

        auto min_elt = std::min_element(single_colored_horses.begin(), single_colored_horses.end());
        unsigned int min = *min_elt;

        if (min > 0) {
            for (unsigned int i = 0; i < min; i++) {
                output.push_back('R');
                output.push_back('Y');
                output.push_back('B');
            }

            auto add = [&min](int a) -> int {
                return a - min;
            };
            std::transform(single_colored_horses.begin(), single_colored_horses.end(), single_colored_horses.begin(), add);
        }

        if (sc[0] == 0 && sc[1] == 0 && sc[2] == 0) {
            //printf("N %d, output %d\n", N, output.size());
            assert(output.size() == N);
            assert(*output.begin() != (*(--output.end())));
            std::string output_str(output.begin(), output.end());
            std::cout << output_str << std::endl;
            continue;
        }

        if (min == 0) {
            if (!(sc[0] == sc[1] || sc[1] == sc[2] || sc[2] == sc[0])) {
                printf("IMPOSSIBLE\n");
                continue;
            }
        }

        if ((sc[0] == sc[1] && sc[0] != 0) || (sc[1] == sc[2] && sc[1] != 0) || (sc[2] == sc[0] && sc[2] != 0)) {
            if (sc[0] == sc[1]) {
                for (unsigned int i = 0; i < sc[0]; i++) {
                    output.push_back('R');
                    output.push_back('Y');
                }
            } else if (sc[1] == sc[2]) {
                for (unsigned int i = 0; i < sc[1]; i++) {
                    output.push_back('Y');
                    output.push_back('B');
                }
            } else if (sc[2] == sc[0]){
                for (unsigned int i = 0; i < sc[2]; i++) {
                    output.push_back('R');
                    output.push_back('B');
                }
            }
            //printf("N %d, output %d\n", N, output.size());
            assert(output.size() == N);
            assert(*output.begin() != (*(--output.end())));
            std::string output_str(output.begin(), output.end());
            std::cout << output_str << std::endl;
            continue;
        }

        unsigned int max_idx, min_idx;

        if (min_elt - sc.begin() == 0) {
            if (sc[1] > sc[2]) {
                max_idx = 1;
                min_idx = 2;
            } else {
                max_idx = 2;
                min_idx = 1;
            }
        } else if (min_elt - sc.begin() == 1) {
            if (sc[0] > sc[2]) {
                max_idx = 0;
                min_idx = 2;
            } else {
                max_idx = 2;
                min_idx = 0;
            }
        } else {
            if (sc[0] > sc[1]) {
                max_idx = 0;
                min_idx = 1;
            } else {
                max_idx = 1;
                min_idx = 0;
            }
        }

        unsigned int rem_max, rem_min;
        char col_max, col_min;

        rem_max = sc[max_idx];
        rem_min = sc[min_idx];
        col_max = colors[max_idx];
        col_min = colors[min_idx];

        if (rem_min > 0) {
            if (col_min == 'B' || col_max == 'B') {
                for (unsigned int i = 0; i < rem_min; i++) {
                    output.push_back(col_min == 'B' ? col_max : col_min);
                    output.push_back('B');
                }
            } else {
                output.pop_back();
                for (unsigned int i = 0; i < rem_min; i++) {
                    output.push_back('R');
                    output.push_back('Y');
                }
                output.push_back('B');
            }

            rem_max -= rem_min;
        }

        if (rem_max > min) {
            printf("IMPOSSIBLE\n");
            continue;
        }

        auto it = output.begin();
        std::vector<char> output2;

        if (col_max == 'Y') {
            output2.push_back('Y');
            //putchar('Y');
        } else if (col_max == 'B') {
            //putchar(*it);
            output2.push_back(*(it++));
            output2.push_back('B');
            //putchar('B');
        } else {
            //putchar(*it);
            output2.push_back(*(it++));
            //putchar(*it);
            output2.push_back(*(it++));
            output2.push_back('R');
            //putchar('R');
        }

        for (unsigned int i = 1; i < rem_max; i++) {
            //putchar(*it);
            output2.push_back(*(it++));
            //putchar(*it);
            output2.push_back(*(it++));
            //putchar(*it);
            output2.push_back(*(it++));
            //putchar(col_max);
            output2.push_back(col_max);
        }

        while (it != output.end()) {
            //putchar(*it);
            output2.push_back(*(it++));
        }

        //printf("N %d, output2 %d\n", N, output2.size());
        assert(output2.size() == N);
        assert(*output2.begin() != (*(--output2.end())));
        std::string output_str(output2.begin(), output2.end());
        std::cout << output_str << std::endl;
    }

    return 0;
}
