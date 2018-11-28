#include <cstdio>

int main(int argc, char **argv) {
    int num_cases;
    scanf("%d", &num_cases);

    for (int c = 1; c <= num_cases; c++) {
        printf("Case #%d: ", c);

        double dest;
        int num_horses;
        scanf("%lf %d", &dest, &num_horses);

        double max_time = -1;

        for (int i = 0; i < num_horses; i++) {
            double pos;
            int speed;
            scanf("%lf %d", &pos, &speed);

            double time = (dest - pos) / double(speed);
            if (time > max_time) {
                max_time = time;
            }
        }

        printf("%.6f\n", dest / max_time);
    }

    return 0;
}
