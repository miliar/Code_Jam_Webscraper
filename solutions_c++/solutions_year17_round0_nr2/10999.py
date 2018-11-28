#include <iostream>

using namespace std;
int dl(int a){
    if(a>=1&&a<10)return 1;
    if(a>=10&&a<100)return 2;
    if(a>=100&&a<1000)return 3;
    if(a=1000)return 4;

}
int f(int a){
    int x=dl(a),k=0;
    int tab[x-1];
    int b;
    b=a;
    while(a>0){
    b=a;
    for(int i=x-1;i>=0;i--){
        tab[i]=b%10;
        b=b/10;
    }
    for(int i=0;i<x-1;i++){
        if(tab[i]<=tab[i+1]){
        k++;
        }
        else break;
    }
    if(k==x-1)return a;
    k=0;
    a--;
    }

}

int main()
{
    int a, b, i, j;
    cin>>a;
    int start[a],stop[a];
    for(i=0;i<a;i++){
        cin>>b;
        start[i]=b;
    }
    for(i=0;i<a;i++)
    cout<<"Case #"<<i+1<<": "<<f(start[i])<<endl;



    return 0;
}
