#include<iostream>
#include<fstream>
using namespace std;
void makeArr(long long int i,int arr[],int &size){
    while(i>0){
        arr[size++] = i%10;
        i=i/10;
    }
    int j=0,k=size-1;
    while(j<k){
        int t = arr[j];
        arr[j] = arr[k];
        arr[k] = t;
        j++;
        k--;
    }
}
long long int convert(int arr[],int size){
    long long int res=0,j=1;
    for(int i=size-1;i>=0;i--){
        res += arr[i]*j;
        j=j*10;
    }
    return res;
}
void getLast(int arr[],int &i){
    i--;
    while(i>0){
        if(arr[i] != arr[i-1])
        return;
        else
        i--;
    }
}
long long int getNo(long long int n){
    int arr[20],size=0,i;
    //long long int i,j=1;
    makeArr(n,arr,size);
    for(i=1;i<size;i++){
        if(arr[i]<arr[i-1]){
            getLast(arr,i);
            arr[i] -= 1;
            break;
        }
    }
    i++;
    while(i<size){
        arr[i] = 9;
        i++;
    }
    return convert(arr,size);
}
int main(){
    int t,i,k;
    long long int n;
    string str;
    ifstream ip;
    ofstream op;
    ip.open("B-large.in");
    op.open("op.txt");
    ip>>t;
    for(i=1;i<=t;i++){
        ip>>n;
        //cout<<k<<endl;
        op<<"Case #"<<i<<": "<<getNo(n)<<endl;
    }
    return 0;
}

