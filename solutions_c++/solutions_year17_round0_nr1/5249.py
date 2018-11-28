
#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>
#include <limits>
#include <cstring>
#include <unordered_set>
#include <stack>
#include <iostream>
#include <unordered_set>
using namespace std;
void Deal(string& str,int index,int k){
    for (int i = index; i<index + k; i++){
        if (str[i] == '-')str[i] = '+';
        else if (str[i] == '+')str[i] = '-';
    }
}
int numofTimes(string str, int k){
    int n = str.length();
    int i = 0;
    int times = 0;
    while (i<=(n-k)){
        if (str[i] == '-'){
            Deal(str,i,k);
            times++;
        }
        i++;
    }
    while (i < n){
        if (str[i] == '-'){
            return -1;
        }
        i++;
    }
    return times;
}


int main(){
     int T;
     cin>>T;
     int j=1;
     while(T--){
        string S;
        int K;
        cin>>S;
        cin>>K;
        int times=numofTimes(S,K);
        printf("Case #%d: ", j++);
        if(times==-1)cout<<"IMPOSSIBLE"<<endl;
        else cout<<times<<endl;
     }
}
