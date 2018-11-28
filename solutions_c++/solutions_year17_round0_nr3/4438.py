#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <utility>
#include <iostream>
using namespace std;

typedef pair<long double, long double> PLL;

PLL f(long long n, long long k){
    if (k == 1)
        return make_pair(ceil(n/2), floor((n-1)/2));
    else{
        if (k%2 == 0)
            return f(n/2, k/2);
        else
            return f(floor((n-1)/2), k/2);
    }
}

int main(int p_Argc, char  **p_Argv)
{
    int nCas;
    cin >> nCas;
    cin.ignore();

    for (int cas = 0; cas < nCas; cas++){
        long long N, K ;
        cin >> N >> K;
        cin.ignore();
        PLL ans = f(N,K);

        cout << "Case #" << cas + 1 <<": ";

        cout << (long long) ans.first<<" "<<(long long) ans.second<<endl;
    }
    return 0;
}





