#include <bits/stdc++.h>
using namespace std;
#define rep(it,st,en) for(int it=(st);it<(int)(en);++it)
#define allof(c) (c).begin(), (c).end()
#define mt make_tuple
#define mp make_pair
#define pb push_back
#define X first
#define Y second
typedef long long int ll; 
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
const int INF=(int)1e9; 
const double EPS=(ld)1e-7;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    rep(t,1,T+1){
        string s;
        cin>>s;
        int i=0;
        while(i<s.size()-1 && s[i] <= s[i+1]) ++i;
        if(i!=s.size()-1){
            int j=i;
            while(j>0 && s[j] == s[j-1]) --j;
            rep(k,j+1,s.size()) s[k] = '9';
            s[j]--;
            if(s[0]=='0') s = s.substr(1);
        }
        cout<<"Case #"<<t<<": "<<s<<endl;
    }
    return 0;
}
