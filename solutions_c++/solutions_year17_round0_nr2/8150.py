#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<int(n);i++)
#define forsn(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define dforsn(i,s,n) for(int i=(int)(n-1);i>=int(s);i--)
#define si(a) ((int)(a).size())
#define pb push_back
#define mp make_pair
#define endl '\n'
#define all(a) a.begin(),a.end()
#define fastio ios_base::sync_with_stdio(false); cin.tie(0)
#define filein(a) freopen(a,"r",stdin)
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long int tint;

int main() {
	fastio;
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);

	int t;
	cin >> t;

	for(int c =1;c<=t;c++){
        string s;
        cin >> s;
        dforsn(i,1,si(s)){
            if(s[i]<s[i-1]){
                forsn(j,i,si(s))s[j]='9';
                s[i-1]--;
            }
        }
        cout << "Case #" << c <<": ";
        bool print = false;
        forn(i,si(s)){
            if(s[i]!='0'||print){
                print=true;
                cout<< s[i];
            }
        }
        cout << endl;
	}


	return 0;
}
