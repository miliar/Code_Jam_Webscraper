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
    ifstream ifs("B-large.in");
    ofstream ofs("output.txt");
    int T;
    //cin>>T;
    ifs>>T;
    REP(t,T){
        string str;
        //cin>>S;
        ifs>>str;
        int sz=SZ(str);
        int sz2=0;
        REP(i,sz-1){
            if(str[i]>str[i+1])break;
            sz2++;
        }
        //cout<<sz2<<endl;どこまで条件をみたすか
        if(sz2==sz-1){
        }else if(sz2==0){
            str[0]--;
            FOR(i,1,sz)str[i]='9';
        }else{
            int tmp=sz2;
            while(tmp>=1&&str[tmp-1]>str[tmp]-1)tmp--;
            //cout<<tmp<<endl;
            str[tmp]--;
            FOR(i,tmp+1,sz)str[i]='9';
        }
        if(str[0]=='0')str=str.substr(1);
        cout<<"Case #"<<t+1<<": ";
        ofs<<"Case #"<<t+1<<": ";
        cout<<str<<endl;
        ofs<<str<<endl;
    }

    return 0;
}
