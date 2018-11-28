#include<bits/stdc++.h>// akash231997
using namespace std;
#define gc getchar
#define mp make_pair
#define pb push_back
#define sc scanint
#define dc print_int
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

int main() {
    int t;
    cin >> t;
    for (int in = 0; in < t; in++) {
        int n;
        pair<int, char> a[6];
        cin >> n;
        for (int i = 0; i < 6; i++) {
            cin >> a[i].first;
        }
        a[0].second = 'R';
        a[1].second = 'O';
        a[2].second = 'Y';
        a[3].second = 'G';
        a[4].second = 'B';
        a[5].second = 'V';
        sort(a, a+6, greater<pair<int, char> >());
        string s;
        if (a[0].first > a[1].first + a[2].first) {
            cout << "Case #" << in + 1  << ": IMPOSSIBLE\n";
            continue;
        }
        if ((a[1].first + a[2].first - a[0].first) % 2 == 1) {
            s.push_back(a[1].second);
            a[1].first--;
        }
        int diff = (a[1].first + a[2].first - a[0].first) / 2;
        for (int i = 0; i < a[0].first; i++)
            {
            s.push_back(a[0].second);
            if (a[0].first - i + diff > a[2].first)
             {
                s.push_back(a[1].second);
            }
        else
            {
                s.push_back(a[2].second);
            }
        }
        for (int i = 0; i < diff; i++) {
            s.push_back(a[1].second);
            s.push_back(a[2].second);
        }
        cout << "Case #" << in + 1  << ": "<< s << "\n";
    }
    return 0;
}
