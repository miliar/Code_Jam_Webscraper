#include<iostream>
#include<math.h>
using namespace std;

int main()
{
	int t, n[10000], k[10000], stalls[10000];
	int a,b, gap, fa, fb, ls, rs, pos, v, maxno, minno;
	
	cin >> t;
	for(int i=0; i<t; i++)
	{
		cin >> n[i] >> k[i];
	}
    
	for(int i=0; i<t; i++)
	{	
		ls=0; rs=0;
		for(int ll=0; ll<n[i]+10; ll++) stalls[ll]=0;
		stalls[0]=1;
		stalls[n[i]+1]=1;
		a=0;
		b=n[i]+1;
		gap=b-a-1;
		fa=a; 
		fb=b;

		for(int z=0; z<k[i]; z++)
		{
			a=0;
			b=n[i]+1;
			gap=0;
			fa=a; 
			fb=b;
			for(int p=b; p>=a; p--)
			{
				if(stalls[p]==1)
				{
					for(int q=p-1; q>=a; q--)
					{	if(stalls[q]==1) 
						{
							if((p-q-1)>=gap && (p-q-1)>0)
							{
								gap=p-q-1 ;
								fa=q;
								fb=p;
								break;
							}
							break;
						}
					}
				}
			}
			if((fa+fb)%2==0){
			 	stalls[(fa+fb+1)/2]=1;
			 	pos = (fa+fb+1)/2;
			}
			else {
				stalls[(fa+fb)/2]=1;
				pos = (fa+fb)/2;
			} 
		}
		v=pos-1;
		while(stalls[v--]!=1){ 
			ls++;
		}
		v=pos+1;
		while(stalls[v++]!=1){ 
			rs++;
		}
		maxno = int(max(ls,rs));
		minno = int(min(rs,ls));
		cout << "Case #" << i+1 << ": "  << maxno << " " << minno << endl;
	}
	return 0;
}