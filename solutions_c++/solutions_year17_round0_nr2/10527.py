#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
    ifstream thefile1("input.in");
    ofstream thefile2("output.out");
    int T,N,X,Y,S;
    thefile1>>T;
    while(T--){
        thefile1>>N;
        X=N;
        while(1){
     Y=X;
     S=Y%10;
     Y=Y/10;
     while(Y>0&&Y%10<=S){
              S=Y%10;
        Y=Y/10;

        }
        if(Y==0){
        thefile2<<“Case #”<<100-T<<“:”<<“ “<<X<<endl;
        break;
        }
     else{
        X--;
     }
     }
    }
}
