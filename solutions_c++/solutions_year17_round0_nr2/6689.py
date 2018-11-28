#include<bits/stdc++.h>
using namespace std;

int main(){
int T;
cin>>T;
for(int t=1;t<=T;t++){
long long int num;
cin>>num;
int count=0;
long long int n=num;
while(n!=0){
    n/=10;
    count++;
}
int arr[count];
for(int i=count-1;i>=0;i--){
    arr[i]=num%10;
    num/=10;
}
for(int i=count-1;i>0;i--){
    if(arr[i]<arr[i-1] ){
        arr[i-1]--;
        for(int x=i;x<count;x++)
            arr[x]=9;
    }
    }

cout<<"Case #"<<t<<":"<<" ";
if(arr[0]!=0){
    for(int i=0;i<count;i++)
        cout<<arr[i];
}
else{
    for(int i=1;i<count;i++)
        cout<<arr[i];
}
cout<<"\n";
}
return 0;
}

