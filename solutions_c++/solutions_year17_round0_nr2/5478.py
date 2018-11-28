//
// Created by limingwu on 17-4-8.
//

#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

string dealer(string& number){
    char result[20]={0};
    int length=number.size();
    int flag=0;

    strncpy(result, number.c_str(),length);
    if(length==1){
        return result;
    }


    for(int i=length-2;i>-1;--i){
        int j=i+1;
        if(result[j]<result[i]) {
            result[j] = '9';
            result[i] = result[i] - 1;
            flag = j;
        }
    }

    for(int i=flag;i<length;++i){
        result[i]='9';
    }

    if(result[0]=='0'){
        for(int i=1;i<length;++i){
            result[i-1]=result[i];
        }
        result[length-1]='\0';
    }

    return result;
}

void getTidy(vector<string>& numbers) {
    string result;
    int count = numbers.size();

    for (int i = 0; i < count; ++i) {
        result = dealer(numbers[i]);
        cout << "Case #" << i + 1 << ": " << result << endl;
    }
}

int main(){
    int lines;
    cin>>lines;

    vector<string> numbers;
    string tmp;

    for(int i=0;i<lines;i++){
        cin>>tmp;
        numbers.push_back(tmp);
    }
    getTidy(numbers);

    return 0;
}
