#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef unsigned long long ull;

ifstream fin("date.in");
ofstream fout("date.out");

/**

    Ls, Rs
    each of which is the number of empty stalls between S and
    the closest occupied stall to the left or right, respectively

**/

struct stall
{
    int Ls, Rs;
    int minlr, maxlr;
    bool occ = false;
};

int cas;

int Ls, Rs;
int n, k;
stall v[1000];
int lastmaxlr, lastminlr;

void write()
{
    fout << "Case #" << cas << ": ";
    fout << lastmaxlr << " " << lastminlr << "\n";
}

void clean()
{
    for (int i = 0; i < n; i ++)
    {
        v[i].occ = false;
    }
}

void calc(stall &a, int pos)
{
    int li = pos, ri = pos;
    int nrl = 0, nrr = 0;

    while (!v[li - 1].occ)
    {
        li --;
        nrl ++;
    }

    while (!v[ri + 1].occ)
    {
        ri ++;
        nrr ++;
    }

    a.Ls = nrl;
    a.Rs = nrr;
    a.minlr = min(nrl, nrr);
    a.maxlr = max(nrl, nrr);
}

void rez()
{
    fin >> n >> k;
    n = n + 2;
    v[0].occ = true;
    v[n - 1].occ = true;

    for (int i = 0; i < k; i ++)
    {

        for (int i = 1; i < n - 1; i ++)
            if (!v[i].occ)
                calc(v[i], i);

        int chosepos, maxmin = -1;
        for (int i = 1; i < n - 1; i ++)
            if (!v[i].occ)
            {
                if (v[i].minlr > maxmin)
                {
                    chosepos = i;
                    maxmin = v[i].minlr;
                }
                else if (v[i].minlr == maxmin)
                {
                    if (v[i].maxlr > v[chosepos].maxlr)
                    {
                        chosepos = i;
                    }
                }
            }
        v[chosepos].occ = true;
        lastmaxlr = v[chosepos].maxlr;
        lastminlr = v[chosepos].minlr;
    }
    write();
}

int main()
{
    int t;
    fin >> t;
    for (int i = 0; i < t; i ++)
    {
        cas ++;
        rez();
        clean();
    }
}
