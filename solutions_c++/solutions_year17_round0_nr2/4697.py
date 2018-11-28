#include <bits/stdc++.h>
using namespace std;
#define INF 1ULL<<30
#define MAXN 1000000000000
#define pb push_back
#define mp make_pair
#define forn(r,a,b) for(int r = a; r<b; r++)
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie(0);
#define fst first
#define snd second

typedef long long int lli;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef pair<ii,string> iis;
typedef vector<iii> viii;
typedef vector<int> vi;
string number;
string answer;
int main(){
    int cc;
    cin >> cc;
    for(int t = 1; t<=cc; t++){
        cin >> number;
        int p = number.size() - 2;
        while(p>=0){
            while(number[p] <= number[p + 1 ] ) p--;
            for(int i = p + 1; i<number.size(); i++){
                number[i] = '9';
            }
            if(number[p+1] == '9') number[p]--;
        }
        printf("Case #%d: ",t);
        p = 0;
        while(number[p] == '0') p++;
        for(int i = p; i<number.size(); i++){
            cout << number[i];
        }
        cout << "\n";
    }
    return 0;

}
