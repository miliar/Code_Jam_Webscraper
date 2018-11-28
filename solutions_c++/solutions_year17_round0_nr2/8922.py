#include<iostream>
#include<stdio.h>

using namespace std;

struct ms {
int dig[20];
int digcount;

void countDigit(long long num){
    int i=0;
    while(num>0){
        dig[i]=num%10;
        num=num/10;
        i++;
    }
    digcount=i;
    }

void p(){
    for(int i=digcount-1; i>=0; i--)
    cout<<dig[i];
    cout<<"\n";
}
};

void findAnswer(ms tc){
int i;
for(i=tc.digcount-1; i>0; i--)
    if(tc.dig[i]>tc.dig[i-1])
        break;

for(int j=i-1;j>=0;j--) tc.dig[j]=9;

int t=i;
while(tc.dig[t]-1<tc.dig[t+1] && t<tc.digcount) {
    tc.dig[t] = 9 ;
    t++;
}
if(t+1==tc.digcount) tc.digcount--;
tc.dig[t] -= 1;

tc.p();
}

bool isdigitasc(long long num){
int prev=10,current;
while(num>0){
    current = num%10;
    //cout<<current<<" "<<prev<<" "<<num<<"\n"; //debug
    if(current>prev)
        return false;
    prev = current;
    num = num/10;
    }
return true;
}

int main(){

freopen("B-small-attempt0.in","r",stdin);
freopen("out1.txt","w",stdout);
int test;
long long num,i;
ms numo;
int testcount=1;
cin>>test;

while(test--){
    cin>>num;
    numo.countDigit(num);
    cout<<"Case #"<<testcount<<": ";
    if(num > 1000)
        findAnswer(numo);
    else {
        for(i=num;i>=0;i--){
        if(isdigitasc(i))
            break;
        }
        cout<<i<<"\n";
    }
    testcount++;
}
}
