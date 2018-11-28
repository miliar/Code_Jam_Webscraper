#include<iostream>
#include<fstream>

using namespace std;

int main(){
    fstream fin("/Users/anupsing/Documents/CP/GCJ/QF/input.in");
    fstream fout("/Users/anupsing/Documents/CP/GCJ/QF/output.txt");
    int T;
    fin>>T;
    int cases=1;
    while(T--){
        string str;
        int k;
        fin>>str;
        fin>>k;
        int len=str.length();
        bool flag=true;
        int counter=0;
        for(int i=0;i<len;i++){
            if(str[i]=='-'){
                if(len-i<k){
                    flag =false;
                    break;
                }
                else {
                        counter++;
                    for(int j=i;j<i+k;j++){
                        if(str[j]=='+') str[j]='-';
                        else str[j]='+';
                    }
                }
            }
        }
        fout<<"Case #"<<cases<<": ";
        cases++;
        if(flag) fout<<counter<<endl;
        else fout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
