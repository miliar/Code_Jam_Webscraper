#include <bits/stdc++.h>
#define MOD 1000000007

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

ll n;
ll dp[20][10][2];

int get_digit(ll x,int k) {
    while(k--)
        x/=10;
    return x%10;
}

ll mul_digit(ll x, int k) {
    while(k--)
        x*=10;
    return x;
}

ll rek(int c_d, int l_d, int eq){
//    cout<<c_d<<" "<<l_d<<" "<<eq<<"\n";
    if(c_d == -1) {
        return 0;
    }
    if(dp[c_d][l_d][eq] == -1) {
        ll rez = -9000000000000000000;
        int no_dig=get_digit(n, c_d);
        for(int ctr1=l_d;ctr1<=9 - eq*(9-no_dig);ctr1++){
            rez = max(rez, mul_digit(ctr1,c_d) + rek(c_d-1,ctr1,eq && (ctr1 == no_dig)));
        }
        dp[c_d][l_d][eq] = rez;
    }
    return dp[c_d][l_d][eq];
}

int main()
{
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    int t,T;
    fin >> t;
    T = t;
    while(t--) {
        memset(dp,-1,sizeof(dp));
        fin >> n;
        ll rez = rek(log10(n)+1,0,1);
        fout<<"Case #"<<T-t<<": "<<rez<<"\n";
        cout<<"Case #"<<T-t<<": "<<rez<<"\n";
    }

    fin.close();
    fout.close();
    return 0;
}
