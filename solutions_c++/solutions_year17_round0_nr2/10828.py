#include <iostream>
#include <cstring>
#include <stdlib.h>
#include <sstream>
using namespace std;
main(){

        int T;
        cin >> T;
        for(int i=0;i<T;i++){
            long long no;
            cin >> no;
            long long k;
            for(k=no;k>0;k--){
                stringstream ss;
                ss << k;
                string temp;
                temp =ss.str();
                string lol;
                int zero = temp.rfind("0");
                if(zero>3){
                    for(int x=0;x<temp.length();x++){
                        if(x!=0)
                            lol+="9";
                        else{
                            if(temp[x]>49)
                                lol+=temp[x]-1;
                            else{}
                        }
                    }
                    cout <<"Case #"<< i+1<<": " <<lol << endl;
                    break;
                }
                else{
                    int j;
                    for(j=0;j<temp.length()-1;j++){
                        if(temp[j]<=temp[j+1]){

                        }
                        else{
                            break;
                        }
                    }
                    if(j==temp.length()-1){
                        cout << "Case #" << i+1 << ": " << temp << endl;
                        break;
                    }
                    if(k==0)
                        cout << "Case #" <<i+1 << ": " <<"IMPOSSIBLE";
                    }
                }
            }
return 0;
}
