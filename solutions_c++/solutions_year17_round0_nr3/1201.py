#include<cstdio>
#include<algorithm>
#include<iostream>
#include<map>
#include<bitset>
using namespace std;
map<long long,long long>cnt;
int main()
{
	int T,cases=0;
	cin>>T;
	long long n,m;
	while(T--){
		cin>>n>>m;
		printf("Case #%d: ",++cases);
		cnt.clear();
		cnt[n]++;
		long long sum=0;
		while(!cnt.empty()){
			auto i=prev(cnt.end());
			if(sum+i->second>=m){ 
				cout<<(i->first)/2<<' '<<(i->first-1)/2<<endl;
				break;
			}
			sum+=i->second;
			cnt[i->first>>1]+=i->second;
			cnt[(i->first-1)>>1]+=i->second;
			cnt.erase(i);
			
		}
	}
}
