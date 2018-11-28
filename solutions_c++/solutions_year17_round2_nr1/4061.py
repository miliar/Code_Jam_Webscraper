#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char *argv[])
{
    int test_case_number;
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &test_case_number);

//    std::cout << test_case_number << std::endl;
    for (int test_case = 1; test_case <= test_case_number; test_case++) {
        int D, N;
        scanf("%d %d", &D, &N);
        std::vector<std::pair<double, double>> speed(N+1, std::pair<double, double>(0, 0));


        for (int i = 1; i <= N; i++) {
            int p, v;
            scanf("%d %d", &p, &v);
            speed[i].first = p;
            speed[i].second = v;
        }
        std::sort(speed.begin(), speed.end());
        double time = 0;

        for (int i = N; 0< i; i--) {
            if (i==N) {
                time += ((double)D - speed[i].first) / (speed[i].second);
            } else {
                if (speed[i].second > speed[i+1].second) {
                    float t1 = (speed[i+1].first - speed[i].first)/ (speed[i].second - speed[i+1].second);
                    if (t1 < time) {
//                        time += ((float)D - (float)speed[i].first - time * speed[i].second) / (speed[i].second);
                    } else {
                        time += ((double)D - speed[i].first - time * speed[i].second) / (speed[i].second);
                    }
                } else  {
                    time += ((double)D - speed[i].first - time * speed[i].second) / (speed[i].second);
                }
            }
        }

        printf("Case #%d: %.6f\n",test_case, (double)D / time);
    }
    return 0;
}
