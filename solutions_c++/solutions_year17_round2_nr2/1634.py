#include<bits/stdc++.h>
using namespace std;

int t,n,cr,cb,cy,cg,cv,co;
char ans[1005];

int issafe(int nr,int ny,int nb)
{
	int tt=nr+ny+nb;
	tt=(tt+1)/2;
	if(nr>tt||ny>tt||nb>tt)
		return 0;
	return 1;
}

int main()
{
	int i,j,k;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		printf("Case #%d: ",j);
		k=0;
		cin>>n>>cr>>co>>cy>>cg>>cb>>cv;
		if(cr>n/2||cy>n/2||cb>n/2)
			cout<<"IMPOSSIBLE"<<endl;
		else
		{
			if(cr>0){
				ans[0]='R';
				cr--;
			}
			else if(cy>0){
				ans[0]='Y';
				cy--;
			}
			else{
				ans[0]='B';
				cb--;
			}
			for(i=1;i<n;i++)
			{
				if(ans[i-1]!='R'&&cr>0&&issafe(cr-1,cy,cb)){
					ans[i]='R';
					cr--;
				}
				else if(ans[i-1]!='Y'&&cy>0&&issafe(cr,cy-1,cb)){
					ans[i]='Y';
					cy--;
				}
				else if(ans[i-1]!='B'&&cb>0&&issafe(cr,cy,cb-1)){
					ans[i]='B';
					cb--;
				}
			}
			for(i=0;i<n;i++)
				cout<<ans[i];
			cout<<endl;
		}
	}
	return 0;
}
