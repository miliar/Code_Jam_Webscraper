#include<bits/stdc++.h>
using namespace std;
ifstream fin("C:\\Users\\Vamseedhar\\Downloads\\C-small-1-attempt2.in");
ofstream fout("C:\\Users\\Vamseedhar\\Downloads\\counting sheep1.txt");
vector<long long >v;
long long stall(long long n,long long a[]){
if(n%2==0){
    v.push_back(n/2);
    a[n/2]++;
    v.push_back((n/2)-1);
    a[(n/2)-1]++;
}
else{
    v.push_back(n/2);
    a[n/2]++;
    v.push_back(n/2);
    a[n/2]++;
}

long x=v.size();
sort(v.begin(),v.end());
for(int i=x-1;i>=0;i--){
        //fout<<"elements are"<<v[i]<<endl;
        if(a[v[i]]>0){
            a[v[i]]--;
return v[i];
break;
        }
}
}

int main(){
int t;
fin>>t;
for(int i=1;i<=t;i++){
        v.clear();
        long long n,k,k1=0;
    fin>>n>>k;
    long long a[n+1];
    for(int j=0;j<=n;j++){
        a[j]=0;
    }
   if(n==k){
    fout<<"Case #"<<i<<": "<<"0 "<<"0"<<endl;
   }
   else{
    while(k1!=k-1){
            n=stall(n,a);
           k1++;
    }
    long long y=n;
    if(y==0){
        fout<<"Case #"<<i<<": "<<"0 "<<"0"<<endl;
    }
    else if(y%2==0&&y!=0){
       fout<<"Case #"<<i<<": "<<(y/2)<<" "<<(y/2)-1<<endl;
    }
    else{
        fout<<"Case #"<<i<<": "<<(y/2)<<" "<<(y/2)<<endl;
    }
   }
}
}
