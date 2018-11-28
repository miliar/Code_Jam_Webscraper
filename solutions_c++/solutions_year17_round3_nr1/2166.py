#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>

const float PI = 3.1415927;

int main(int argc, char *argv[])
{
    int test_case_number;
    freopen("input.txt", "r", stdin);
    freopen("A-small-attempt3.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &test_case_number);

    for (int test_case = 1; test_case <= test_case_number; test_case++) {
        double answer = 0;
        int n, k;
        scanf("%d %d", &n, &k);
        std::vector<long> radius(n);
        std::vector<long> heights(n);
        for (size_t i = 0; i < n; i++) {
            int  h, r;
            scanf("%d %d", &r, &h);
            radius[i] = r;
            heights[i] = h;
        }

        for (int mask = 0; mask < (1<<n);mask++)
        {
//            std::cout << mask << " "<< test_case<<" "<< n<< std::endl;
            int n_bits = 0;
            for (int cnt = 0; cnt < n; cnt++) {
                if (((1 <<cnt)&mask)) {
                    n_bits++;
                }
            }
            if (n_bits==k) {
                std::priority_queue<std::pair<long, long>, std::vector<std::pair<long, long>>, std::greater<std::pair<long, long>>> pq;
                for (int i = 0; i < n; i++) {
                    if (mask & (1 << i)) {
                        pq.push(std::pair<long, long>(radius[i], heights[i]));
                    }
                }
                double current_answer = 0;
                long last_radius = 0;
                while (!pq.empty()) {
                    current_answer +=  2.0 * M_PI * (double)(pq.top().first) * (double)(pq.top().second);
                    last_radius = pq.top().first;
                    pq.pop();
                }
                current_answer +=  M_PI * (double)last_radius * (double)last_radius;
//                std::cout << current_answer <<  " "<<mask<< " " << test_case<<" " << std::endl;
                if (current_answer > answer) {
                    answer = current_answer;
                }

            } else {
                continue;
            }
        }

//        std::priority_queue<std::pair<long,std::pair<long, long>> , std::vector<std::pair<long, std::pair<long, long>>>, std::greater<std::pair<long,std::pair<long, long>>>> pq;
//        for (size_t i = 0; i < n; i++) {
//            if (pq.size() < k) {
//                pq.push(std::pair<long, std::pair<long, long>>((2*radius[i] * heights[i])
//                                                               +(radius[i]*radius[i])
//                                                               , std::pair<long, long>(radius[i], heights[i])));
//            } else {
//                if (pq.top().first  < (
//                            (2*radius[i] * heights[i])
//                            +
//                            (radius[i]*radius[i])
//                            )
//                        ) {
//                     pq.pop();
//                     pq.push(std::pair<long, std::pair<long, long>>((2*radius[i] * heights[i]), std::pair<long, long>(radius[i], heights[i])));
//                    pq.push(std::pair<long, std::pair<long, long>>((2*radius[i] * heights[i])+(radius[i]*radius[i]), std::pair<long, long>(radius[i], heights[i])));
//                }
//            }
//        }

//        long last_radius = 0;
//        while (!pq.empty()) {
//            answer +=  2.0 * M_PI * (double)(pq.top().second.first) * (double)(pq.top().second.second);
//            last_radius = pq.top().second.first;
//            pq.pop();
//        }
//        answer +=  M_PI * (double)last_radius * (double)last_radius;
        printf("Case #%d: %.9f\n",test_case, answer);
    }
    return 0;
}
