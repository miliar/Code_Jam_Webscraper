#include <bits/stdc++.h>
using namespace std;

int f[2][1500][750];

int C, J;

int a[1500];
void simulate(int s){

    memset(f, 0x3f, sizeof(f));
    for(int i = 0; i < 1440; i++){
        // f[0][i][j], C doing work at time i, remaining time C is j
        // remaing for J is i+1-j
        //for(int j = 0; j <= 720 && j <= i+1 && i+1 - j <= 720; j++){
        for(int j = 0; j <= 720; j++){
            if(a[i] != 1 && j >= 1){
                if(i == 0){
                    f[0][i][j] = s;
                    continue;
                }
                f[0][i][j] = 1 + f[1][i-1][j-1]; 
                if(j >= 2)
                    f[0][i][j] = min(f[0][i][j], f[0][i-1][j-1]); 
            }

            if(a[i] != 2 && i+1-j >= 1){
                if(i == 0){
                    f[1][i][j] = 1-s;
                    continue;
                }
                f[1][i][j] = f[0][i-1][j] + 1;
                if(i+1-j >= 2)
                    f[1][i][j] = min(f[1][i][j], f[1][i-1][j]);
            }

            //if(i <= 5)
             // printf("%d   %d  %d %d\n", i, j, f[0][i][j], f[1][i][j]);
        }
    }
   /* 
    for(int k = 0; k <= 1; k++){
    
    printf("%d  user \n", k);

    for(int i = 5; i < 1440+5; i++){
        for(int j = i; j <= i ; j++)
            cout << i << " " <<  min(100, f[k][i][j]) << "\t"; 

        cout << endl;
    }
    
    }
    */
}



int work(){

    memset(a, 0, sizeof(a));

    cin >> C >> J;
    for(int i = 0; i < C; i++){
        int c, d;
        cin >> c >> d;
        for(int i = c; i < d; i++)
            a[i] = 1; // C has activities
    }

    for(int i = 0; i < J; i++){
        int c, d;
        cin >> c >> d;
        for(int i = c; i < d; i++)
            a[i] = 2; // J has activities
    }
    int ret = 0x3f3f3f3f;
    simulate(0); // last minute is C
    ret = min(ret, f[0][1440-1][720]);
    simulate(1);
    ret = min(ret, f[1][1440-1][720]);
    return ret;
}

int main(){

    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        printf("Case #%d: %d\n", i, work());
    }
    return 0;
}
