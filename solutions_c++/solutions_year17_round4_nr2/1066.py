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
int N,a[1005][2];
int main()
{
	int t,i,j,k,cs,css;
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		cin>>N>>t>>k;
		for(i=0;i<=1000;i++)a[i][0]=a[i][1]=0;
		for(i=0;i<k;i++) {
			cin>>t>>j;
			a[t-1][j-1]++;
		}
		cout<<"Case #"<<cs<<": ";
		int an1=0,an2=0;
		for(i=0;i<N;i++) {
			while(a[i][0]+a[i][1]>0) {
				if(a[i][0]>=a[i][1]) k=1;
				else k=0;
				int m=-1;
				for(j=i+1;j<N;j++) {
					if(a[j][k]==0)continue;
					if(m==-1)m=j;
					if(a[j][1-k]>a[m][1-k])m=j;
					if(a[j][1-k]==a[m][1-k] && a[j][k]>a[m][k])m=j;
				}
				if(m==-1) {
					if(i>0 && a[i][k]>0) {
						a[i][k]--;
						an2++;
					}
				} else {
					a[m][k]--;
				}
				a[i][1-k]--;
				an1++;
			}
		}
		cout<<an1<<" "<<an2<<endl;
	}
	return 0;
}
