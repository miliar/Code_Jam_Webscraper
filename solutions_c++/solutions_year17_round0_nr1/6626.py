#include<vector>
#include <iostream>
 using namespace std;
 int main(){
    int t, no, count;
    bool check;
    string str;
    cin>>t;
    vector<int> vec;
    for(int jj = 1; jj <= t; jj++){
        cin>>str>>no;
        check = true;
        count = 0;
        for(int i = 0; i <= str.size()-no; i++){//
            if(str.at(i) == '-'){
                count++;
                for(int j = 0; j < no; j++){
                    if(str.at(i+j) == '+'){
                        str.at(i+j) ='-';
                    }
                    else{
                        str.at(i+j) = '+';
                    }
                }
            }
        }
        for(int i = str.size()-no+1; i < str.size(); i++){
            if(str.at(i) == '-'){
                check = false;
            }
        }
        if(check == false){
            vec.push_back(-1);
        }
        else{
            vec.push_back(count);
        }
    }
    for(int i = 0; i < vec.size(); i++){
        if(vec.at(i) < 0){
            cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
        }
        else{
            cout<<"Case #"<<i+1<<": "<<vec.at(i)<<endl;
        }
    }
}
