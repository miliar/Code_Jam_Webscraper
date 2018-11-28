#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector <double> vi;
typedef set <int> si;
typedef vector <vi> vvi;
typedef vector <char> vc;
typedef vector <vi> vvc;
typedef pair <double,double> ii;
typedef vector <ii> vii;
typedef tuple <int,int,int> iii;

const double pi = 3.14159265358979;
int n, k;
vi H, R;
double ma = 0;


void rec(vi& U){
    if(U.size() < n){
        int a = 0;
        for(auto x : U) a += x;
        if(a > k) return;
    }
    if(U.size() == n){
        int a = 0;
        for(auto x : U) a += x;
        if(a != k) return;

    //    for(auto x : U) cout << " " << x;
    //    cout << endl;

        double ss = 0;
        for(int i=0; i<U.size(); i++){
            if(U[i]) ss += 2*pi/1.0*R[i]/1.0*H[i]/1.0;
        }
        double r_max=0.0;
        for(int i=0; i<U.size(); i++){
            if(U[i]) if(r_max < R[i]) r_max = R[i]/1.0;
        }
     //   cerr << r_max << endl;
        ss += r_max/1.0*r_max/1.0*pi/1.0;
        if(ma < ss) ma = ss/1.0;
        return;
    }

    U.push_back(1);
    rec(U);
    U.pop_back();
    U.push_back(0);
    rec(U);
    U.pop_back();
}


int main(){
    cout.precision(9);
    cout.setf(ios::fixed);

    int cas_t;
    cin >> cas_t;
    for(int cas = 1; cas <= cas_t; cas++){
        cin >> n >> k;
        R = H = vi(n);
        ma = 0;

        for(int i = 0; i<n; i++) cin >> R[i] >> H[i];

        vi U;
        rec(U);

        cout << "Case #" << cas << ": " << ma << endl;
    }
}


