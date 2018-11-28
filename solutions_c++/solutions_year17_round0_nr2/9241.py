#include<bits/stdc++.h>
#define MAX 0x3f3f3f
using namespace std;
int main(){
    int t, num, check, back, y;
    vector<int> flag;
    cin>>t;
    for(int test = 1; test <= t; test++){
        cin>>num;
        check = num;
        back = MAX;
        while(check){
            y = check%10;
            check = check/10;
            if(y > back){
                check = num = num-1;
                back = MAX;
            }
            else{
                back = y;
            }
        }
        flag.push_back(num);
    }
    for(int i = 0; i < flag.size(); i++){
        cout<<"Case #"<<i+1<<": "<<flag.at(i)<<endl;
    }
}
