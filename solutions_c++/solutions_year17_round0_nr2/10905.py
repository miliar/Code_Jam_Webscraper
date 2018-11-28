#include <iostream>
#include <cstdio>
using namespace std;

bool checknum(int x,int y){
    if(x<=y){
        return true;
    } else {
        return false;
    }
}

int main(){

    int T,c;
    bool T0,T1,T2;
    scanf("%d",&T);

    for(int i=0;i<T;i++){
        scanf("%d",&c);
        if(c/10 == 0){
            cout << "Case #" << i+1 << ": " << c << endl;
        } else if(c/1000 != 0){
             T0 = false;
             T1 = false;
             T2 = false;
            while(!(T0 && T1 && T2)){
                T0 = checknum(c/1000,c/100%10); // 1 < 2
                T1 = checknum(c/100%10,c/10%10);
                T2 = checknum(c/10%10,c%10);
                if(T0 && T1 && T2){
                    cout << "Case #" << i+1 << ": " << c << endl;
                } else {
                --c;
                }
		}
	 } else if(c/100 != 0){
             T0 = false;
             T1 = false;
          while(!(T0 && T1)){
            T0 = checknum(c/100%10,c/10%10); // 1 < 2
            T1 = checknum(c/10%10,c%10);
            if(T0 && T1){
                cout << "Case #" << i+1 << ": " << c << endl;
            } else {
               --c;
            }
         }

        } else if(c/10 != 0){
            T0 = false;
            while(!T0){
                T0 = checknum(c/10%10,c%10);
                if(T0){
                    cout << "Case #" << i+1 << ": " << c << endl;
                } else {
                    --c;
                }
            }
        }
    }
}
