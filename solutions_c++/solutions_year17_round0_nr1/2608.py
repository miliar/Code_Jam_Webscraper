#include<iostream>
#include<algorithm>
#include<fstream>
#include <iomanip>
using namespace std;
string flip(string a,int k){
    for(int i = 0; i < k ; i++){
        if(a[i] == '+'){
            a[i] = '-';
        }else{
            a[i] = '+';
        }
    }
    return a;
}
int main(){
    ifstream cin("A-large.in");
    ofstream cout("result.txt");
    int n;
    cin >> n;
    for(int p = 0 ; p < n; p++){
        string s;
        int k;
        cin >> s >> k;
        int i = 0;
        int l = s.length();
        int sum = 0;
        while(true){
            if(i == l-k+1){
                break;
            }
            if(s[i] == '-'){
                sum++;
                string temp = flip(s.substr(i,k),k);
                s = s.substr(0,i)+temp+s.substr(i+k);
            }
            i++;
        }
        bool ch = true;
        for(int j = i ; j < l ; j++){
            if(s[j] == '-')
                ch = false;
        }
        if(ch){
            cout <<"Case #"<<p+1<<": "<<sum<<endl;
        }else{
            cout <<"Case #"<<p+1<<": "<<"IMPOSSIBLE"<<endl;
        }

    }
}
