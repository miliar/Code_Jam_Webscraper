#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("/Users/rishabh-pc/Downloads/B-large.in","r",stdin);
    freopen("/Users/rishabh-pc/Desktop/cjq2yes1.txt","w",stdout);
    int t;
    cin>>t;
    int tcc=1;
   /* while(t--){
    	int n;
    	cin>>n;
    	int ans=1;
    	int i,j;
    	for(i=1;i<=n;i++){
    	   int arr[20];
    	memset(arr,0,sizeof(arr));
    	int ii=19;
    	int temp=i;
    	while(i>0){
    		arr[ii]=i%10;
    		i/=10;
    		ii--;
		}
		for(j=0;j<19;j++)if(arr[j]>arr[j+1])break;
		if(j==19)ans=temp;
		i=temp;	
		}
		cout<<"Case #"<<tcc++<<": ";
		cout<<ans<<endl;
	}*/
    while(t--){
    	long long n;
    	cin>>n;
    	int arr[20];
    	memset(arr,0,sizeof(arr));
    	int i=19,j;
    	while(n>0){
    		arr[i]=n%10;
    		n/=10;
    		i--;
		}
		i++;
		for(i;i<19;i++){
			if(arr[i]>arr[i+1]){
				if(arr[i]==1 && arr[i+1]==0){
					for(j=0;j<20;j++)
					if(arr[j]==1)
					{
						arr[j]=0;
						break;
					}
					j++;
					for(;j<20;j++)
					arr[j]=9;
					break;
				}
				else{
					j=i-1;
					int tt=arr[i];
					while(j>=0 && arr[j]==tt)j--;
					j++;
					arr[j]--;
					j++;
					for(;j<20;j++){
						arr[j]=9;
					}
					break;
				}
			}
		}
		cout<<"Case #"<<tcc++<<": ";
		i=0;
		long long ans=0;
		while(arr[i]==0)i++;
		for(;i<20;i++)ans+=(long long)(arr[i]*pow(10,19-i));
		cout<<ans<<endl;
	}
    return 0;
}
