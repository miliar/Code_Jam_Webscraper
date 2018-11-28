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
#include <cmath>
// #include <gmpxx.h>

using namespace std;

// typedef mpz_class mpzc_t;
typedef unsigned long ul_t;
typedef unsigned long long ull_t;
// typedef vector<ul_t> vul_t;

static unsigned dbg_flags;

typedef std::vector<unsigned> vuints_t;

static void iota(vuints_t& v, unsigned n, unsigned val=0)
{
    v.clear();
    v.reserve(n);
    for (unsigned k = 0; k < n; ++k, val++)
    {
        v.push_back(val);
    }
}

void combination_first(vuints_t &c, unsigned n, unsigned k)
{
    iota(c, k, 0);
}

bool combination_next(vuints_t &c, unsigned n)
{
    unsigned j = 0, k = c.size();

    // sentinels (Knuth) (Why the second (0) ??!)
    c.push_back(n);  c.push_back(0);

    while ((j < k) && (c[j] + 1 == c[j + 1]))
    {
        c[j] = j;
        ++j;
    }
    bool ret = j < k;
    if (ret)
    {
        ++(c[j]);
    }

    c.pop_back(); c.pop_back(); // the sentinels

    return ret;
}


class Pancake
{
 public:
    Pancake(double vr=0, double vh=0) : r(vr), h(vh)
    {
        compute();
    }
    void compute()
    {
        fa = face_area();
        sa = side_area();
    }
    double face_area() const
    {
        double ret = M_PI*r*r;
        return ret;
    }
    double side_area() const
    {
        double ret = 2*M_PI*r*h;
        return ret;
    }
    double r;
    double h;
    double fa;
    double sa;
};
typedef vector<Pancake> vpan_t;

bool lt_rad(const Pancake &p0, const Pancake &p1)
{
    bool lt = (p0.r < p1.r) || ((p0.r == p1.r) && (p0.h < p1.h));
    return lt;
}

bool lt_sa(const Pancake &p0, const Pancake &p1)
{
    bool lt = p0.sa < p1.sa;
    return lt;
}

class Syrup
{
 public:
    Syrup(istream& fi);
    void solve_naive();
    void solve();
    void print_solution(ostream&) const;
 private:
    void solve_subset(const vuints_t& idx);
    unsigned n, k;
    vpan_t pans;
    double solution;
};

Syrup::Syrup(istream& fi) : solution(0)
{
    fi >> n >> k;
    for (unsigned i = 0; i < n; ++i)
    {
        double r, h;
        fi >> r >> h;
        pans.push_back(Pancake(r, h));
    }
}

void Syrup::solve_subset(const vuints_t& idx)
{
    double s = 0;
    double maxr = 0;
    for (unsigned ki = 0; ki < k; ++ki)
    {
        unsigned i = idx[ki];
        const Pancake &pan = pans[i];
        if (maxr < pan.r)
        {
            maxr = pan.r;
        }
        double sa = pan.side_area();
        s += sa;
    }
    double fa = M_PI * maxr * maxr;
    s += fa;
    if (solution < s)
    {
        solution = s;
    }
}

void Syrup::solve_naive()
{
    vuints_t idx;
    combination_first(idx, n, k);
    solve_subset(idx);
    while (combination_next(idx, n))
    {
        solve_subset(idx);
    }
    
}

void Syrup::solve()
{
    sort(pans.begin(), pans.end(), lt_rad);
    if (k == 1)
    {
        for (unsigned i = 0; i < n; ++i)
        {
            const Pancake &pan = pans[i];
            double s = pan.fa + pan.sa;
            if (solution < s)
            {
                solution = s;
            }
        }
    }
    else
    {
        for (unsigned i = k - 1; i < n; ++i)
        {
            const Pancake &pan = pans[i];
            double s = pan.fa + pan.sa;
            sort(pans.begin(), pans.begin() + i, lt_sa);
            for (unsigned j = i - (k - 1); j < i; ++j)
            {
                const Pancake &jpan = pans[j];
                s += jpan.sa;
            }
            if (solution < s)
            {
                solution = s;
            }
        }
    }
}

void Syrup::print_solution(ostream &fo) const
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

    void (Syrup::*psolve)() =
        (naive ? &Syrup::solve_naive : &Syrup::solve);

    ostream &fout = *pfo;
    bool tellg = getenv("TELLG");
    ul_t fpos_last = pfi->tellg();
    for (unsigned ci = 0; ci < n_cases; ci++)
    {
        Syrup problem(*pfi);
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
