#include <bits/stdc++.h>
using namespace std;
#define forn(i,n) for(int i=0 ;i < (int)(n); i++)
#define forni(i,n) for(int i=1 ;i <= (int)(n); i++)
#define dforn(i, n) for( tint i=(int) (n)-1 ;i >= 0; i--)
typedef long long tint;
const int MAXN=500100, inf=1e9;

int n, p, am[55], boxes[55][55], pos[55], ans, l, r, L, R, posm, minr;
bool andamos;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("Output_Problem_2.txt", "w", stdout);
    int t;
    cin >> t;
    forn(cs, t){
    //while(cin >> n){
        cin >> n >> p;
        memset(pos, 0, sizeof pos);
        forn(i, n)cin >> am[i];
        forn(i, n){
            forn(j, p)cin >> boxes[i][j];
            sort(boxes[i], boxes[i]+p);
        }
        andamos = true; ans = 0;
        //cout << "Tenemos:"; forn(i, n)cout << " " << am[i]; cout << endl;
        while(andamos){
            L = -inf; R = inf;
            forn(i, n){
                l = ((boxes[i][pos[i]] * 10 + 10) / 11 + am[i] - 1) / am[i];
                r = boxes[i][pos[i]] * 10 / 9 / am[i];
                L = max(L, l);
                R = min(R, r);
            }
            /*cout << "Examinando...\n  ";
            forn(i, n)cout << boxes[i][pos[i]] << " "; cout << endl;
            cout << "L es " << L << " y R es " << R << endl;*/
            if(R >= L){
                forn(i, n)pos[i]++;
                ans++;
                //cout << "Anda.\n";
            }
            else{
                posm = -1; minr=inf;
                forn(i, n){
                    r = boxes[i][pos[i]] * 10 / 9 / am[i];
                    if(r < minr){minr = r; posm = i;}
                }
                pos[posm]++;
                //cout << "No anda, pusheamos el " << posm +1<< endl;
            }
            forn(i, n)if(pos[i] > p - 1)andamos = false;
        }
        cout << "Case #" << cs+1 << ": " << ans << "\n";

    }
    return 0;
}

