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

int main(){
    lli t,tc=1;
    cin>>t;
    string s,s1,s3,s2;
    while(t--){
        cin>>s1;
        s2="9";
        s3="0";
        s=s3+s1+s2;
        lli l=s.length();
        for(lli i=l-2;i>=0;i--){
            if(s[i]>s[i+1]){
                s[i]--;
                for(lli j=i+1;j<=l-1;j++){
                    s[j]='9';
                }
            }
        }
        cout<<"Case #"<<tc<<": ";
        for(lli i=1;i<l-1;i++){
            if(s[i]!='0')
                cout<<s[i];
        }
        cout<<"\n";
        tc++;
    }   
}