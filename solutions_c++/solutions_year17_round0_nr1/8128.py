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
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
	int t;
	cin >> t;
	for(int c =1;c<=t;c++){
        string s;int k;
        cin >> s >> k;
        int cant = 0;
        forn(i,si(s)-(k-1)){
            if(s[i]=='-'){
                cant++;
                forsn(j,i,i+k)s[j]= (s[j]=='+') ? '-' : '+';
            }
        }
        cout << "Case #" << c << ": ";
        if(s.find('-')!=-1)cout<<"IMPOSSIBLE" << endl;
        else cout << cant << endl;
	}


	return 0;
}
