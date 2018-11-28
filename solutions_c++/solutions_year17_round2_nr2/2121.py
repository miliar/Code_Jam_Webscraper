#include<bits/stdc++.h> //_Shaffi
using namespace std;
#define sc scanint
#define sl scanlong
#define gc getchar
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define in(a,arr) sc(a); arr.push_back(a);
#define mi 100000007
#define DO int t; scanf("%d",&t); while(t--)
#define st(arr); sort(arr.begin(),arr.end());
#define er(arr); arr.erase(unique(arr.begin(),arr.end()),arr.end());
#define INF INT_MAX
#define mx(arr) *max_element(arr.begin(),arr.end())
#define mn(arr) *max_element(arr.begin(),arr.end())
#define getst(s) getline(cin>>ws,s)
#define sci(a,b) sc(a),sc(b);
#define scl(a,b) sl(a),sl(b);
#define MAX 664579
typedef long long ll;
typedef vector<int> vi;
typedef vector<pair<int,int> > pi;
void scanint(int &x);
void scanlong(ll &x);
void scanint(int &x)
{
        int flag=0;
        register int c = gc();
        if(c == '-') flag=1;
	x = 0;
	for(;(c<48 || c>57);c = gc());
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
        if(flag == 1)x=-x;
}
void scanlong(ll &x)
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
    int a=0;
    DO
    {
        int n;
        a++;
        pair<int, char> arr[6];
        cin >> n;
        for (int i = 0; i < 6; i++) {
            cin >> arr[i].first;
        }
        arr[0].second = 'R';
        arr[1].second = 'O';
        arr[2].second = 'Y';
        arr[3].second = 'G';
        arr[4].second = 'B';
        arr[5].second = 'V';
        sort(arr, arr + 6, greater<pair<int, char> >());
        string res;
        if (arr[0].first > arr[1].first + arr[2].first) {
            cout << "Case #" << a  << ": IMPOSSIBLE\n";
            continue;
        }
        if ((arr[1].first + arr[2].first - arr[0].first) % 2 == 1) {
            res.push_back(arr[1].second);
            arr[1].first--;
        }
        int diff = (arr[1].first + arr[2].first - arr[0].first) / 2;
        for (int i = 0; i < arr[0].first; i++) {
            res.push_back(arr[0].second);
            if (arr[0].first - i + diff > arr[2].first) {
                res.push_back(arr[1].second);
            } else {
                res.push_back(arr[2].second);
            }
        }
        for (int i = 0; i < diff; i++) {
            res.push_back(arr[1].second);
            res.push_back(arr[2].second);
        }
        cout << "Case #" << a  << ": "<< res << "\n";
    }
    return 0;
}
