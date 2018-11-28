//
//  main.cpp
//  GCJ_QR_B
//
//  Created by Yuto Murashita on 08/04/2017.
//  Copyright © 2017 Yuto Murashita. All rights reserved.
//

#include <iostream>
using namespace std;

class number{
    int digit[20];
public:
    int l;
    number(long long N){
        l=0;
        while(N!=0){
            digit[l]=N%10;
            N/=10;
            l++;
        }
    }
    bool is_tidy(void){
        for(int i=0; i<l-1; i++){
            if(digit[i]<digit[i+1]) return false;
        }
        return true;
    }
    void tidy_up(void){
        while(!is_tidy()){
            for(int i=l-1; i>=0; i--){
                if(digit[i]>digit[i-1]){
                    digit[i]-=1;
                    for(int j=i-1; j>=0; j--)
                        digit[j]=9;
                    break;
                }
            }
        }
    }
    long long number_form(void){
        long long tmp=0;
        for(int i=l-1; i>=0; i--){
            tmp=tmp*10+digit[i];
        }
        return tmp;
    }
};

int main(int argc, const char * argv[]) {
    int T;
    long long N;
    cin>>T;
    for(int t=1; t<=T; t++){
        cin>>N;
        number tmp(N);
        tmp.tidy_up();
        cout<<"Case #" << t << ": " << tmp.number_form() << endl;
    }
    
    return 0;
}
