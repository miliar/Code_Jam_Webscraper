#include <cstdio>
#include <map>
#include <queue>
#include <vector>
#include <limits>
using namespace std;

#define LL int64_t

int test_case = 0;

#define IN(...) fscanf(stdin, ##__VA_ARGS__)
#define OUT(...) fprintf(stdout, ##__VA_ARGS__)

#

int main(int argc, const char * argv[]) {

#if DEBUG
    freopen("/Users/kzaher/Projects/codejam/CodeJam1/horse/input.txt", "rb", stdin);
    freopen("/Users/kzaher/Projects/codejam/CodeJam1/horse/output.txt", "wb", stdout);
#endif

    int count;
    IN("%d\n", &count);

    for (test_case = 0; test_case < count; ++test_case) {
        double distance = 0;
        double max_time = 0;

        int number_of_horses;
        IN("%lf %d", &distance, &number_of_horses);
        for (int i = 0; i < number_of_horses; ++i) {
            double position, max_speed;
            IN("%lf %lf", &position, &max_speed);
            double time = (distance - position) / max_speed;
            if (time > max_time) {
                max_time = time;
            }
        }

        OUT("Case #%d: %lf\n", test_case + 1, distance / max_time);
    }

    return 0;
}
