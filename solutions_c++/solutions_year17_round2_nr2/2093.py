#include<bits/stdc++.h>
using namespace std;
int main(){
    int t,n,testca=0,num4,o,num2,g,num3,v,num1;
    cin>>t;
    while(t--){
        testca++;
        cin>>n>>num4>>o>>num2>>g>>num3>>v;
        cout<<"Case #"<<testca<<": ";
        num1=max(max(num4,num2),num3);
        if(num1==num4){
            if(num1>num2+num3){
                cout<<"IMPOSSIBLE";
            }
            else {
                while(num1!=(num2+num3)){
                    if(num2>num3){
                        cout<<"R"<<"Y"<<"B";
                    }
                    else{
                        cout<<"R"<<"B"<<"Y";
                    }
                    num2--;
                    num3--;
                    num1--;
                }
                while(num2!=0){
                    cout<<"R"<<"Y";
                    num2--;
                }
                while(num3!=0){
                    cout<<"R"<<"B";
                    num3--;
                }
            }
        }
        else if(num1==num2){
            if(num1>num4+num3){
                cout<<"IMPOSSIBLE";
            }
            else {
                while(num1!=(num4+num3)){
                    if(num4>num3){
                        cout<<"Y"<<"R"<<"B";
                    }
                    else{
                        cout<<"Y"<<"B"<<"R";
                    }
                    num4--;
                    num3--;
                    num1--;
                }
                while(num4!=0){
                    cout<<"Y"<<"R";
                    num4--;
                }
                while(num3!=0){
                    cout<<"Y"<<"B";
                    num3--;
                }
            }
        }
        else if(num1==num3){
            if(num1>num4+num2){
                cout<<"IMPOSSIBLE";			
            }
            else {
                while(num1!=(num4+num2)){
                    if(num4>num2){
                        cout<<"B"<<"R"<<"Y";
                    }
                    else{
                        cout<<"B"<<"Y"<<"R";
                    }
                    num4--;
                    num2--;
                    num1--;
                }
                while(num4!=0){
                    cout<<"B"<<"R";
                    num4--;
                }
                while(num2!=0){
                    cout<<"B"<<"Y";
                    num2--;
                }
            }
        }
        cout<<endl;
        
    }
    
}
