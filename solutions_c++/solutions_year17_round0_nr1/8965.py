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

int findfirst(string str){
    int32_t n=str.size();
    for(int32_t i=0;i<n;i++){
        if(str[i]=='-'){
            return i;
        }
    }
    return -1;
}


int main(){
    #ifdef LocalHost
        freopen("input.in","r",stdin);
        freopen("output.out","w",stdout);
    #endif
    int32_t testcases;
    cin>>testcases;
    for(int32_t cs=1;cs<=testcases;cs++){
        string str;
        int32_t k;
        cin>>str>>k;
        int32_t n=str.size();
        int32_t ctr=0;
        bool imp=false;
        while(1){
            int32_t idx=findfirst(str);
            if(idx==-1){
                break;
            }
            else if(idx>n-k){
                cout<<"Case #"<<cs<<": IMPOSSIBLE\n";
                imp=true;
                break;
            }
            else{
                for(int32_t j=idx;j-idx<k;j++){
                    str[j]=='+'?str[j]='-':str[j]='+';
                }
                ctr++;
            }
        }
        if(!imp){
            cout<<"Case #"<<cs<<": "<<ctr<<"\n";
        }
    }

    #ifdef LocalHost

    #endif

    return 0;
}
