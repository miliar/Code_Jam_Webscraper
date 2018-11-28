







#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;


bool isTidy(int s){
    vector<int> numToS;
    numToS.clear();
    while (s!=0) {
        int tmp = s%10;
        numToS.push_back(tmp);
        s = s/10;
    }
    for (int i=0; i<numToS.size()-1; i++) {
        if (numToS[i]<numToS[i+1]) {
            return false;
        }
    }
    return true;
}

void modify(int *s){
    *s = *s - 1;
}

int main() {
    
    
    int t;
    scanf("%d", &t);
    //char*s = (char*)malloc(20);
    int s;
    for (int i=0; i<t; i++) {
        scanf("%d", &s);
        while (!isTidy(s)) {
            modify(&s);
        }
        printf("Case #%d: %d\n", i+1, s);
        
    }
    
    
    
    return 0;
}
