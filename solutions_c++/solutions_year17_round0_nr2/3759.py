#include <iostream>
#define h 1000000007
#include <vector>
#include <map>
#include <utility>

using namespace std;

int main(){
    int whatt,up=1;
    cin>>whatt;
    while(whatt--){
        string s;
        int flag = 0;
        cin>>s;

        int pre;
        for(int i =0;i<s.size()-1;i++){
            pre= i;
            char a = s[pre];
            if(s[i]==a){

                while(i<s.size()-1 && s[i]==a)
                    i++;
                    i--;
            }
            if(s[i]>s[i+1]){
                if(s[i]!= '1' && s[i]!= '0'){
                    if(pre!=0){
                        s[pre] = max(char(s[i]-1),s[pre-1]);
                        //cout<<"here "<<s[pre];
                        }else {s[pre] = char(s[i]-1);

                        }
                        for(int k = pre+1;k<s.size();k++)
                            s[k]='9';
                    break;
                }else{
                s.resize(s.size()-1);
                for(int k=0;k<s.size();k++)
                    s[k]='9';
                }
            }
                    }
        cout<<"Case #"<<up++<<": "<<s<<endl;
    }
    return 0;
}
