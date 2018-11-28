bool onlyonecase=false;
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include "math.h"
#include <stdexcept>
#include <iostream>
#include <fstream>
#include <array>
#include <vector>
#include <deque>
#include <list>
#include <forward_list> 
#include <set>
#include <map>
#include <unordered_set> 
#include <unordered_map> 
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <iterator>
#include <functional>
#include <cstdlib>
#include <string.h>
#include <sstream>

// Useful constants
#define INF                         (t)1e19
#define EPS                         1e-9
// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd
// Useful container manipulation / traversal macros
#define forall(i,a,b)               for (auto i=a;i!=b;i=(a<b)?i+1:i-1 )
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define IMPOSSIBLE "IMPOSSIBLE"

using namespace std;
istream * pin;

//typedef uintmax_t t;
typedef intmax_t t;

t konstansmod=(1e9)+7;

template<typename T>
vector<T> read(int num=-1,int szorzo=1,istream & in=*pin)
{
    vector<T> container;
    if (num==-1)
        in>>num;
    num*=szorzo;
    for (int i=0;i<num;i++)
    {
        T q;
        in>>q;
        container.push_back(q);
    }
    return container;
}


struct printer
{
ostream *o;
printer(ostream &a=cout):o(&a)
{

}

void pr()
{
*o<<"\n";
}

template<typename T>
void pr(T t)
{
*o<<fixed<<std::setprecision(9) << t<<"\n";
}

template<typename T>
void pr(vector<T> t)
{
    for(T w:t)
pr(w);
pr();
}

template<typename T, typename... Args>
void pr(T value, Args... args)
{
//cout<<value;
    pr(value);
pr(args...);
}

};
#define p(args...)  do { printer().pr(args); } while (false)
#ifdef DEBUG
#define dl(...) do {show(std::cerr, "Line", __LINE__);show(std::cerr, #__VA_ARGS__, __VA_ARGS__);} while (false)
#define d(...) do { show(std::cerr, #__VA_ARGS__, __VA_ARGS__); } while (false)
#else
#define dl(...) {}
#define d(...) {}
#endif

template<typename H1>
void show(std::ostream& out, const char* label, H1&& value) {
  //out << label << "=" << std::forward<H1>(value) << '\n';
// printer(out).pr(label+"=").pr(value);
out << label << "=" ;
printer(out).pr(value);
}

template<typename H1, typename ...T>
void show(std::ostream& out, const char* label, H1&& value, T&&... rest) {
  const char* pcomma = strchr(label, ',');
out.write(label, pcomma - label) << "=";
printer(out).pr(value);

 show(out,pcomma+1,std::forward<T>(rest)...);
}

void print(bool b)
{
    cout<<(b?"Yes":"No")<<"\n";
}

vector<double> gauss(vector< vector<double> > A) {
    int n = A.size();

    for (int i=0; i<n; i++) {
        // Search for maximum in this column
        double maxEl = abs(A[i][i]);
        int maxRow = i;
        for (int k=i+1; k<n; k++) {
            if (abs(A[k][i]) > maxEl) {
                maxEl = abs(A[k][i]);
                maxRow = k;
            }
        }

        // Swap maximum row with current row (column by column)
        for (int k=i; k<n+1;k++) {
            double tmp = A[maxRow][k];
            A[maxRow][k] = A[i][k];
            A[i][k] = tmp;
        }

        // Make all rows below this one 0 in current column
        for (int k=i+1; k<n; k++) {
            double c = -A[k][i]/A[i][i];
            for (int j=i; j<n+1; j++) {
                if (i==j) {
                    A[k][j] = 0;
                } else {
                    A[k][j] += c * A[i][j];
                }
            }
        }
    }

    // Solve equation Ax=b for an upper triangular matrix A
    vector<double> x(n);
    for (int i=n-1; i>=0; i--) {
        x[i] = A[i][n]/A[i][i];
        for (int k=i-1;k>=0; k--) {
            A[k][n] -= A[k][i] * x[i];
        }
    }
    return x;
}

t gcd(t a, t b)
{
    for (;;)
    {
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
    }
}

