#include <bits/stdc++.h>
using namespace std;

void turns( int pos, string &b ){
    for( int i=pos ; i<=b.size() ; i++ ){
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
        string a;
        cin >> a;
        string b;
        b += a[a.size()-1];
        for( int i=a.size()-2 ; i>=0 ; i-- ){
            if( a[i]>b[0] ){
                turns(0, b);
                b = (char)(a[i]-1) + b;
                a[i]--;
            }
            else{
                b = a[i]+b;
            }
        }
        if(b[0]=='0') b.erase(b.begin());
        printf("Case #%d: ", ++cas);
        cout << b << endl;
    }
    return 0;
}