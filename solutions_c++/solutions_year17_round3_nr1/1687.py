#include <fstream>
#include <algorithm>
#include <iomanip>
#include <cmath>
#define NMAX 1001
using namespace std;

struct PANCAKE{long long r, h;};

PANCAKE pancakes[NMAX];

double PI = 3.14159265358979323846264338327950288419716939937510;
long double PIZ = 0.14159265358979323846264338327950288419716939937510;
long double PIL = 3.14159265358979323846264338327950288419716939937510;

double lateralSurface(PANCAKE p)
{
    return PI * 2 * p.r * p.h;
}

long long lateralSurfaceI(PANCAKE p)
{
    return p.r * p.h * 2;
}

bool compPan(PANCAKE a, PANCAKE b)
{
    return (lateralSurfaceI(a) > lateralSurfaceI(b));
}

int main()
{
    ifstream f("problema.in");
    ofstream g("problema.out");
    int t, ii;
    int n, k;
    int i;
    int maxRadPos;
    f >> t;
    for (ii = 0; ii < t; ii++)
    {
        f >> n >> k;
        maxRadPos = 0;
        for (i = 0; i < n; i++)
        {
            f >> pancakes[i].r >> pancakes[i].h;
//            if (pancakes[i].r > pancakes[maxRadPos].r)
//            {
//                maxRadPos = i;
//            }
        }
        sort(pancakes, pancakes + n, compPan);
//        double totalSurface = 0;
        long long totalSurface = 0;
//        double totalSurfZ = 0;
        for (i = 0; i < k - 1; i++)
        {
            if (pancakes[i].r > pancakes[maxRadPos].r)
            {
                maxRadPos = i;
            }
            totalSurface += lateralSurfaceI(pancakes[i]);
//            totalSurfZ += (totalSurface - floor(totalSurface));
//            totalSurface = floor(totalSurface);
        }
        int antMaxRadPos = maxRadPos;
        for (i = k - 1; i < n; i++)
        {
            if (pancakes[i].r > pancakes[maxRadPos].r)
            {
                maxRadPos = i;
            }
        }
        if (maxRadPos < k)
        {
            totalSurface += lateralSurfaceI(pancakes[k - 1]);
//            totalSurface *= PI;
//            totalSurface += PI * pancakes[maxRadPos].r * pancakes[maxRadPos].r;
            totalSurface += pancakes[maxRadPos].r * pancakes[maxRadPos].r;
        }
        else
        {
            if (pancakes[k - 1].r > pancakes[antMaxRadPos].r)
            {
                antMaxRadPos = k - 1;
            }
            long long v1 = lateralSurfaceI(pancakes[maxRadPos]) + pancakes[maxRadPos].r * pancakes[maxRadPos].r;
            long long v2 = lateralSurfaceI(pancakes[k - 1]) + pancakes[antMaxRadPos].r * pancakes[antMaxRadPos].r;
//            totalSurface += lateralSurfaceI(pancakes[maxRadPos]);
//            totalSurface *= PI;
            if (v1 > v2)
                totalSurface += v1;
            else
                totalSurface += v2;
        }
//        totalSurface *= PI;
//        totalSurface += PI * pancakes[maxRadPos].r * pancakes[maxRadPos].r;
//        totalSurfZ += (totalSurface - floor(totalSurface));
//        totalSurface = floor(totalSurface);
//        long long intTS = floor(totalSurface);
//        long long zecTS = totalSurfZ * 1000000000;
        long double result = totalSurface * PIL;
        long long intTS = floor(result);
        long long zecTS = (result - floor(result)) * 1000000000;
        g << "Case #" << ii + 1 << ": ";
        g << intTS << '.';
        g << setfill('0') << setw(9) << zecTS;
//        g << fixed << setprecision(10) << totalSurface;
        g << '\n';
    }
    f.close();
    g.close();
    return 0;
}