#include <bits/stdc++.h>
using namespace std;
#define lli long long int
#define fio ios_base::sync_with_stdio(0)
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define ii pair<int,int>
#define vi vector<int>
#define vvi vector<vi >
#define vii vector<ii >
#define vvii vector<vii >
#define ll pair<lli,lli>
#define vl vector<lli>
#define vvl vector<vl >
#define vll vector<ll >
#define vvll vector<vll >
#define M_PI 3.14159265358979323846
#define MOD 1000000007
#define MAX 200005
#define EPS 1e-12

bool goodtogo(string x){
    for(int i=0;i<x.length();i++)
        if(x[i]=='-') 
            return false;
    return true;
}
int main(){
    lli t,tc=1;
    cin>>t;
    while(t--){
        string s;
        lli k;
        cin>>s>>k;
        lli n=s.length();
        queue<pair<string,lli> > q;
        set<string> st;
        q.push(mp(s,0));
        st.insert(s);
        bool found=false;
        cout<<"Case #"<<tc<<": ";
        while(!q.empty()){
            pair<string,lli> xx=q.front();
            q.pop();
            if(goodtogo(xx.first)){
                found=true;
                cout<<xx.second<<"\n";
                break;
            }
            for(int i=0;i<=n-k;i++){
                string nwstr=xx.first;
                for(int j=i;j<=i+k-1;j++){
                    if(nwstr[j]=='+') nwstr[j]='-';
                    else nwstr[j]='+';
                }
                if(st.find(nwstr)==st.end()){
                    st.insert(nwstr);
                    q.push(mp(nwstr,xx.second+1));
                }
            }
        }
        if(!found)
            cout<<"IMPOSSIBLE\n";
        tc++;
    }
    return 0;
}