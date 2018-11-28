#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

// C++
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
#include <string.h>

#include <unordered_map>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;

// Input macros
#define s(n)                        scanf("%d",&n)
#define p(n)                        printf("%d\n",n)
#define pl(n)                       printf("%lld\n",n);
#define INF                         (int)1e9
#define EPS                         1e-9
// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())
#define DBG(vari) cerr<<#vari<<" = "<<(vari)<<endl;
#define mod 1000000007LL

// Useful container manipulation / traversal macros
#define all(n)                      for(int i=0;i<n;i++)
#define alls(m)                     for(int j=0;j<m;j++)
#define rep(a,n)                    for(int i=a;i<n;i++)
#define each(v, c)                  for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all1(a)                     a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                   memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair
#define init(Arr) memset((Arr), 0, sizeof (Arr))


int cases,a,b,c,d,i,j,k,n,m,t,ar[1000001],flag,w[1010][1010];
string ch[100],ch2;
pii p;

bool myfunction (int i,int j) { return (i<j); }

bool sortinrev(const pair<int,int> &a, 
               const pair<int,int> &b)
{
       return (a.first > b.first);
}

int main() 
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cases;

    cin>>cases;
   


    for(int t=1;t<=cases;t++)
    {
        long long sum ,cur;

        long double ans = 0 ;
        vector<pair<long, long> > v;
        cout<<"Case #"<<t<<": ";

        cin>>n>>k;

        for(i=0;i<n;i++){
            cin>>a>>b;
            v.pb(mp(a,b));
        }

        sort(v.begin(),v.end(),sortinrev);
        
        for(i=0;i<n-k+1;i++){

            //cout<<"yo";
            cur =0;
            sum =0 ;
            vector <long long>  temp ;
            long st = v[i].first;

            cur += st * st ;
            cur += long((long)2 * (long)st * (long)v[i].second);
           // cout<<st<<" ";

            for(j=i+1;j<n;j++){
                temp.pb(long (v[j].first*v[j].second ) );
            }
           

            sort(temp.begin(),temp.end(),greater<long long>() );
            


            for(j=0;j<k-1;j++){
                
                //cout<<temp[j] <<" ";
                sum+=temp[j];     
                 }   

            sum *=2;
            cur +=sum;

            //cout<<cur<<"\n";
            if(ans<cur)
                ans=cur;

        }

       // cout<<ans <<"\n";
        ans=ans*(double)3.1415926535897932384626433832795028841971693;
        printf("%0.8Lf\n",ans);

    }

    return 0;
}