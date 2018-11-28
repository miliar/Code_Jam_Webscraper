#include<bits/stdc++.h>

#define ull unsigned long long int
#define lli long long int
#define li long int
#define mp make_pair
#define pb push_back
#define ft first
#define sc second

#define Tr(S) printf(S);
#define T(A,B) printf(A,"\t",B,"\n");

using namespace std;
const int MAX = 1e5+5;

long double Ti[MAX];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("AL.out", "w", stdout);

    int T;
    long double N,D;
    cin>>T;
    for(int i=1; i<=T; i++){
        cin>>D>>N;
        for(int i=0;i<N;i++){
            long double K,S;
            cin>>K>>S;
            Ti[i] = (D-K)/S;
        }

        sort(Ti,Ti+(lli)(N));
        long double Ans = Ti[(lli)(N-1)],res;
        res = D/Ans;

        cout << "Case #"<< i << ": ";
        std::cout << std::fixed;
        cout << std::setprecision(6) << res << "\n";
    }

    return 0;
}
