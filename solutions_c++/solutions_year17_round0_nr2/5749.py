#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    freopen("B-small-attempt0.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,test=1;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        int v;
        do{
            v=n;
            while(v){
                if(v%10 >= (v/10)%10)v/=10;
                else break;
            }
            if(v == 0){
                v = n;
                break;
            }
        }while(n--);
        cout << "Case #" << test << ": ";
        cout << v << endl;
        test++;
    }
    return 0;
}
