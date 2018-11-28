#include <iostream>
using namespace std;
struct act
{
    int s, e;
    bool belongToC;
};
act a[205];
bool cmp(act a, act b)
{
    return a.s < b.s;
}
int AAspace[205];
int ABspace[205];
int BBspace[205];
int main()
{
    int T;
    cin >> T;
    for (int ca = 1; ca <= T; ++ca)
    {
        int ac, aj;
        cin >> ac >> aj;
        int total = 0;
        int totalC = 0, totalJ = 0;
        for (int i = 0; i < ac; ++i)
        {
            cin >> a[total].s >> a[total].e;
            a[total].belongToC = false;
            totalJ += (a[total].e - a[total].s);
            total++;
        }
        for (int i = 0; i < aj; ++i)
        {
            cin >> a[total].s >> a[total].e;
            a[total].belongToC = true;
            totalC += (a[total].e - a[total].s);
            total++;
        }
        totalC = 24 * 60 / 2 - totalC;
        totalJ = 24 * 60 / 2 - totalJ;
        sort(a, a + total, cmp);
        int noOfAA = 0;
        int noOfAB = 0;
        int noOfBB = 0;
        int result;
        if (totalJ <= totalC)
        {
            result = ac * 2;
            for (int i = 0; i < total; ++i)
            {
                int j = i + 1;
                if (j == total)
                    j = 0;
                int e = a[i].e;
                int s = a[j].s;
                if (s < e)
                    s += 24 * 60;
                if (a[i].belongToC && a[j].belongToC)
                {
                    if (s == e)
                        continue;
                    BBspace[noOfBB++] = s - e;
                    continue;
                }
                if (a[i].belongToC || a[j].belongToC)
                {
                    if (s == e)
                        continue;
                    ABspace[noOfAB++] = s - e;
                    continue;
                }
                //AA
                if (s == e)
                    result -= 2;
                else
                    AAspace[noOfAA++] = s - e;
            }
            sort(AAspace, AAspace + noOfAA);
            sort(ABspace, ABspace + noOfAB);
            sort(BBspace, BBspace + noOfBB);
            for (int i = 0; i < noOfAA; ++i)
            {
                if (totalJ >= AAspace[i])
                {
                    result -= 2;
                    totalJ -= AAspace[i];
                }
                else
                {
                    totalJ = 0;
                    break;
                }
            }
            if (totalJ > 0)
            {
                for (int i = noOfAB - 1; i >= 0; --i)
                {
                    totalJ -= ABspace[i];
                }
            }
            if (totalJ > 0)
            {
                for (int i = noOfBB - 1; i >= 0; --i)
                {
                    totalJ -= BBspace[i];
                    result += 2;
                    if (totalJ <= 0)
                        break;
                }
            }
            cout << "Case #" << ca << ": " << result << endl;
            ;
        }
        else
        {
            result = aj * 2;
            for (int i = 0; i < total; ++i)
            {
                int j = i + 1;
                if (j == total)
                    j = 0;
                int e = a[i].e;
                int s = a[j].s;
                if (s < e)
                    s += 24 * 60;
                if ((!a[i].belongToC) && (!a[j].belongToC))
                {
                    if (s == e)
                        continue;
                    BBspace[noOfBB++] = s - e;
                    continue;
                }
                if ((!a[i].belongToC) || (!a[j].belongToC))
                {
                    if (s == e)
                        continue;
                    ABspace[noOfAB++] = s - e;
                    continue;
                }
                //AA
                if (s == e)
                    result -= 2;
                else
                    AAspace[noOfAA++] = s - e;
            }
            sort(AAspace, AAspace + noOfAA);
            sort(ABspace, ABspace + noOfAB);
            sort(BBspace, BBspace + noOfBB);
            for (int i = 0; i < noOfAA; ++i)
            {
                if (totalC >= AAspace[i])
                {
                    result -= 2;
                    totalC -= AAspace[i];
                }
                else
                {
                    totalC = 0;
                    break;
                }
            }
            if (totalC > 0)
            {
                for (int i = noOfAB - 1; i >= 0; --i)
                {
                    totalC -= ABspace[i];
                }
            }
            if (totalC > 0)
            {
                for (int i = noOfBB - 1; i >= 0; --i)
                {
                    totalC -= BBspace[i];
                    result += 2;
                    if (totalC <= 0)
                        break;
                }
            }
            cout << "Case #" << ca << ": " << result << endl;
            ;
        }
    }
}