#include <iostream>

using namespace std;

string s;
int k;
int steps_needed(){
    int result = 0;
    int nMinus = 0;
    for(int i = 0; i<s.size()-k+1; i++){
        if(s[i]=='-'){
            result++;
            for(int j = i; j<k+i; j++){
                s[j]= s[j]=='-'? '+':'-';

            }
        }
    }

    for(int i = 0; i<s.size(); i++){
        if(s[i]=='-')return -1;
    }
    return result;
}

int main(){

    int tt;
    cin>>tt;

    int temp;
    for(int i = 0; i<tt; i++){

        cin>>s>>k;
        temp = steps_needed();
        cout<<"Case #"<<(i+1)<<": ";
        if(temp<0){
            cout<<"IMPOSSIBLE"<<endl;
        }else{
            cout<<temp<<endl;
        }
    }

    return 0;
}
