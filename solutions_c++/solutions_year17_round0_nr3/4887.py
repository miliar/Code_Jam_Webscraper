#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        long long int k,n;
        cin >> n >> k;
        int l,f,m,base,extras,nodo,ans,ans1,ans2;
        l = log2(k);
        m = pow(2,l);
        f = n-m+1;
        base = f/m;
        extras = f%m;
        nodo = k-m+1;
        ans = base;
        if (nodo <= extras){
            ans++;
        }
        ans1 = (ans)/2;
        ans2 = (ans-1)/2;
        cout << "Case #" << i+1 << ": " << ans1 << " " << ans2 << endl;
    }
    return 0;
}
