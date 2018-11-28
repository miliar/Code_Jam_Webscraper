#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
#define PB push_back
#define pii pair<int,int>
#define MP make_pair
#define sz size()
#define fi first
#define se second
using namespace std;
typedef long long ll;
int inRange(ll s, ll w, int t) {
//	cout<<s<<" "<<w<<" "<<t<<endl;
	w*=t;
	s*=100;
	if(w*90 <= s && s<=w*110)return 0;
	if(w*90 > s) return -1;
	return 1;
}
int main()
{
	int t,i,j,k,cs,css;
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		int N,P;
		ll W[100],S[100][100];
		int ctr[100];
		cin>>N>>P;
		for(i=0;i<N;i++)cin>>W[i];
		for(i=0;i<N;i++) {
			for(j=0;j<P;j++)cin>>S[i][j];
			sort(S[i],S[i]+P);
			ctr[i]=0;
		}
		int ans=0,ser=1;
		bool flag=false;
		while(1) {
			while(1) {
				bool ff=false;
				for(i=0;i<N;i++) {
					for(j=ctr[i];j<P;j++) {
						k=inRange(S[i][j],W[i],ser);
//						cout<<i<<" "<<j<<" "<<k<<endl;
						if(k<=-1)continue;
						if(k == 0)break;
						ff=true;
						ser++;
						j--;
					}				
					if(j>=P) {
						flag=true;
						break;
					}
					ctr[i]=j;
				}
				if(flag)break;
				if(!ff)break;
			}
			if(flag)break;
			ans++;
			for(i=0;i<N;i++)ctr[i]++;
		}
		cout<<"Case #"<<cs<<": "<<ans<<endl;
	}
	return 0;
}
