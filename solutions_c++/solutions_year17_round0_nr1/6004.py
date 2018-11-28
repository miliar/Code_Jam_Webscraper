#include <cstdio>
#include <string>
#include <iostream>
using namespace std;

int main(){
    int T; cin >> T;
    for(int tc=1;tc<=T;++tc){
        string str;
        int K,cnt=0;
        cin >> str >> K;
        for(int i=0; i<str.size()-K+1;++i){
            if(str[i]=='-'){
                cnt++;
                for(int j=0;j<K;++j)str[i+j]= str[i+j]=='-'? '+':'-';
            }
        }   
        bool Ans=true;
        for(int i=0;i<str.size();++i){
            if(str[i]!='+') {
                Ans=false;
                break;
            }
        }
        printf("Case #%d: ",tc);
        if(Ans) printf("%d\n",cnt);
        else printf("IMPOSSIBLE\n");
    }

    return 0;
}