#include <iostream>
#include <math.h>
#include<fstream>

using namespace std;
long long N;

long long Max=0;

void rec(long long a){
if(a>Max)Max=a;
if(pow(10,floor(log10(N))-floor(log10(a)))*a<Max){
    int checkup_val=a;
    for(int x=floor(log10(a));x<floor(log10(N));x++){
        a*=10;
        a+=9;
    }
    //+9*pow(10,floor(log10(N))-floor(log10(a))-1)
    if(Max>checkup_val)return;



}
//cout<<a<<endl;
int ret=-1;
for(int x=9;x>=a%10;x--){
    if(a*10+x<=N){
        rec(a*10+x);
     //   if(ret!=-1 ){return ret;}
    }
}
//if(ret<a)ret=a;

}

void recs(){
    int ret;
for(int x=9;x>=1;x--){
    if(x<=N)rec(x);
    //if(ret!=-1){return ret;}
}
//return ret;
}

int main()
{
int T;
cin>>T;
ofstream fout("out.txt");
for(int i=0;i<T;i++){

    cin>>N;
    Max=0;
  recs();
    fout<<"Case #"<<i+1<<": "<<Max<<endl;
}
}
