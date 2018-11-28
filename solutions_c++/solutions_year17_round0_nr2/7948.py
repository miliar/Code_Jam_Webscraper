#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int main(){
long long int T,N,X,temp,j,tx,V;
int arr[18];

ifstream f1("input.in”);
ofstream f2("output.out”);
f1>>T;
V=T;
while(T--){
        f1>>N;
        X=N;
vector<int> v;
while(X>0){
    v.push_back(X%10);
    X/=10;
}
for(int i=0;i<v.size();i++){
    if((i+1)<v.size()&&v[i]<v[i+1]){
        v[i]=9;
        v[i+1]--;
    }
}
f2<<"Case #"<<V-T<<": ";
for(int i=v.size()-1;i>=0;i--){
        if(v[i])
       f2<<v[i];
        if(v[i]==9){

if(i-1>=0)
    v[i-1]=9;
        }
}
f2<<endl;
}
}