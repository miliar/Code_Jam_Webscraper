#include<bits/stdc++.h>
 using namespace std;
 int main(){
    int Test, k, result;
    vector<int> flag;
    bool find;
    string input;
    cin>>Test;
    for(int jj = 1; jj <= Test; jj++){
        cin>>input>>k;
        find = true;
        result = 0;
        for(int i = 0; i <= input.length()-k; i++){
            if(input.at(i) == (char)45){
                result++;
                for(int j = 0; j < k; j++){
                    if(input.at(i+j) == (char)43){
                        input.at(i+j) =(char)45;
                    }
                    else{
                        input.at(i+j) = (char)43;
                    }
                }
            }
        }
        for(int i = input.length()-k+1; i < input.length(); i++){
            if(input.at(i) == (char)45){
                find = false;
            }
        }
        if(find == false){
            flag.push_back(-1);
        }
        else{
            flag.push_back(result);
        }
    }
    for(int j = 0; j < flag.size(); j++){
        cout<<"Case #"<<j+1<<": ";
        if(flag.at(j) == -1){
            cout<<"IMPOSSIBLE"<<endl;
        }
        else{
            cout<<flag.at(j)<<endl;
        }
    }
}
