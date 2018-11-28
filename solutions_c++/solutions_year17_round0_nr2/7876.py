#include <iostream>
#include <string>
#include <vector>

using namespace std;

void doTest(int tc){
    string number;
    cin>>number;
    unsigned carry=0;
    vector<int> minNumbers(number.length() ,0);
    int maxNum=0;

    int dealBreakerPosition=0; bool breakerFound=false;
    for(int i=0;i<number.length();++i){
        if((number[i]-48)>=maxNum){
            maxNum=number[i]-48;
        }else if(!breakerFound){
            breakerFound=true;
            dealBreakerPosition=i;
            carry=1;
        }
        if(breakerFound){
            number[i]=48+9;
        }
        minNumbers[i]=maxNum;
    }

    for (int i=dealBreakerPosition-1; i>=0; --i){
        int value=number[i]-48;
        value-=carry;
        value=(value<0)?9:(value);

        if(i==0){
            value=(value<0)?0:value;
        }else{
            if(value<minNumbers[i-1]){
                value=9;
                carry=1;  
            }else{
                carry=0;
            }
        }
        number[i]=value+48;
    }

    if(number[0]=='0')
        number=number.substr(1);

    cout<<"Case #"<<tc<<": "<<number<<endl;
}

int main(){
    int T; cin>>T;
    int tc=1;
    while(T--){
        doTest(tc++);
    }
}