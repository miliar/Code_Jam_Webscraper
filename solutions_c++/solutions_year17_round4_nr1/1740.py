#include<bits/stdc++.h>
using namespace std;

int a[105],f[5];

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int cnt=0;
	
	while(T--)
	{
		cnt++;
		memset(f,0,sizeof(f));
		int n,p;
		scanf("%d%d",&n,&p);
		
		int i;
		
		for (i=1;i<=n;i++){
			scanf("%d",&a[i]);
		}
		
		for (i=1;i<=n;i++){
			a[i]=a[i]%p;
			f[a[i]]++;
		}
		
		printf("Case #%d: ",cnt);
		
		if(p==2)
		{
			int ans=f[0]+(f[1]+1)/2;
			cout<<ans<<endl;
			continue;
		}
		
		else if(p==3){
			
			int ans=f[0]+min(f[1],f[2]);
			int x=min(f[1],f[2]);
			
			f[1]-=x;
			f[2]-=x;
			
			ans+=(f[1]+2)/3+(f[2]+2)/3;
			
			cout<<ans<<endl;
		}
		
		else if(p==4){
			
				int ans=f[0];
				int x=min(f[1],f[3]);
				
				f[1]-=x;
				f[3]-=x;
				
				ans+=(x)+(f[1]+3)/4+(f[3]+3)/4;
				
				ans+=(f[2]+3)/4;
				cout<<ans<<endl;
		}
		
		
	}
}
