#include<bits/stdc++.h>// <3 Nandini <3
using namespace std;
#define gc getchar
#define mp make_pair
#define pb push_back
#define sc scanint
#define dc print_int
#define f first
#define s second
#define ret return 0;
#define rf std::ios::sync_with_stdio(false);
#define mi 1000000007
#define tl int t;sc(t);while(t--)
#define in int n;sc(n);
#define vin vi arr; for(int i=0;i<n;i++){int a;sc(a);arr.pb(a);}
#define st string s1; getline(cin>>ws,s1);
#define sorta sort(arr.begin(),arr.end());
#define reva reverse(arr.begin(),arr.end());
#define pf(a) printf("%d",a);
#define mina *min_element(arr.begin(),arr.end())
#define maxa *max_element(arr.begin(),arr.end())
#define sl scanlong
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long int ll;
typedef pair<int, int> pii;
typedef unsigned long long int ull;


void scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}
void scanlong(ull &x);
void scanlong(ull &x)
{
        int flag=0;
        register int c = gc();
        if(c == '-') flag=1;
	x = 0;
	for(;(c<48 || c>57);c = gc());
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
        if(flag == 1)x=-x;
}

using namespace std;

bool cross(pair<int, int>, pair<int, int>, int d);

int main(int argc, const char * argv[]) {
    int t;
    cin >> t;
    for (int i_t = 0; i_t < t; i_t++) {
        int n;
        pair<int, char> c[6];
        cin >> n;
        for (int i = 0; i < 6; i++) {
            cin >> c[i].first;
        }
        c[0].second = 'R';
        c[1].second = 'O';
        c[2].second = 'Y';
        c[3].second = 'G';
        c[4].second = 'B';
        c[5].second = 'V';
        sort(c, c + 6, greater<pair<int, char> >());
        string res;
        if (c[0].first > c[1].first + c[2].first) {
            cout << "Case #" << i_t + 1  << ": IMPOSSIBLE\n";
            continue;
        }
        if ((c[1].first + c[2].first - c[0].first) % 2 == 1) {
            res.push_back(c[1].second);
            c[1].first--;
        }
        int diff = (c[1].first + c[2].first - c[0].first) / 2;
        for (int i = 0; i < c[0].first; i++) {
            res.push_back(c[0].second);
            if (c[0].first - i + diff > c[2].first) {
                res.push_back(c[1].second);
            } else {
                res.push_back(c[2].second);
            }
        }
        for (int i = 0; i < diff; i++) {
            res.push_back(c[1].second);
            res.push_back(c[2].second);
        }
        cout << "Case #" << i_t + 1  << ": "<< res << "\n";
    }
    return 0;
}
