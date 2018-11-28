#include <iostream>
#include<vector>
#include<limits.h>
#include<fstream>
#define MAX LONG_LONG_MAX
#include<map>

using namespace std;

map<pair<long,long>,pair<long,long> > mem;
//vector<vector<pair<long long,long long> > > mem;

pair<long long,long long> rec(long long n,long long k){
    //cout<<n<<k<<endl;
if(k==0)return {MAX,MAX};
if(k==1)return {(n-1)/2,n-1-(n-1)/2};
if(mem[{n,k}].first!=0){return mem[{n,k}];}
pair<long long,long long> ret1=rec((n-1)/2,(k-1)/2);
pair<long long,long long> ret2=rec(n-1-((n-1)/2),k-1-((k-1)/2));
mem[{n,k}]=min(ret1,ret2);
return min(ret1,ret2);
}

int main()
{
int T;
cin>>T;
ofstream fout("out.txt");
for(int i=0;i<T;i++){
long long N,K;
cin>>N>>K;
/*mem.clear();
mem.resize(N+1);
for(int x=0;x<N+1;x++)mem[x].resize(K+1,make_pair(-1,-1));*/
pair<long long,long long> a=rec(N,K);
fout<<"Case #"<<i+1<<": "<<a.second<<" "<<a.first<<endl;
}
}
