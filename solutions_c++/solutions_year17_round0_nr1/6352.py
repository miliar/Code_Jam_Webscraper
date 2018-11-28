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


void flip(string &basic_string, int i, int k);

string s[101];
int k[101];

void flip(string &basic_string, int index, int k) {

    int i;
    for(i=index;k-->0;i++){
        if(basic_string[i]=='-')
            basic_string[i]='+';
        else
            basic_string[i]='-';
    }

}


int getAns(string basic_string,int k) {

    int len=basic_string.length();
    int i;
    int ans=0;
    for(i=0;i<=(len-1);i++){
        if(basic_string[i]=='-'){
            if(len-i<k)
                return -1;
            else
            {
                flip(basic_string,i,k);
                ans++;
            }
        }
    }
    return ans;
}



int main(){

    cin>>t;
    int i;
    for(i=1;i<=t;i++){
        cin>>s[i]>>k[i];
    }

    int ans;
    for(i=1;i<=t;i++){
        ans=getAns(s[i],k[i]);
        cout<<"Case #"<<i<<": ";
        if(ans==-1)
            cout<<"IMPOSSIBLE";
        else
            cout<<ans;
        cout<<endl;

    }




    return 0;

}

