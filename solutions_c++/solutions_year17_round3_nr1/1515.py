#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;

//#define M_PI 3.14159265358979323846f
//#define M_PI 3.141592653589793f

int R[1000];
int H[1000];
double chuvi[1000];
double dientich[1000];

int main(int argc, char **argv)
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int ntest;
    scanf("%d", &ntest);

    for (int test = 1; test <= ntest; test++) {
        printf("Case #%d: ", test);

        int N,K;
        scanf("%d %d", &N, &K);

        for (int i = 0; i != N; i++) {
            scanf("%d %d", &R[i], &H[i]);

            chuvi[i] = 2*M_PI*(double)R[i]*(double)H[i];
            dientich[i] = M_PI*(double)R[i]*(double)R[i];
        }

        double ans = 0.0;

        for (int i = 0; i != N; i++) {
            vector<pair<double,int> > V;
            for (int j = 0; j != N; j++) {
                if (i==j) continue;
                if (R[j] > R[i]) continue;
                V.push_back(make_pair(chuvi[j],j));
            }

            if (V.size() < K-1)
                continue;

            sort(V.begin(),V.end());
            reverse(V.begin(),V.end());

            double tmp = dientich[i] + chuvi[i];
            for (int k = 0; k != K-1; k++)
                tmp += chuvi[V[k].second];

            ans = max(ans,tmp);
        }

        printf("%0.7f\n", ans);

    }

	return 0;
}

