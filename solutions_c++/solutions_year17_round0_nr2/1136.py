#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;

int main(){
    int t;
    ifstream in("B-large.in");
    ofstream out("out.txt");
    in>>t;
    char n[20];
    for(int it=0;it<t;it++){
        in>>n;
        int len=strlen(n);
        bool ar[len];
        ar[len-1]=true;
        for(int i=len-2;i>=0;i--){
            if(n[i]==n[i+1])
                ar[i]=ar[i+1];
            else if(n[i]>n[i+1])
                ar[i]=false;
            else
                ar[i]=true;
        }
        for(int i=0;i<len;i++){
            if(!ar[i]){
                n[i++]--;
                for(;i<len;i++)
                    n[i]='9';
            }
        }
        if(n[0]=='0'){
            out<<"Case #"<<it+1<<": "<<n+1<<endl;
        }else{
            out<<"Case #"<<it+1<<": "<<n<<endl;
        }
    }
}
