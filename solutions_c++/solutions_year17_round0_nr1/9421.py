#include<bits/stdc++.h>
using namespace std;
main(){
        ofstream fout("output.out");
        ifstream fin("input.in");
        int t;
        fin>>t;
        for(int i=1;i<=t;i++){
                string s;
                fin>>s;
                int k,cnt{};
                fin>>k;
                int pos=0;
                while(pos<s.length() && s[pos]=='+' ){
                pos++;
                }
                while((pos+k)<=s.length()){
                        if(s[pos]=='+'){
                                pos++;
                                continue;
                        }
                        cnt++;
                        for(int j=0;j<k;j++){
                                if(s[j+pos]=='-')
                                        s[j+pos]='+';
                                else
                                        s[j+pos]='-';
                        }
                pos++;
                }
                int flag=1;
                for(int j=0;j<s.length();j++){
                        if(s[j]=='-'){
                                flag=0;
                                break;
                        }
                }
                if(flag==1){
                        fout<<"Case #"<<i<<": "<<cnt<<"\n";
                }
                else{
                        fout<<"Case #"<<i<<": "<<"IMPOSSIBLE\n";
                }
        }
}
