#include <iostream>
using namespace std;

int main(){

    int t,a,c,b;
    long long n,k,m;
    cin >> t;
    c = t;
    while(t--){
        long long x,y,z,w,xx,yy;
        x = 1;
        y = 1;
        cin >> n>>k;
        //cout << "CASE: " << c-t << " n = " << n << ", k = " << k << endl;
        if(k>1){
                yy=k;
        while(k>0){
            k/=2;
            y *= 2;
            x += 1;
        }
        y = (y+1)/2;
        xx = yy-y+1;
        //cout << "y=" << y << endl;


        z = (n-y+1)%y;
       // cout << "x=" << z << endl;
        if(z ==0 ) z = y;
        //cout << "n-y+1-x = " << n-y+1-z<<endl;
        w = (n-y+1-z)/y;
        //cout << "q=" << w << endl;
        if(xx<=z) w++;
        //cout << "q=" << w << endl;
        //cout << "xx=" << xx <<endl;
        }
        else if (k==1){
            w = n;
        }

        if(w%2==0) cout << "Case #" << c-t << ": " << w/2 << " " << w/2-1 << endl;
        else cout << "Case #" << c-t << ": " << w/2 << " " << w/2 << endl;
    }







return 0;}
