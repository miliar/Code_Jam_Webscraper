#include <bits/stdc++.h>

#define FOR(i,n)    for(lli i=0;i<(lli)(n);++i)
#define FORU(i,j,k) for(lli i=(j);i<=(lli)(k);++i)
#define FORD(i,j,k) for(lli i=(j);i>=(lli)(k);--i)

#define pb push_back
#define mt make_tuple

using namespace std;

using lli = long long int;
using pll = pair<lli, lli>;

using vi = vector<lli>;
using vvi = vector<vi>;
using pii = tuple<lli, lli>;
using vii = vector<pii>;
using vvii = vector<vii>;

#define X(a) get<0>(a)
#define Y(a) get<1>(a)
#define Z(a) get<2>(a)

string TYPE(const int*)          { return "%d";   }
string TYPE(const lli*)          { return "%lld"; }
string TYPE(const char*)         { return "%c";   }
string TYPE(const char**)        { return "%s";   }
string TYPE(const unsigned int*) { return "%u";   }

const int MAX_BUF = 100*1000+42;
char buf[MAX_BUF];

void RD() {}
template<typename T, typename... Args> 
void RD(T* v, Args... args)
{
    scanf((" " + TYPE(v)).c_str(), v);
    RD(args...);
}
template<typename... Args> 
void RD(string* v, Args... args)
{
    scanf(" %s", buf);
    (*v) = buf;
    RD(args...);
}

void PR(bool nl = true)
{ if(nl) printf("\n"); }
template<typename T, typename... Args> 
void PR(bool nl, T v, Args... args)
{
    printf((TYPE(&v) + " ").c_str(), v);
    PR(nl, args...);
}
template<typename... Args> 
void PR(bool nl, string& v, Args... args)
{
    printf("%s", v.c_str());
    PR(nl, args...);
}
template<typename... Args> 
void PR(Args... args)
{ PR(true, args...); }

const long long int oo = 1000*1000*1000;

struct Coord {
    int x, y;
    Coord(int x = 0, int y = 0) : x(x), y(y) {}
    Coord operator + (const Coord& droite) const
    { return Coord(x + droite.x, y + droite.y); }
};

struct AB {
    int k; vector<lli> arbre;
    AB(int _k = 20, lli def = 0) { k = _k;
        FOR(i, 1 << k)
            arbre.push_back(i < (1 << (k-1)) ? 0LL : def);
        FORD(i, ((1 << (k-1)) - 1), 1)
            arbre[i] = arbre[i << 1] + arbre[(i << 1) ^ 1];
    }
    void set(int i, lli x) { int feuille = i + (1 << (k-1));
        arbre[feuille] = x;
        iset(feuille >> 1);
    }
    void iset(int noeud) {
        if(noeud) {
            arbre[noeud] = arbre[noeud << 1] + arbre[(noeud << 1)  ^ 1];
            iset(noeud >> 1);
    }   }
    lli sum(int deb, int fin, int noeud = 1, int p = 0, int q = -1) {
        if(q < p) q = 1 << (k-1);
        if(deb <= p && q <= fin) return arbre[noeud];
        if(deb >= q || fin <= p) return 0LL;
        int mil = (p + q) / 2;
        return sum(deb, fin, noeud << 1, p, mil) + sum(deb, fin, (noeud << 1) ^ 1, mil, q);
    }
};

vector<int> flips;

int main()
{
    int nT;
    RD(&nT);
    FOR(i, nT)
    {
        string s;
        int k;
        RD(&s, &k);
        int cur = 0, j = 0;
        FOR(i, (int)s.size()-k+1)
        {
            while(j < (int)flips.size() && flips[j] <= i-k)
            {
                cur ^= 1;
                ++j;
            }
            if((s[i] == '-') ^ cur)
            {
                flips.push_back(i);
                cur ^= 1;
            }
        }
        bool valid = true;
        printf("Case #%lld: ", i+1);
        FORU(i, (int)s.size()-k+1, (int)s.size()-1)
        {
            while(j < (int)flips.size() && flips[j] <= i-k)
            {
                cur ^= 1;
                ++j;
            }
            if((s[i] == '-') ^ cur)
            {
                valid = false;
                printf("IMPOSSIBLE");
                break;
            }
        }
        if(valid) printf("%d", (int)flips.size());
        PR();
        flips.clear();
    }
    return 0;
}
