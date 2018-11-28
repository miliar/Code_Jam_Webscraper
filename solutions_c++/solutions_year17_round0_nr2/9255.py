#include <bits/stdc++.h>
#include <string>
using namespace std;

#define FOR(i,a)    for(int i = 0;i < a;i++)
#define REP(i,a,b)  for(int i = a;i < b;i++)
#define CL(a,b)		memset(a,b,sizeof a)
#define pb			push_back
#define LocalHost

typedef long double ld;
typedef long long ll;
typedef pair<int,int>	pii;
typedef pair<ld,ld>	pdd;
typedef vector<int> vi;
typedef vector<ld> vd;
typedef pair<ll,ll> pl;

string to_str(int ele){
    string ret;
    ret.clear();
    while(ele){
        ret.push_back(ele%10);
        ele/=10;
    }
    reverse(ret.begin(),ret.end());
    return ret;
}

int main(){
    #ifdef LocalHost
        freopen("input.in","r",stdin);
        freopen("output.out","w",stdout);
    #endif
    int testcases;
    cin>>testcases;
    int n;
    int cs=1;
    while(testcases--){
        cin>>n;
        while(n>=1){
            string str=to_str(n);
            string sostr=str;
            sort(sostr.begin(),sostr.end());
            if(sostr==str){
                cout<<"Case #"<<cs<<": "<<n<<"\n";
                break;
            }
            n--;
        }
        cs++;
    }

    #ifdef LocalHost

    #endif

    return 0;
}
