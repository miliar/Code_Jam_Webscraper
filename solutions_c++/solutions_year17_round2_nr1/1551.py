#include<iostream>
#include<cstdio>
#include<algorithm>


using namespace std;

const int MAX_N = 1000;

double arr[MAX_N];

int main(void)
{
    int T;  cin >> T;
    double D; int N;
    double K, V;

    for (int t = 1; t <= T; t ++)
    {
        scanf("%lf %d", &D, &N);
        
        for (int i = 0; i < N; i ++)
        {
            scanf("%lf %lf", &K, &V);
            arr[i] = (D-K)/V;
        }
    
        sort(arr, arr + N);

        double res = D / arr[N-1];

        printf("Case #%d: %lf\n",t, res);
    }
}
