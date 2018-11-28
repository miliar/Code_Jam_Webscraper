#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    //freopen("B-small-practice.in","r",stdin);
    //freopen("output_file_name.out","w",stdout);
    int T;
    cin >> T;
    string s[T];
    int k[T];
    for(int i=0;i<T;i++){
        cin >> s[i] >> k[i];
    }
    for(int i=0;i<T;i++){
        string S=s[i];
        int K = k[i];
        int n=0;
        for(int j=0;j<S.length();j++){
            if(S.substr(j,1).compare("-")==0){
                if(j+K>S.length()){
                    n=-1;
                    break;
                }else{
                    string change = "";
                    for(int k=0;k<K;k++){
                        if(S.substr(j+k,1).compare("-")==0){
                            change += "+";
                        }else{
                            change += "-";
                        }
                    }
                    S = S.substr(0,j)+change+S.substr(j+K,S.length());
                    n++;
                }
            }
        }
        if(n==-1){
            cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
        }else{
            cout<<"Case #"<<i+1<<": "<<n<<endl;
        }
    }
    return 0;
}