t lcm(t a, t b)
{
    t temp = gcd(a, b);

    return temp ? (a / temp * b) : 0;
}

void solve();
int main(int argc, char** argv) {
    srand((unsigned) time(NULL));
    ifstream * argfile=NULL;
    string filename="";
    if (argc>=2 && filename.length()==0)
        filename=argv[1];
    if (filename.length()>0)
    {
        argfile=new ifstream(filename);
        if (!argfile->is_open()) {
            cerr<<"file cant be opened,exiting. Filename:"<<filename<<"\n";
            cerr << "Error: " << strerror(errno)<<"\n";
            return 1;
        }
    }
    if (argfile) std::cin.rdbuf(argfile->rdbuf());
    istream & myfile=argfile?*argfile:cin;
    pin=&myfile;
    int num;
    if (onlyonecase)
    {
    solve(); return 0;
    }

    myfile>>num;
    for (int i = 0; i < num; i++) {
        cout<<"Case #"<<(i+1)<<": ";
        solve();
    }
    return 0;
}




void solve()
{
    t n,k;
    cin>>n>>k;
    vector<pair<t,t>> pos;
    forall(i,0,n)
    {
        t a,b;
        cin>>a>>b;
        pos.push_back({a,b} );
    }
    double max_v=0;
    function< void (set<t > &) > solve;
    solve=[&](auto & ww)
    {
        if (ww.size()==k)
        {
            t maxr=0;
            double sum=0;
            for (auto i:ww)
            {
                sum+=pos[i].first*2*M_PI*pos[i].second;
                maxr=max(pos[i].first,maxr);
            }
            sum+=(double)maxr*(double)maxr*M_PI;
            max_v=max(max_v,sum);
        }
        else
        {
        //    for( auto e:ww)
          //      d(e);
            t startv=-1;
            if (ww.size()!=0) startv=*ww.rbegin();
        forall (i,startv+1,n)
        {
            if (ww.find(i )==ww.end() )
            {
                auto ww2=ww;
                ww2.insert(i);
                solve(ww2);

            }

        }

        }


    };
    set<t> zz;
    //solve(zz);
    //printf("%.8lf\n",max_v );
    //return;



    double max_a=0;
    sort(pos.begin(),pos.end(),[&](auto &a, auto &b ) {
        double asize=a.first*a.first*M_PI*2.+2.*a.first*M_PI*a.second;
        double bsize=b.first*b.first*M_PI*2.+2.*b.first*M_PI*b.second;
        return a.first<b.first;
} );

    forall (qq,0,n)
    {
        d(qq,k,n);
        auto also=pos[qq];
auto pos3=pos;
pos3.clear();

forall(p,0,n)
{
    if (pos[p].first<=also.first && p!=qq)
            pos3.push_back(pos[p]);
}

if (pos3.size()+1<k) continue;

    sort(pos3.begin(),pos3.end(),[&](auto &a, auto &b ) {
        t asize,bsize;
        //double asize=a.first*a.first*M_PI*2.+2.*a.first*M_PI*a.second;
        //double bsize=b.first*b.first*M_PI*2.+2.*b.first*M_PI*b.second;

        asize=2*a.first*a.second;
        bsize=2*b.first*b.second;
        return asize>bsize;
    } );
    auto pos2=pos;
    pos2.clear();
    pos2.push_back(also);
    forall(i,0,k-1)
    {
    //    pos2.push_back(pos3[pos3.size()-1-i]);
            pos2.push_back(pos3[i] );
    }

    sort(pos2.begin(),pos2.end(),[&](auto &a, auto &b ) {
        double asize=a.first;
        double bsize=b.first;
        return asize>bsize;
    } );

double retsize=pos2[0].first*pos2[0].first*M_PI;
forall(i,0,k)
{
    d(pos2[i].first,pos2[i].second);
    retsize+=2.*pos2[i].first*M_PI*pos2[i].second;
}
max_a=max(max_a,retsize);
//if (pos3.size()==n) break;
 }
printf("%.8lf\n",max_a );

}


