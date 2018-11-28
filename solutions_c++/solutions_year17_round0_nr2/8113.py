#include <iostream>
#include <vector>
#include <fstream>
//g++ -std=c++11 -o main *.cpp 
using namespace std;

//#define eps 0.001
#define dt int

string lastTidy(string number){
    if (number.size()==1){
        return number;
    }    
    int i,j;
    for(i=1;i<number.size() && number[i-1] <= number[i] ;i++);
    if (i== number.size()){
        return number;
    }
    i--;
    for (i;i>0;i--){
         if (number[i]-1 != '0' && number[i-1] <= number[i]-1 ){
            break;
        }
    }
    if (i == 0 && number[i] == '1'){
        string r ="";
        for(i=0;i<number.size()-1;i++){
            r+='9';
        }
        return r;
    }else{
        number[i]=number[i]-1;
        for(++i;i<number.size();i++){
            number[i]='9';
        }
    }
    return number;

}

int main(){
    
    ifstream cin("B-large.in");
    ofstream cout("B-large.out");
    //*/
    int c;
    string number;
    cin>>c;
    for (int i=0;i<c;i++){
        cin>>number;
        cout<<"Case #"<<(i+1)<<": "<<lastTidy(number)<<endl;
    }
    return 0;
}