#include<iostream>
#include<fstream>
using namespace std;
int main(){

int num,a[10],count=0,c,i=0,b=0,t1=0,l=0,j=0;
ifstream in("B-small-attempt1 .in");
ofstream out("output.txt");
in>>t1;
if(t1<0||t1>100){
    t1=100;
}
for(j=1,i=0,l=0;l<t1;l++,j++,i++){
out<<"Case #"<<j<<": ";
in>>num;
b=num;
while(num!=0){
a[i]=num%10;
num=num/10;
i++;
}
i--;
c=i;
for(i=0;i+1<=c;i++)
{
if(a[i]>=a[i+1]){}
else{count++;}
}
if(count==0){
    for(i=c;i>=0;i--){
        out<<a[i];
    }
    out<<endl;
}
else if(count>0){

    while(count!=0){
        num=num+b;
        num=num-1;
    b--;
            count=0,i=0;
        while(num!=0){
a[i]=num%10;
num=num/10;
i++;
}
i--;
c=i;
for(i=0;i+1<=c;i++)
{
if(a[i]>=a[i+1]){}
else{count++;}
}
if(count==0){
    for(i=c;i>=0;i--){
        out<<a[i];
    }
out<<endl;
    }

}
}
}
return 0;
}
