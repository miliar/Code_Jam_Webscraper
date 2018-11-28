#include<bits/stdc++.h>
using namespace std;

bool test(int a){
    int l=9;
    while(a){
        if((a%10)>l)return false;
        l=a%10;
        a/=10;
    }
    return true;
}
int main(){

    ifstream myReadFile;
    myReadFile.open("input.in");
    ofstream myfile;
    myfile.open ("output.out");
    int t;
    myReadFile>>t;
    int c=1;

    while(t--){
        string  N;
        myReadFile>>N;
        for(int i=0;i<N.size()-1;i++){
            if(N[i]>N[i+1]){
                N[i]=N[i]-1;
                for(int j=i+1;j<N.size();j++){
                    N[j]='9';
                }
                for(int j=i;j>0;j--){
                    if(N[j]<N[j-1]){
                        N[j]='9';
                        N[j-1]=N[j-1]-1;
                    }else{
                        break;
                    }
                }
                break;
            }
        }
        myfile<<"Case #"<<c<<": ";
        bool f=true;
        for(int i=0;i<N.size();i++){
            if((N[i]=='0')&&f)continue;
            if(N[i]!='0')f=false;
            myfile<<N[i];
        }
        myfile<<endl;
        c++;
    }
    return 0;
}
