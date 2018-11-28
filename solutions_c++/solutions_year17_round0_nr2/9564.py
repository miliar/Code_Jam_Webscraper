#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <valarray>
#include <algorithm>

using namespace std;

bool inOrder(string n){
    int i;
    for(i=0; i<n.length()-1; i++){
        if(n[i] > n[i+1]){
            return false;
        }
    }
    return true;
}

int main()
{
    FILE *fin = freopen("B-small-attempt0.in", "r", stdin);
    FILE *fout = freopen("B-small.out", "w", stdout);
    int i,j=0,t;
    string num;
    cin>>t;
    while(t--){
        j++;
        cin>>num;
        for(i=0; i<num.length()-1; i++){
            if(num[i] > num[i+1]){
                num[i] = num[i] - 1;
                num.replace(i+1,num.length()-1,num.length()-1-i,'9');
                break;
            }
        }
        while(num.length()>1 && num[0] == '0'){
           num.erase(0,1);
        }
        if(inOrder(num)){
            cout<<"Case #"<<j<<": "<<num<<endl;
        }else{
            num[0] -= 1;
            num.replace(1,num.length()-1,num.length()-1,'9');
            if(num[0] == '0'){
                num.erase(0,1);
            }
            cout<<"Case #"<<j<<": "<<num<<endl;
        }
    }
    return 0;
}
