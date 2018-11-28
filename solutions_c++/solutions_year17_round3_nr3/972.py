// CodeJam
// Author:  Yotam Medini  yotam.medini@gmail.com -- Created: 2013/April/20

#include <iostream>
#include <fstream>
#include <string>
// #include <set>
// #include <map>
#include <vector>
#include <utility>
#include <algorithm>

#include <cstdlib>
// #include <gmpxx.h>

using namespace std;

// typedef mpz_class mpzc_t;
typedef unsigned long ul_t;
typedef unsigned long long ull_t;
typedef vector<double> vd_t;

static unsigned dbg_flags;

class CoreTrain
{
 public:
    CoreTrain(istream& fi);
    void solve_naive();
    void solve();
    void print_solution(ostream&) const;
 private:
    unsigned n, k;
    double u;
    vd_t cores;
    double solution;
};

CoreTrain::CoreTrain(istream& fi) : solution(0)
{
    fi >> n >> k;
    fi >> u;
    cores.reserve(n);
    for (unsigned i = 0; i < n; ++i)
    {
        double p;
        fi >> p;
        cores.push_back(p);
    }
}

void CoreTrain::solve_naive() // k == n
{
    sort(cores.begin(), cores.end());
    while (u > 0)
    {
        unsigned i;
        for (i = 0; (i + 1 < n) && (cores[i] == cores[i + 1]); ++i) {}
        if ((i + 1) == n)
        {
            double a = u/n;
            u = 0;
            double newp = cores[0] + a;
            if (newp > 1) { newp = 1.; }
            fill(cores.begin(), cores.end(), newp);
        }
        else
        {
            double delta = cores[i + 1] - cores[i];
            double desire = (i + 1) * delta;
            double give = desire;
            if (give >= u)
            {
                give = u;
                u = 0;
            }
            else
            {
                u -= give;
            }
            double newp = cores[0] + give/(i + 1);
            fill(cores.begin(), cores.begin() + (i + 1), newp);
        }
    }
    solution = 1.;
    for (unsigned i = 0; i < n; ++i)
    {
        solution *= cores[i];
    }
}

void CoreTrain::solve()
{
    solve_naive();
}

void CoreTrain::print_solution(ostream &fo) const
{
    char buf[0x40];
    sprintf(buf, "%.9f", solution);
    fo << " " << buf;
}

int main(int argc, char ** argv)
{
    const string dash("-");

    unsigned n_opts = 0;
    bool naive = false;

    if ((argc > 1) && (string(argv[1]) == "-naive"))
    {
        naive = true;
        n_opts = 1;
    }
    int ai_in = n_opts + 1;
    int ai_out = ai_in + 1;
    int ai_dbg = ai_out + 1;
    istream *pfi = (argc <= ai_in || (string(argv[ai_in]) == dash))
         ? &cin
         : new ifstream(argv[ai_in]);
    ostream *pfo = (argc <= ai_out || (string(argv[ai_out]) == dash))
         ? &cout
         : new ofstream(argv[ai_out]);

    if ((!pfi) || (!pfo) || pfi->fail() || pfo->fail())
    {
        cerr << "Open file error\n";
        exit(1);
    }

    if (ai_dbg < argc) { dbg_flags = strtoul(argv[ai_dbg], 0, 0); }

    unsigned n_cases;
    *pfi >> n_cases;

    void (CoreTrain::*psolve)() =
        (naive ? &CoreTrain::solve_naive : &CoreTrain::solve);

    ostream &fout = *pfo;
    bool tellg = getenv("TELLG");
    ul_t fpos_last = pfi->tellg();
    for (unsigned ci = 0; ci < n_cases; ci++)
    {
        CoreTrain problem(*pfi);
        if (tellg)
        {
            ul_t fpos = pfi->tellg();
            cerr << "Case (ci+1)="<<(ci+1) << ", tellg=[" <<
                fpos_last << ", " << fpos << ")\n";
            fpos_last = fpos;
        }

        (problem.*psolve)();
        fout << "Case #"<< ci+1 << ":";
        problem.print_solution(fout);
        fout << "\n";
        fout.flush();

    }

    if (pfi != &cin) { delete pfi; }
    if (pfo != &cout) { delete pfo; }
    return 0;
}
