#include <iostream>
#include <fstream>
using namespace std;
int num(int no);
int numm(int n);
int tidy(int n,int first);
void di(int n,int arr[]);

int main(){

    int m[1000]={0},p=0,n[1000]={0};
    int fir[1000]={0};
    ifstream file;
    ofstream file_o;
    file.open("B-small-attempt1.in");
    while(!file.eof()){
        file>>m[p];
        p++;
    }
    if(m[0] == 0){
        return 0;
    }

    for(int y=0;y<m[0];y++){
        fir[y] = numm(m[y+1]);
    }
    for(int u=0; u<m[0]; u++){
        n[u] = tidy(m[u+1],fir[u]);
    }
    file_o.open ("output.txt");
    for(int i=0; i<100;i++){
        file_o<<"Case #"<<i+1<<": "<<n[i]<<endl;
    }
    file.close();
    file_o.close();
}

int num(int no){
    int a=0;
    while(no>0)
    {
    no=no/10;
    a++;
    }
    return a;
}
int numm(int n){
    while(n > 9){
     n /= 10;
    }
    return n;
}

void di(int n,int arr[]){
    int y=0;
    while (n > 0){
    int digit = n % 10;
    arr[y] = digit;
    n /= 10;
    y++;
    }
}

int tidy(int n,int first){
    int k=0,l=0;
    l = num(n);
    int counte = l-1;
    int dig[l]={0};
    for(int i=n;i>0;i--){
            di(i,dig);
            int flag=0;
            for(int j=0; j<counte;j++){
                if(dig[j] >= dig[j+1]){
                    flag = flag + 1;
                }
            }
            if(flag == counte){
                return i;
            }
    }

}
