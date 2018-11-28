#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <fstream>
#include<math.h>

using namespace std;


int main(){
    int64_t n;
    int64_t num;
    int64_t div;
    int64_t temp;
    int64_t res;
    int64_t digit;
    int64_t pass;
    int64_t nextDigit;
    int64_t s;
    bool isSmall;
    int zeroCount;
    ofstream fout;
    fout.open("output.txt");
    cin>>n;

    for(int i=0;i<n;++i){
        cin>>num;
        temp=num;
        res=0;
        s=0;
        isSmall=true;
        zeroCount=0;
        div=1;
        while(temp>0){
            digit=temp%10;
            temp=temp/10;
            s+=1;
            if(digit<=1)
            {
                if(digit==0)
                    zeroCount+=1;
            }
            else{
                isSmall=false;
            }
        }
        /*
        if(isSmall==true && zeroCount>0){
            temp=num;
            for(int j=0;j<s-1;++j){
                digit=temp%10;
                temp=int(temp/10);
                res+=9*div;
                div*=10;
            }
            fout<<"Case #"<<i+1<<": "<<res<<endl;
            continue;
        }*/
        s=1;
        div=1;
        temp=num;
        pass=0;
        while (temp>0){
            digit=temp%10-pass;
            temp=int(temp/10);
            nextDigit=temp%10;
            if(temp==0){
                res=ceil(res)+ceil(digit*pow(10,s-1));
                fout<<"Case #"<<i+1<<": "<<res<<endl;
            }
            if(nextDigit>digit){
                digit=9;
                pass=1;
                res=0;
                div=1;
                for(int j=0;j<s;++j){
                    res+=9*div;
                    div=div*10;
                }
            }
            else{
                pass=0;
                res+=digit*pow(10,s-1);
            }
            s+=1;
        }
    }
}
