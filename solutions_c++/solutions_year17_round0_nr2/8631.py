#include <stdio.h>
#include <vector>

using namespace std;

long findTidy(vector<int> &v){

    for(int i=1; i<v.size(); i++){
    
        if(v[i-1] < v[i]){
        
            v[i]--;
            for(int j=0; j<=i-1; j++){
                v[j] = 9;
            }
        
        }
    
    }
    
    long n=0;
    long multi = 1;
    
    for(int i=0; i<v.size(); i++){
        n += v[i]*multi;
        multi *= 10;
    }

    return n;
}


int main(){
    
    int T;
    
    scanf("%d", &T);
    
    for(int t=1; t<=T; t++){
    
        long n;
        
        scanf("%ld", &n);
    
        vector<int> number;
        
        while(n>0){
            number.push_back(n%10);
            n/=10;
        }
        
        printf("Case #%d: %ld\n", t, findTidy(number)); 
    
    }
    
    return 0;
}
