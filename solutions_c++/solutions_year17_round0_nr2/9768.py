#include <iostream>
#include <bits/stdc++.h>

//freopen("B-small-attempt().in","r",stdin);
//freopen("output.txt","w",stdout);

using namespace std;

int main()
{
    int T;
    cin >> T;
    int t=1;
    while (t<=T) {
        long long n;
        cin >> n;
        int f=0;
        while(n){
            long long m=n;
            while (m){
                if (m%10>=(m/10)%10){
                    f=1;
                }else{
                    f=0;
                    break;
                }
                m/=10;
            }
            if (f){
                cout << "Case #" << t << ": " << n << endl;
                break;
            }
            n--;
        }
        t++;
    }
    return 0;
}
