#include <bits/stdc++.h>
#define X first
#define Y second

#define bitAt(a,b) (a & (1<<b))

using namespace std;

typedef long long LL;
typedef pair <int, int> PII;
typedef pair <LL,LL> PLL;

const int Maxn = 100*1000 + 250;
const int Mod = 1000 * 1000 * 1000 + 7;
const int abMax = 1 << 30 ;
const double EPS = 1e-9;
const double PI = acos(-1.0);

ofstream fout ("A-large.out");
ifstream fin ("A-large.in");

#define cin fin
#define cout fout

int n;
string s;

void doflip(int i , int k , string &st){

    if(i+k > st.size()){
        return;
    }

    for(int j = i ; j < i+k;j++){
        if(st[j] == '+'){
            st[j] = '-';
        }
        else{
            st[j] = '+';
        }
    }
}

int ans = 0;

int main() {
	ios::sync_with_stdio(0);
	int t;
	cin >> t;
	for(int tt = 0; tt < t ;tt++){
        cin >> s >> n;
        ans = 0;

        for(int i = 0 ; i < s.size();i++){
            if(s[i] == '-'){
                doflip(i,n,s);
                    //cerr << s << endl;
                ans++;
            }
        }
        bool flag = true;
        for(int i = 0 ; i < s.size();i++){
            if(s[i] == '-'){
                flag = false;
            }
        }
        cout << "Case #" << tt+1 << ": " ;
        if(flag)
            cout << ans ;
        else
            cout << "IMPOSSIBLE";
        cout << endl;
	}
}
