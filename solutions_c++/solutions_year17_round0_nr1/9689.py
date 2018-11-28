#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<stack>
#include<vector>
#include<cctype>
#include<cstdio>
#include<string>
#include<sstream>
#include<cstring>
#include<cstdlib>
#include<fstream>
#include<iterator>
#include<iostream>
#include<algorithm>

using namespace std;

#pragma comment(linker,"/STACK:16777216")
#pragma warning(disable:4786)

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define myabs(a) ((a)<0?(-(a)):(a))
#define pi acos(-1.0)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define ff first
#define ss second
#define eps 1e-9
#define root 1
#define lft 2*idx
#define rgt 2*idx+1
#define cllft lft,st,mid
#define clrgt rgt,mid+1,ed
#define inf (1<<29)
#define i64 long long
#define MX 1000002

typedef pair<i64,i64> pii;
void toggle(string &s, int pos,int k){
    int i;
    for(i = pos; i < pos + k; i++){
        if(s[i]=='-')s[i] = '+';
        else s[i] = '-';
    }

}
int main(){
    i64 n, k, t = 1, cs, i, res;
    string s;
    cin>>cs;
    while(cs--){
        cin>>s>>k;
        res = 0;
        for(i = 0; i < s.size(); i++){
            if(s[i] == '-' && i + k - 1 < s.size()) {
                toggle(s, i, k);
                res++;
            }
        }
        int flag = 0;
        for(i = 0; i < s.size();i++){
            if(s[i] == '-') flag = 1;
        }
        printf("Case #%lld: ", t++);
        if(flag)cout<<"IMPOSSIBLE"<<endl;
        else cout<<res<<endl;
    }
	return 0;
}


