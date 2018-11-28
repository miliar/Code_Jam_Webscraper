#include <cstdio>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <cstring>
using namespace std;


int T,K;
char str[1001];
int a[1001];
int len;
int result;
int flipcount=0;

void print() {
    for(int i=0;i<len;i++){
        printf("%d",a[i]);
    }
    cout << endl;
}

void flip(int index){
    if(index+K > len) return;
    for(int i=index;i<index+K;i++){
        a[i] = 1-a[i];
    }
}

bool solve(){
    for(int i=0;i<len-K+1;i++) {
        //print();
        //printf("index %d\n",i);
        if(a[i] == 0) { 
            //printf("flip: index %d\n",i);
            flip(i); 
            flipcount++;}    
    }    
    
    for(int i=0;i<len;i++) {
        if(a[i] == 0) { return false; }    
    }
    return true;

}


int main() {
    cin >> T;
    
    for (int t=1;t<=T;t++) {
        cin >> str >> K;
        len = strlen(str);
        flipcount=0;
        for(int i=0;i<len;i++) {
            if(str[i] == '+') a[i] = 1;
            else a[i] = 0;
        }
        if (solve()) {
            printf("Case #%d: %d\n", t, flipcount);
        }
        else {
            printf("Case #%d: %s\n", t, "IMPOSSIBLE");
        }
    }

    return 0;
}
