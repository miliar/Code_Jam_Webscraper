#include <fstream>
#include <cstdio>

using namespace std;

ifstream cin("data.in");

int main()
{
    double D, k, s;
    int t, T, N, i;
    double temp_d, temp_t, max_t = -1, temp_s;

    FILE *fout = fopen("data.out","w");

    cin >> T;
    for(t = 1; t <= T; t++){
        max_t = 0;
        cin >> D >> N;
        for(i = 1; i <= N; i++){
            cin >> k >> s;
            temp_d = D - k;
            temp_t = temp_d / s;
            if(temp_t > max_t)
                max_t = temp_t;
        }
        temp_s = D/max_t;
        fprintf(fout, "Case #%d: %.6f\n", t, temp_s);
        //cout << "Case #" << i << ": " << temp_s << '\n';
    }
    return 0;
}
