#include<iostream>
#include<math.h>
#include<algorithm>
#define ull unsigned long long
using namespace std;
int main()
{
	int t;
	ull n,k,ans,L,R;
	cin>>t;
	for(int ii=1;ii<=t;ii++)
	{
		cin>>n>>k;
		int base=log2(k);
		ull a[2*k],b[2*k],*oldl,*newl,*temp;
		a[0]=n;
		oldl=a;newl=b;
	
		for(int i=0;i<base;i++)
		{
			for(int p=0,k=0;p<(int)pow(2,i);p++)
			{
				if(oldl[p]%2==0)
				{
					newl[k++]=oldl[p]/2;
					newl[k++]=(oldl[p]/2)-1;
				}
				else
				{
					newl[k++]=oldl[p]/2;
					newl[k++]=(oldl[p]/2);
				}
			}
			temp=newl;
			newl=oldl;
			oldl=temp;
		}
		sort(oldl,oldl+(int)pow(2,base));
		int p=pow(2,base),index=(p-1)-(k-p);
		//cout<<"\n p: "<<p<<" k: "<<k<<" index: "<<index;
		ans=oldl[index];//<<" "<<old[];
		if(ans%2==0)
		{
			L=ans/2;
			R=(ans/2==0?0:(ans/2) -1);
		}
		else
		{
			L=R=ans/2;
		}
		cout<<"Case #"<<ii<<": "<<L<<" "<<R<<endl;
	}
		
	
	return 0;
}
