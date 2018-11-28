#include<iostream>
#include<sstream>
#include<fstream>
#include<vector>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<functional>
#include<climits>
#include<utility>
#include <iomanip>
#include<map>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int,int> pi;
typedef pair<ll,ll> pl;

#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define FOR(i,s,e) for (int i = int(s); i < int(e); i++)
#define REP(i,x) FOR(i,0,x)
#define CLR(a) memset((a), 0 ,sizeof(a))


const int MOD = 1e+9+7;
const double PI  = acos(-1.0);

int main(){
    int T;
    cin>>T;
    REP(t,T){
        cout<<"Case #"<<(t+1)<<": ";
        string s;
        int n;
        cin>>s>>n;
        int l=s.size();
        int flipend[l];
        CLR(flipend);
        int ret=0;
        int acc=0;
        REP(i,l){
            int side=acc+(s[i]=='-');
            if(side%2){
                if(i>l-n){
                    ret=-1;
                    cout<<"IMPOSSIBLE\n";
                    break;
                }
                ret++;
                acc++;
                flipend[i+n-1]=-1;
            }
            acc+=flipend[i];
        }
        if(ret>=0){
            cout<<ret<<"\n";
        }

    }
}
