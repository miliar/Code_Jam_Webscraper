#include <bits/stdc++.h>
#ifndef LOCAL
#define cerr dolor_sit_amet
#endif

#define mp make_pair
//#define sz(x) ((int)((x).size()))
#define X first
#define Y second

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair < int , int > ipair;
typedef pair < ll , ll > lpair;
const int IINF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3fll;
const double DINF = numeric_limits<double>::infinity();
const ll MOD = 1000000007;
const double EPS = 1e-9;
const int DX[] = { 1,  0, -1,  0,  1, -1,  1, -1};
const int DY[] = { 0,  1,  0, -1,  1, -1, -1,  1};
int manhattan(ipair a, ipair b)
{
    return abs(a.X-b.X)+abs(a.Y-b.Y);
}
//void clear( std::queue<int> &q )
//{
//   std::priority_queue<int> empty;
//   std::swap( q, empty );
//}

ifstream fin("data.in");
ofstream fout("data.out");
int main()
{

        int t,caz;
        ll n,k,rez;
        fin>>t;
        for(caz=1;caz<=t;caz++)
        {

            fin>>n>>k;
//            if(k==1)
//                rez=n;
//            else if(k==n)
//                rez=1;
//            else
//                rez=(n-k+2)/2;

            rez=n-k;
            while(k>>1)
            {
                rez>>=1;
                k>>=1;
            }
            ++rez;


//            cout<<'\n';



            if(rez&1)
                fout<<"Case #"<<caz<<": "<<rez/2<<' '<<rez/2<<'\n';
            else
                fout<<"Case #"<<caz<<": "<<rez/2<<' '<<rez/2-1<<'\n';
        }


//            fout<<"Case #"<<caz<<": "<<rez<<"\n";


    return 0;
}
