#include<iostream>
#include<vector>
#include<fstream>

using namespace std;

int main(){
    ifstream in("B-large.in");
    ofstream out("B-large.out");
    int t;
    in >> t;
    string str;
    for(int h=0;h<t;++h){
        in >> str;
        int n = str.size();
        for(int i=n-2;i>=0;--i){
            if(str[i] > str[i+1]){
                str[i]--;
                for(int j=i+1;j<n;++j){
                    str[j] = '9';
                }
            }
        }
        while(str.front() == '0'){
            str.erase(str.begin());
        }
        out <<"Case #"<<h+1<<": "<<str<<endl;

    }
}
