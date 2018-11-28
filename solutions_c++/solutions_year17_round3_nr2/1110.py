#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main(){
	int T;
	cin >> T;
	for(int ii = 0; ii < T; ii++){
        int C, J;
        cin >> C >> J;

        int ca, cb, ja, jb;
        int a, b, c, d;
        int exc;
        if(C == 2 || J == 2){
            cin >> a >> b >> c >> d;
        
            if(a < c){
                if(d - a <= 12*60 || 24*60 - c + b <= 12*60) exc = 2;
                else exc = 4;
            } else {
                if(b-c <= 12*60 ||24*60 - a + d <= 12*60) exc = 2;
                else exc = 4;
            }

            

            ///polnoc

        }
//10 01 11
        else {
          if(C == 1) cin >> ca >> cb;
          if(J == 1) cin >> ja >> jb;  
        
        
          if(C == 0 || J == 0) exc = 2;
          else{
            exc = 2;
          }
        
        }
        
        
        cout << "Case #" << ii+1 << ": ";
        cout << exc;
        
        //cout << (long double)D / (long double)max;
        cout << "\n";
	}
	return 0;
}
