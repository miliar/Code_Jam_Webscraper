#include <bits/stdc++.h>
using namespace std;

//#define PI 3.1415926535897
typedef std::vector<double> my_vec;

int R[1000], H[1000];
double area[1000];
double surr_area[1000];

int main(int argc, char *argv[])
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    //FILE *f = fopen("/home/quanganh/projects/TestQt/build-TestQt-Desktop-Debug/input.txt", "r");

    int num_test;
    //fscanf(f, "%d", &num_test);
    scanf("%d", &num_test);

    for (int test = 0; test < num_test; test++)
    {
        int N, K;
        scanf("%d %d", &N, &K);
        for (int i = 0; i < N; i++)
        {
            scanf("%d %d", &R[i], &H[i]);
        }

        for (int i = 0; i < N; i++)
        {
            area[i] = M_PI * (double)R[i] * (double)R[i];
            surr_area[i] = 2 * M_PI * (double)R[i] * (double)H[i];
        }

        double max_res = 0.0f;

        for (int i = 0; i < N; i++)
        {
            int max_r = R[i];
            double tmp_max = area[i] + surr_area[i];
            my_vec sorted_r;
            for (int j = 0; j < N; j++)
            {
                if (j == i) continue;
                if (R[j] <= R[i])
                    sorted_r.push_back(surr_area[j]);
            }
            int s = sorted_r.size();
            if (s < K - 1)
                continue;
            sort(sorted_r.begin(), sorted_r.end());
            reverse(sorted_r.begin(), sorted_r.end());
            
            for (int j = 0; j < K - 1; j++)
            	tmp_max += sorted_r[j];

            max_res = max_res > tmp_max ? max_res : tmp_max;

        }

        printf("Case #%d: %0.7f\n", test + 1, max_res);
    }

    return 0;
}

