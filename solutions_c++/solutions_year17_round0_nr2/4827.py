#include<bits/stdc++.h>
using namespace std;




int main()
{
		freopen("B-small-attempt0.in","r",stdin);
		freopen("B_small.out","w",stdout);
		int T,cas=0;
		scanf("%d",&T);
		while(T--){
			int N;
			cin>>N;
			//cout<<N<<endl;
			int ans=0;
			for(;N;N--){
				int n=N;
				//cout<<n<<endl;
				
				bool t=1;
				int last=n%10;
				n/=10;
				while(n){
					//cout<<last<<" ";
					if(last>=n%10){
						last=n%10;
						n/=10;
					} else {
						t=0;
						break;
					}
				}
				if(t){ans=N;break;}
			}
			
			printf("Case #%d: %d\n", ++cas, ans);
		}
		return 0;
}


