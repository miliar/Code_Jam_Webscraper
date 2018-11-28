#include<iostream>
#include<cstdio>
#include<string>
#include<sstream>
using namespace std;
string tidy_number(const string &str){
    int len = str.length();
    ostringstream sout;
    bool changed = false;
    bool print_9 = false;
    for(int i=1;i<len;i++){
        if(print_9){
            sout<<9;
            continue;
        }
        if(str[i] < str[i-1]){
            changed = true;
            if(i==1){
                if(str[i-1] =='1'){
                    sout<<9;
                    print_9 = true;
                }
                else{
                    sout<<char(str[i-1]-1);
                    sout<<9;
                    print_9 = true;
                }
            }
            else{
                if(str[i-1] == '0'){
                    for(int j = i-2; j>=0;j--){
                        if(str[j] > '0'){
                            for(int k = 0 ;k < j ; k++)sout<<str[k];
                            if(char(str[j] - 1) != '0' || j == 0) sout<<char(str[j] - 1);
                            for(int k=j+1; k<=i-2 ; k++)sout<<9;
                            break;
                        }
                    }
                    sout<<9;
                    sout<<9;
                    print_9 = true;
                }
                else{
                    for(int j = 0 ;j < i-1;j++)sout<<str[j];
                    sout<<char(str[i-1]-1);
                    sout<<9;
                    print_9 = true;
                }
            }
        }
    }
    return changed ? tidy_number(sout.str()) : str;
}
int main(){
    int cas,q;
    freopen("B-large.in","r",stdin);
    freopen("Bout.txt","w",stdout);
    cin>>cas;
    for(int q=1;q<=cas;q++){
        string str;
        cin>>str;
        str = tidy_number(str);
        cout<<"Case #"<<q<<": "<<str<<endl;
    }
    return 0;
}
