#include<bits/stdc++.h>
using namespace std;
ifstream fin("C:\\Users\\Vamseedhar\\Downloads\\B-small-attempt0.in");
ofstream fout("C:\\Users\\Vamseedhar\\Downloads\\counting sheep1.txt");
long long tidy1(long long n){
    vector<long long >v;
    long long k=n,m;
while(k!=0){
    m=k%10;
    v.push_back(m);
    k=k/10;
}
int k1=v.size();
for(int i=0;i<k1-1;i++){
    if(v[i+1]>v[i]){
         //cout<<v[i]<<endl;
        return 1;
        break;
    }
}
return 2;
}
int main(){
int t;
fin>>t;
for(int i=1;i<=t;i++){
    long long n;
    fin>>n;
    if(n>=0&&n<=9){
        fout<<"Case #"<<i<<": "<<n<<endl;
}
else{
        long long k1=tidy1(n);
        while(k1>0){
        long long k=n,le;
        if(k1==2){
    fout<<"Case #"<<i<<": "<<n<<endl;
    break;
        }
    else{
            n=n-1;
        k1=tidy1(n);
    }
}
}
}
}
