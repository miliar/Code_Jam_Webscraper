#include <bits/stdc++.h>
#define for0(i, n) for(int i = 0; i < n; i++)
#define for1(i, n) for(int i = 1; i <= n; i++)
#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()
#define V vector<int>
#define VP vector<pair<int, int> >
#define clr(A, x) memset(A, x, sizeof(A))
#define cpy(A, B) memcpy(A, B, sizeof(B))
#define g(s) getline(cin, s) ///ai grija la fin/cin ///
#define FASTIO ios_base::sync_with_stdio(0)
const long long INFLL = (1LL<<62);
const int INFINT = 2000000000;
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
/*template <typename T>
string to_string(const T& n){
    ostringstream os;
    os << n;
    return os.str();
}*/

ifstream fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");
//ifstream fin("A-large-attempt0.in");
//ofstream fout("A-large-attempt0.out");

const int NMAX = 1e5 + 5;
const int MOD = 666013;
const double eps = 0.000000001;

int t, n;
double d;
deque<pair<double, double> > v;
deque<pair<double, double> > temp;



int main()
{
    fin >> t;
    for1(nr, t)
    {
        v.clear();
        fin >> d >> n;
        for1(i, n)
        {
            double a, b;
            fin >> a >> b;
            v.pb({a, b});
          //  temp.pb({a, b});
        }
        sort(all(v));
       // sort(all(temp));
        double sol = 1e9, tot = 0;
        for(;;)
        {
            double t = 1e9;
            V ind;

            //sol = d / ((d - v[0].first) / v[0].second);
            sol = tot + (d - v[0].first) / v[0].second;
            for0(i, v.size() - 1)
                if(v[i].second - v[i + 1].second > eps)
                {
                    if(t >= (v[i].first - v[i + 1].first) / (v[i].second - v[i + 1].second))
                    {
                        if(t != abs((v[i].first - v[i + 1].first) / (v[i].second - v[i + 1].second)))
                            ind.clear();

                        t = abs((v[i].first - v[i + 1].first) / (v[i].second - v[i + 1].second));
                        ind.pb(i);
                    }
                }
            if(ind.empty())
            {
               // sol = d / ((d - v[0].first) / v[0].second);
                break;
            }
            tot += t;
            for0(i, v.size())
                v[i].first += v[i].second * t;
            for(auto i: ind)
                v[i].second = v[i + 1].second;
            sort(all(v));
            if(abs(v[0].first - d) <= eps || v[0].first >= d)
                break;
            //cout << t << endl;
        }
        fout << "Case #" << nr << ": " << setprecision(7) << d / sol << '\n';
    }


    return 0;
}




