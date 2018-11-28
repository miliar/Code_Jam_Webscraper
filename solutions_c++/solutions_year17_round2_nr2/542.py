#include<bits/stdc++.h>
#define mp make_pair
#define PII pair<int,int>
#define fi first
#define se second
#define pb push_back
#define ll long long
#define ull unsigned long long
#define ui unsigned int
#define sci(x) scanf("%d",&x)
#define scs(s) scanf("%s",s)
#define scc(c) scanf("%c",c)
#define scd(d) scanf("%lf",&d)
#define scld(ld) scanf("%Lf",&ld)
using namespace std;

//********************************************
//Error tracking
#define show(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }

vector<string> split(const string& s, char c) {
    vector<string> v;
    stringstream ss(s);
    string x;
    while (getline(ss, x, c))
        v.emplace_back(x);
    return move(v);
}

void err(vector<string>::iterator it) {}
template<typename T, typename... Args>
void err(vector<string>::iterator it, T a, Args... args) {
    cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << '\n';
    err(++it, args...);
}
//********************************************

const int NMAX = 1005;

int t,N, R, Y, B, O, G, V;
char sol[NMAX];

int main(){
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    cin.sync_with_stdio(false);
    
    cin >> t;
    for (int jj = 1; jj <= t; jj++){
        cout << "Case #" << jj << ": ";

        cin >> N >> R >> O >> Y >> G >> B >> V;

        int mx = max(R, max(Y, B));
        if (mx >= N / 2 + 1) cout << "IMPOSSIBLE\n";
        else{
            sol[0] = 'T';
            for (int i = 1; i <= N; i++) {
                char C;
                int act = 0;
                if (R > act && sol[i - 1] != 'R') {C = 'R'; act = R;}
                if (B > act && sol[i - 1] != 'B') {C = 'B'; act = B;}
                if (Y > act && sol[i - 1] != 'Y') {C = 'Y'; act = Y;}

                sol[i] = C;

                if (C == 'R') R--;
                if (C == 'B') B--;
                if (C == 'Y') Y--;
            }
            if (N > 1 && sol[1] == sol[N])
            {
                int ok = 0;
                for (int i = N; i > 1 && !ok; i--)
                {
                    swap(sol[i], sol[i - 1]);
                    if (sol[i] != sol[i - 1] && sol[i - 1] != sol[i - 2]) ok = 1;
                }
            }
            for (int i = 1; i <= N; i++) cout << sol[i];
            cout << "\n";
        }

    }
    return 0;   
}