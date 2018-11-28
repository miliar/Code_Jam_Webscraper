#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string arr;

void to_nine( int idx) {
    for(; idx<arr.size(); idx++)
        arr[idx] = '9';
}

string func() {
    int l = arr.size()-1;
    while(l>0) {
        if(arr[l] < '0') {
            arr[l] = '9';
            if(l+1 < arr.size() && arr[l+1]!='9')
                to_nine(l+1);
            arr[l-1]--;
        }
        if(arr[l] < arr[l-1]){
            arr[l] = '9';
            if(l+1 < arr.size() && arr[l+1]!='9')
                to_nine(l+1);
            arr[l-1]--;
        }
        l--;
    }
    while(arr[0] == '0') {
            arr = arr.substr(1, arr.size());
    }
    return arr;
}

int main()
{
    int tc;
    ifstream cinn("input.txt");
    ofstream coutt("output.txt");

    cinn >> tc;


    for(int i=0; i<tc; i++){
        cinn >> arr;
        coutt << "Case #" << i+1 << ": " << func() << endl;
    }
    return 0;
}
