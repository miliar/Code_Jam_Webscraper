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
int gt(int c1,int c2,int p) {
	int an=0;
	if(c1>=c2) {
		an+=c2;
		c1-=c2;
	} else {
		an+=c1;
		c2-=c1;
		c1=c2;
	}
	if(c1%p==0)an+=(c1-c1/p);
	else an+=(c1-c1/p-1);
	return an;
}
int main()
{
	int t,i,j,k,cs,css;
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		int N,P;
		int a[10];
		cin>>N>>P;
		a[0]=a[1]=a[2]=a[3]=0;
		for(i=0;i<N;i++) {
			cin>>t;
			a[t%P]++;
		}
		cout<<"Case #"<<cs<<": ";
		if(P==2) {
			k=a[1]/2;
			cout<<N-k<<endl;
			continue;
		}
		if(P==3) {
			k=0;
			if(a[1]>=a[2]) {
				k=a[2];
				a[1]-=a[2];
				if(a[1]%3 == 0)k+=(a[1]-a[1]/3);
				else k+=(a[1]-a[1]/3-1);
			} else {
				k=a[1];
				a[2]-=a[1];
				a[1]=a[2];
				if(a[1]%3 == 0)k+=(a[1]-a[1]/3);
				else k+=(a[1]-a[1]/3-1);
			}
			cout<<N-k<<endl;
			continue;
		}
		if(P==4) {
			k=0;
			if(a[2]%2==0) {
				k+=a[2]/2;
				a[2]=0;
				if(a[1]>=a[3]) {
					k+=a[3];
					a[1]-=a[3];
				} else {
					k+=a[1];
					a[3]-=a[1];
					a[1]=a[3];
				}
				if(a[1]%4 == 0)k+=(a[1]-a[1]/4);
				else k+=(a[1]-a[1]/4-1);				
			} else {
				k+=a[2]/2;
				a[2]=1;
				if(a[1]>=a[3]) {
					if(a[1]==0) {
						cout<<N-k<<endl;
						continue;
					}
					if(a[1]==1) {
						k+=a[1]+a[3];
						cout<<N-k<<endl;
						continue;
					}
					a[1]-=2;
					k+=gt(a[1],a[3],4);
					cout<<N-k<<endl;
					continue;
				}
				if(a[3]==1) {
					k++;
					cout<<N-k<<endl;
					continue;
				}
				a[3]-=2;
				k+=gt(a[1],a[3],4);
				cout<<N-k<<endl;
				continue;
			}
		}
	}
	return 0;
}
