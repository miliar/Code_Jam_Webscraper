#include <bits/stdc++.h>
using namespace std;
void turns(string &b ){
    for( int i=0; i<=b.size() ; i++ ){
        b[i] = '9';
    }
}
int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    int cas = 0;
    cin >> t;
    while( t-- ){
		printf("Case #%d: ",++cas);
        string a;
        cin >> a;
        string b;
        b += a[a.length()-1];
        for( int i=a.size()-2 ; i>=0 ; i-- ){
            if( a[i]>b[0] ){
                turns(b);
				a[i]--;
                b = a[i] + b;
            }
            else{
                b = a[i]+b;
            }
        }
        if(b[0]=='0') b.erase(b.begin());
        cout << b << endl;
    }
    return 0;
}
