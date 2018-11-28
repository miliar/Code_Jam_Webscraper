#include <bits/stdc++.h>
using namespace std;

#define sd(a) scanf("%d",&a)
#define ss(a) scanf("%s",a)
#define sl(a) scanf("%lld",&a)
#define clr(a) memset(a,0,sizeof(a))
#define debug(a) printf("check%d\n",a)
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define ll long long
#define MAX 100005
#define mod 1000000007

int main() {
	
	int t;
//	
//		freopen("input.txt", "r", stdin);
//		freopen("output.txt", "w", stdout);

	
	sd(t);
	ll x,y,start,i,j,k,l,m,n,temp,count;
	int kk = 0;
	while(t--){
		kk++;
		cout<<"Case #"<<kk<<": ";
		sl(n);
		sl(k);
		
		
		if(k==n){
			x = 0;
			y = 0;
			cout<<x<<" "<<y<<endl;
			continue;
		}
		
		if(n==2){
			x = 1;
			y = 0;
			cout<<x<<" "<<y<<endl;
			continue;
		}
		
		if(n==3){
			if(k==1){
				x=1;
				y=1;
			}
			else{
				x = 0;
				y = 0;
			}
			
			cout<<x<<" "<<y<<endl;
			continue;
		}
		
		
		k--;
		
		ll minn,maxx;
		
		if(n%2==1){
			maxx = (n-1)/2;
			minn = maxx;
		}
		
		else{
			maxx = n/2;
			minn = maxx-1;
		}
		
		ll minCount=1,maxCount=1;
		
		while(k>0){
			
			if(maxx==1){
				maxx = 0;
				minn = 0;
				break;
			}
			
			if(minn==maxx){
				
				if(minn==1){
					minn = 0;
					maxx = 0;
					break;
				}
					
				if(maxx%2==1){
					minn = maxx/2;
					maxx = minn;
				}
				else{
					maxx = maxx/2;
					minn = maxx-1;
				}
				
				k-=minCount;
				k-=maxCount;
				minCount*=2;
				maxCount*=2;
			}
			
			else{
				
				if(k<=maxCount){
					
					if(maxx%2==1){
						minn = maxx/2;
						maxx = minn;
					}
					else{
						maxx = maxx/2;
						minn = maxx-1;
					}
					
					break;
				}
				else if(k<=(maxCount+minCount)){
					
					if(minn%2==1){
						minn = minn/2;
						maxx = minn;
					}
					else{
						maxx = minn/2;
						minn = maxx-1;
					}
					break;
				}
				
				else{
					k-=minCount;
					k-=maxCount;
					
					if(maxx%2==0){
						maxx = maxx/2;
						minn = minn/2;
						minCount*=2;
						minCount+=maxCount;
					}
					else{
						maxx = maxx/2;
						minn = maxx-1;
						
						maxCount*=2;
						maxCount+=minCount;	
					}
					
				}
					
			}
			
		
		}
		
		cout<<maxx<<" "<<minn<<endl;
		
	}
	
	
	
	return 0;
}
