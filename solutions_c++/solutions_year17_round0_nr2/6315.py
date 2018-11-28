#include <cstdio>
#include <cmath>
#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <map>
#include <cassert>
#include <string>
#include <cstring>
#include <queue>
using namespace std;
typedef int64_t ll;

ll t;



string s[101];
void checkUptoStart(string &res,int index){
    int i=index;
    while(i>0){
        if(res[i-1]>res[i]){
            res[i]='9';
            res[i-1]=res[i-1]-1;
            checkUptoStart(res,i-1);
        }
        i--;
    }


}

void computeRes(string &bs){

    int len=bs.length();
    int i;
    int si=0;
    int carry=0;
    for(i=0;i<(len-1);i++){
        if(bs[i]>bs[i+1]){
            //reduce i+1 to 9
            if(carry==0){
                bs[i+1]='9';
                bs[i]=bs[i]-1;
                carry=1;
            }
            else
                bs[i+1]='9';

            checkUptoStart(bs,i);
            //reduce i by 1
        }
    }

}


int main(){

    cin>>t;
    int i;
    for(i=1;i<=t;i++){
        cin>>s[i];
    }

    for(i=1;i<=t;i++){
        computeRes(s[i]);
    }

    for(i=1;i<=t;i++){
        int j=0;
        while(s[i][j]=='0')
            j++;
        cout<<"Case #"<<i<<": ";
        cout<<s[i].substr(j)<<endl;
    }





    return 0;

}


