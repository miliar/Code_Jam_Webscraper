#include <iostream>
#include<math.h>
#include <fstream>
using namespace std;

string solve(int intNum);
bool isTidy(const string& sample);


//cout<<"Case #"<<i+1<<": "<<moves<<endl;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int testcase,intNum;
    cin>>testcase;

    for(int i = 0; i < testcase; i++){

        cin>>intNum;
        string lastTidyNum = solve(intNum);

        cout<<"Case #"<<i+1<<": "<<lastTidyNum<<endl;
    }
    return 0;
}

string solve(int intNum){

    string lastTidyNumber;
    string sample;


    for(int i = 1; i <= intNum; i++){
        sample = std::to_string(i);
        if(isTidy(sample)){
            lastTidyNumber = sample;
        }
    }

    return lastTidyNumber;

}



bool isTidy(const string& sample){
    for(int i = 0; i < sample.size() - 1; i++)
        if(sample[i] > sample[i+1])
            return false;

    return true;

}
