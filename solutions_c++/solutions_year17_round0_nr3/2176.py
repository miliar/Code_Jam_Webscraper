#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {

    ll t, n, m, i, j, k, a, b, x, y, ans1, ans2, odd, even;
    cin>>t;
    string s;
    for (a = 1; a <= t; ++a) {
    	cin >> n;
        cin>>k;

        if (n%2==0) {
            even = 1;
            odd = 0;
            y = n;
            x = n-1;
        }
        else {
            odd = 1;
            even = 0;
            x = n;
            y = n-1;
        }

        while(k!=0) {
            
            if (x < y) {
                i = even+odd;
                if (k>i) {
                    if (((y-2)/2) %2==0) {
                        j = even;
                        even = 2*odd +even;
                        odd = j;
                        y = (x-1)/2;
                        x = y+1;
                    }
                    else {
                        odd = 2*odd+even;
                        even = even;
                        x = (x-1)/2;
                        y = x+1;
                    }
                    k-=i;
                    // cout<<"e"<<k<<" "<<odd<<" "<<even<<" "<<x<<" "<<y<<endl;
                }
                else if (k>even){
                    ans1 = (x-1)/2;
                    ans2 = ans1;
                    k = 0;
                }
                else {
                    ans1 = (y-2)/2;
                    ans2 = ans1+1;
                    k = 0;
                }
            }
            else {
                i = even+odd;
                if (k>i) {
                    if (((x-1)/2) %2==0) {
                        j = even;
                        even = 2*odd +even;
                        odd = j;
                        x = (y-2)/2;
                        y = x+1;
                    }
                    else {
                        odd = 2*odd+even;
                        even = even;
                        x = (x-1)/2;
                        y = x-1;
                    }
                    k-=i;
                    // cout<<"o"<<k<<" "<<odd<<" "<<even<<" "<<x<<" "<<y<<endl;
                }
                else if (k>odd){
                    ans1 = (y-2)/2;
                    ans2 = ans1+1;
                    k = 0;
                }
                else {
                    ans1 = (x-1)/2;
                    ans2 = ans1;
                    k = 0;
                }
            }


        }


		cout << "Case #" << a << ": ";

			cout<<max(ans1, ans2)<<" "<<min(ans1,ans2)<<endl;

	}


    return 0;

}