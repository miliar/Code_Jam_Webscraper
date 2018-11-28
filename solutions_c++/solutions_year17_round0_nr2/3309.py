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
        cin>>s;
        int ptr=0;
        int i=0;
        while(i<s.size()){
            if(s[ptr]>s[i]) break;
            if(s[ptr]<s[i]) ptr=i;
            i++;
        }
        if(i==s.size()) ptr=i;
        ll ret=0LL;
        REP(i,s.size()){
            ret*=10;
            if(i<ptr) ret+=s[i]-'0';
            else if(i==ptr) ret+=s[i]-1-'0';
            else ret+=9;
        }
        cout<<ret<<"\n";

    }
}
