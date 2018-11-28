#include <iostream>
#include <algorithm>
#include <iomanip>
#include <cmath>

const int MAX = 1005;

int N,K;
long R[MAX];
long H[MAX];
int RH[MAX];
int Hi[MAX];
int HRi[MAX];

bool cmpH(int l, int r)
{
    return R[l] < R[r];
}
bool cmpHR(int l, int r)
{
    return H[l]*R[l] > H[r]*R[r];
}

typedef long double LD;

void Solve(int T)
{
    std::cin >> N >> K;
    for (int i=0;i<N;++i)
    {
        std::cin >> R[i] >> H[i];
        Hi[i] = i;
    }
    std::sort(Hi, Hi+N, cmpH);

    LD result = 0;
    for (int i=K-1;i<N;++i)
    {
        for (int j=0;j<i;++j)
            HRi[j] = Hi[j];
        std::sort(HRi, HRi+i, cmpHR);

        int Bi = Hi[i];
        LD P = LD(R[Bi]) * R[Bi] + 2.0L*H[Bi]*R[Bi];
        for (int j=0;j<K-1;++j)
        {
            int Pi = HRi[j];
            P += 2.0L*H[Pi]*R[Pi];
        }
        result = std::max(result, P);
    }
    result *= 3.14159265358979323846264338327950288419716939937510L;

    std::cout.precision(9);

    std::cout << "Case #" << T << ": " << std::fixed << result << "\n";
}

int main()
{
    int T;
    std::cin >> T;
    for (int i=1;i<=T;++i)
        Solve(i);
    return 0;
}