#include<bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef long long int ll;
typedef pair<int,int> pi;
typedef unsigned long long int ull;

ll lsone(ll p){return(p & -p);}

int TC,j;
char m[50];
string s;
ll n,k;

bool check(int i, int j){
    if (j>=n) return(true);
    if (s[j]>s[i]) return(true);
    if (s[j]<s[i]) return(false);
    return(check(i,j+1));
}

int main(){
    std::ios::sync_with_stdio(false);
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> TC;
    for (int outi=1;outi<=TC;outi++){
        cin >> s;
        cout << "Case #" << outi << ": ";
        n = s.size();
        j = 0;
        while (j<n && check(j,j+1)) j++;
        if (j<n){
            s[j]--;
            for (int i = j+1;i<n;i++) s[i] = '9';
        }
        j=0;
        while (s[j]=='0') j++;
        s = s.substr(j);
        cout << s << "\n";
    }

}
