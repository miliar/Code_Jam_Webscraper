#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<map>

using namespace std;

#define x first
#define y second
#define NMAX 10005

int answer[NMAX], T, n;

int ok(int N){
    int last = 10;
    while(N) {
        int last_cif = N % 10;
        if(last_cif > last)
            return 0;
        last = last_cif;
        N /= 10;
    }
    return 1;
}

int main (){
    
    for(int i = 1; i <= 1000; i++){
        if(ok(i)) {
            answer[i] = i;
        }
        else
            answer[i] = answer[i - 1];
    }

    scanf("%d",&T);
    for(int t = 1; t <= T; t++) {
        scanf("%d",&n);
        printf("Case #%d: %d\n", t, answer[n]);
    }
    
    
    return 0;
}


