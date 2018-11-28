#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    vector<bool> surfp, surfm;
    string str;    
    int T;
    cin>>T;
    char inchar;
    int fsize;
    for(int cnum =1; cnum<=T; cnum++){
        surfp.clear();
        cin>>str;
        cin>>fsize;

        int n = str.length();
        for(int i=0; i<str.length(); i++){
            if(str[i]=='+'){
                surfp.push_back(true);
            }
            else{
                surfp.push_back(false);
            }
        }

        int i;
        // for +
        int pcnt=0;
        for(i=0; i<=n-fsize; i++){
            if(surfp[i]){
                continue;
            }
            else{
                //flip
                for(int j=i; j<i+fsize; j++){
                    surfp[j] = !surfp[j];
                }
                pcnt++;
            }
        }
        for(; i<n; i++){
            if(!surfp[i]){
                pcnt = 10000;
                break;
            }
        }
        cout<<"Case #"<<cnum<<": ";
        if(pcnt==10000){
            cout<<"IMPOSSIBLE\n";
        }
        else{
            cout<<pcnt<<endl;
        }
        
    }    
    return 0;
}
