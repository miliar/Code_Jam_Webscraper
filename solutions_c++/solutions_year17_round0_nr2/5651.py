#include <queue>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <fstream>
#include <cstring>
#include <string>
#include <climits>
#include <unordered_map>

using namespace std;

//macros
typedef long long ll;
typedef complex<double> point;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;




#define FOR(k,a,b) for(int k=(a); k<=(b); ++k)
#define REP(k,a) for(int k=0; k<(a);++k)
#define SZ(a) int((a).size())
#define ALL(c) (c).begin(),(c).end()
#define PB push_back
#define MP make_pair
#define INF 1000000001
#define INFLONG 1000000000000000000
#define MOD 1000000007
#define MAX 100
#define ITERS 100
#define MAXM 200000
#define MAXN 1000000
#define _gcd __gcd
#define eps 1e-7
#define PI 3.1415926535897932384626
using namespace std;

string tos(ll i){
    string ret = "";
    while(i>0){
        ret = char(i%10 + '0')+ret;
        i/=10;
    }
    return ret;
}
ll tol(string str){
    ll ret = 0;
    REP(i,str.length()){
        ret = 10*ret + int(str[i]-'0');
    }
    return ret;
}
string project(char c, int times){
    string ret = "";
    REP(i,times) ret = ret + c;
    return ret;
}
int comp(string s1, string s2){
    if(s1.length()>s2.length()) return 1;
    else if(s1.length()<s2.length()) return -1;
    for(int i = 0; i < s1.length(); i++){
        if(s1[i]>s2[i]) return 1;
        if(s1[i]<s2[i]) return -1;

    }
    return 0;
}
string maxim;
void construct(ll n){
    string str = tos(n);
    int len = str.length();
    maxim="";
    if(len==1){
        maxim = char(n + '0');
    } else{
        maxim = project('9',len-1);
    }
    //cout << comp("119","132")<<endl;
    REP(i,len+1){
        if(i>0 && str[i-1]=='0') break;
        //position of starting 9's
        //i...len-1
        //len-i
        string proj = project('9',len-i);
        string left = "";
        int highind = 1;


        for(int pos = 0; pos <= i-1; pos++){
            for(int dig = 9; dig >=highind; dig--){
                //cout << pos << " " << left+project(char(dig+'0'),i-pos)+proj<<endl;
                if(comp(left+project(char(dig+'0'),i-pos)+proj,str)!=1){

                    left = left + char(dig+'0');
                    highind=dig;
                    break;
                }
            }
        }

        string tot = left+proj;
        //cout << n << " " << tot << endl;
        if(comp(tot,str)!=1 && comp(tot,maxim)==1){
            maxim = tot;
        }
    }
}
int main() {

    int tests;
    ifstream fin("insert.in");
    ofstream fout("printo.txt");
    fin >> tests;
    for(int tr=1;tr<=tests;tr++){
        ll n;
        fin >> n;
        construct(n);
        fout << "Case #"<<tr<<": " << maxim << endl;
    }
    fout.close();

}
