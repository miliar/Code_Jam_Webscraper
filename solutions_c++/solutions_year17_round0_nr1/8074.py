#include <bits/stdc++.h>
#include <cstdio>
#include <cstdlib>

#ifdef _MSC_VER
#include <Windows.h>
#else
#include <unistd.h>
#endif

using namespace std;

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//math
//-------------------------------------------
template<class T> inline T sqr(T x) {return x*x;}

//typedef
//------------------------------------------
typedef pair<int, int> PII;
typedef pair<long, long> PLL;
typedef long long LL;
//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB emplace_back
#define MP make_pair
#define SZ(a) int((a).size())
#define SORT(c) sort((c).begin(),(c).end())

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);
const LL MOD=(double)1e9+7;
//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

#define DEBUG


int main(){
    ifstream ifs("A-large.in");
    ofstream ofs("output.txt");
    int T;
    //cin>>T;
    ifs>>T;
    REP(t,T){
        string str;int k;
        //cin>>str>>k;
        ifs>>str>>k;
        int cnt=0;
        vector<int>bl;
        REP(i,SZ(str)){
            if(str[i]=='-')bl.PB(-1);
            else bl.PB(1);
        }
        REP(i,SZ(bl)-k+1){
            if(bl[i]==-1){
                REP(j,k)bl[i+j]*=-1;
                cnt++;
            }
        }
        bool res=true;
        REP(i,SZ(bl)){
            if(bl[i]==-1){
                res=false;break;
            }
        }
        cout<<"Case #"<<t+1<<": ";
        ofs<<"Case #"<<t+1<<": ";
        if(!res){
            cout<<"IMPOSSIBLE"<<endl;
            ofs<<"IMPOSSIBLE"<<endl;
        }else{
            cout<<cnt<<endl;
            ofs<<cnt<<endl;
        }
    }

    return 0;
}
