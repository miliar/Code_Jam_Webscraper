#include<iostream>
#include<string>
#include<vector>
#include<math.h>
using namespace std;
void calc(unsigned long long n,unsigned long long a[], unsigned long long b[])
{
        for(unsigned long long i=1;i<=log2(n);i++){
            if(a[i-1]%2==0){
                b[i]=0;
                b[i]+=b[i-1];
                a[i]=(a[i-1]/2)-1;
            }
            else if(a[i-1]%2!=0){
               
                b[i]=2*b[i-1]+pow(2,i-1)-b[i-1];
                a[i]=(a[i-1]/2);
            }
        }
}
int main(){
    int t;
    cin>>t;
    for(int l=1;l<=t;l++){
        unsigned  long long n,k,m,r;
        cin>>n;
        cin>>k;
        unsigned long long a[(unsigned long long)log2(n)+1],b[(unsigned long long)log2(n)+1];
        a[0]=n;
        b[0]=1;
        calc(n,a,b);
        m=(unsigned long long )log2(k);
        if(m!=0){
            k=k-(unsigned long long )pow(2,m);
        }
        if(k<pow(2,m)-b[m]){
            r=a[m]+1;
            cout<<"Case #"<<l<<": "<<r/2<<" "<<(r-1)/2<<"\n";
        }
        else{
            r=a[m];
            cout<<"Case #"<<l<<": "<<r/2<<" "<<(r-1)/2<<"\n";
        }
    }
    return 0;
}
