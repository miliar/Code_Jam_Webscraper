#include <bits/stdc++.h>

#define sd(n) scanf("%d",&n)
#define sld(n) scanf("%lld",&n)

#define pd(n) printf("%d\n",n)
#define pld(n) printf("%lld\n",n)

#define test int t; sd(t);while(t--)
#define MAXI (int)1e6 + 1

typedef long long ll;


using namespace std;


int arr[6];

bool fun(int in){
	int sumi=0;
	for(int i=0;i<6;i++){
		if(i==in)continue;
		sumi+=arr[i];
	}

	if(sumi>=arr[in])return true;
	return false;

}

int solve(int x,int pref){
	int mn=0;
	if(x==0)mn=1;

	for(int i=0;i<6;i++){
		if(arr[i]>arr[mn] && i!=x)mn=i;
		if(arr[i]==arr[mn] && i==pref && i!=x)mn=i;
	}
	return mn;
}


int main(){
	freopen("B-small-attempt2.in","r",stdin);
	freopen("A2.out","w",stdout);
	int z=1;
	char A[6]={'R','O','Y','G','B','V'};
	test{
		if(z!=1)cout << endl;
		printf("Case #%d: ",z++);
		int n;sd(n);
		for(int i=0;i<6;i++){
			cin >> arr[i];
		}

		int flag=1;

		for(int i=0;i<6;i++){
			if(!fun(i)){
				flag=0;
				cout << "IMPOSSIBLE";
				break;
			}
		}
		int x1=-1,x2=-1;
		if(flag){
			int prev=-1;
			for(int i=0;i<n;i++){
				int y=solve(prev,x1);
				if(prev==-1)x1=y;
				arr[y]--;
				cout << A[y];
				prev=y;
				//if(i==n-1)x2=y;
			}
			//if(x1==x2)cout << "\nI am nohindwkdmnslndnhosjdpskc";
		}
	//	cout << endl;
	}
}
