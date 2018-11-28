#include<bits/stdc++.h>
using namespace std;
int a[6];
char s[7]="ROYGBV";
int ans[1050];
int main()
{
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		int n;
		cin>>n;
		int tag=0;
		for(int i=0;i<6;i++){
			cin>>a[i];
			if(a[i]>a[tag])tag=i;
		}
		int tmp=tag;
		bool ok=true;
		ans[1]=tag;
		a[tag]--;
		for(int i=2;i<=n;i++){
			int f=(tmp+2)%6;
			for(int j=2;j<=4;j++){
				if(a[(tmp+j)%6]>a[f]||(a[(tmp+j)%6]==a[f]&&(tmp+j)%6==ans[1]))f=(tmp+j)%6;
			}
			if(a[f]==0){
				ok=false;
				break;
			}
			tmp=f;
			a[f]--;
			ans[i]=f;
		}
		bool ff=false;
		for(int i=2;i<=4;i++){
			if((ans[1]+i)%6==ans[n])ff=true;
		}
		if(!ff)ok=false;
		printf("Case #%d: ", tt);
		if(!ok)printf("IMPOSSIBLE\n");
		else {
			for(int i=1;i<=n;i++){
				printf("%c", s[ans[i]]);
			}
			printf("\n");
		}
	}
}

