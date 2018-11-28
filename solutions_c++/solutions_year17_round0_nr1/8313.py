 #include<iostream>
#include<fstream>
using namespace std;
int main(){

int T=0,K=0;
string S;
ifstream iF ("‪inputer.in");
ofstream oF ("output7.txt");
iF>>T;
for(int i=0;i<T;i++){
int j=0, counter=0, ans=0;
iF>>S>>K;
while(K<=(S.length()-j)){
if(S[j]=='-'){
int b=j;
for(int l=0;l<K;l++){
if(S[b]=='-')
S[b]='+';
else
S[b]='-';
b++;
if(l==0)
counter++;
}
}
j++;
}
for(int a=0;a<S.size();a++){
if(S[a]=='+')
ans++;
}
oF<<"Case #"<<i+1<<": ";
if(ans==S.size())
oF<<counter;
else
oF<<"IMPOSSIBLE";
oF<<endl;
}
iF.close();
oF.close();
return 0;
}
