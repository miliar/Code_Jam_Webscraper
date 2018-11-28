#include<iostream>
using namespace std;

int a[1001],b[1001];

long long int power(long long int index)
{
	long long int value=1;
	for(long long int i=0;i<index;i++)
		value*=10;
	return value;
}

int main(){
	//freopen("B-small.in","r",stdin);
	//freopen("B-out.txt","w",stdout);
	long long int c,cc,t=0,i,ans,k,j,ind=0,sm=0;
	bool indi=false;
	
	scanf("%lld",&cc);

	for(c=1 ; c<=cc ; c++){
		scanf("%lld",&t);
		ans=t;
		k=t%10;
		while(t/10!=0)
		{	ind++;
			k=t%10;
			i=(t/10)%10;
			if(i<k) t=t/10;
			else {
				if(i>k) indi=true;
				sm=ind;
				t=t/10;
			}
			
		}
		
		j=power(sm);
		//cout<<j<<endl;
		if(ans/10!=0 and indi)
		ans=(ans/j-1)*j+j-1;
		cout << "Case #" << c << ": " << ans << endl;
		ind=0;
		sm=0;
		indi=false;
		
		}
		
		return 1;
	}

