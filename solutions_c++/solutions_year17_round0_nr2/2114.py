#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {

    ll t, n, m, i, j, k, a, b, x, ans;
    cin>>t;
    string s;
    for (a = 1; a <= t; ++a) {
    	cin >> n;
        m = 1;
    	bool flag = false;

        while(!flag) {
            flag = true;
            while(n/10 >= m) {
                if ((n/m)%10 < (n/(10*m)%10)) {
                    flag = false;
                    n = (n/(m*10))*(m*10);
                    break;
                }
                m = m*10;
            }
            if (flag) {
                n = n;
            }
            else {
                n = n-1;
            }
        }
    	

        ans = n;


		cout << "Case #" << a << ": ";

			cout<<ans<<endl;

	}


    return 0;

}