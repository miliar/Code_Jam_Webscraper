#include <iostream>
#include <vector>
using namespace std;
int main() {
long long int q;
long long int yy;
int t,count=0;
cin>>t;
while(t--)
	{
cin>>q;
yy=q;
count++;
vector<int> vv;
	int c=0,d=100,r=-1,p=-2;
	while(q)
	{
 if(d>=q%10)
 {
 	p=d;
 	d=q%10;
 	}		else {				r=c+1;
		d=q%10;		}
		q/=10;
	vv.push_back(d);		
	c++;
		}
		cout<<"Case #"<<count<<": ";
	if(r==-1)
	cout<<yy<<endl;
		else
		{		
			int dd=r,e=0,k=0;
   vv[dd-1]--;
		    int dd1=dd;
  while(dd1 <= c && vv[dd1-1] < vv[dd1])
		 {
		   vv[dd1-1]=9;
		   
		    vv[dd1]--;
		   
		    dd1++;
		           }
		      dd=dd1;
	
		while(dd<c && vv[dd-1]==0)
			 {
			vv[dd-1]=9;
			    	if(dd<c && vv[dd]>0)
			{	
				vv[dd]--;
				dd++;
				e=1;
			}
			
			}
			if(e==1)
			
			for(int i=0;i<r;i++)
		{	
			vv[i]=9;}
			r--;
		
	         		while(e!=1 && r>0)
			{
 
			 vv[r-1]=9;
			r--;
	        		}
 
		while(vv[c-1]==0)
		{	c--; 
		}
		for(int i=c-1;i>=0;i--)
		{	
			cout<<vv[i];
}			
cout<<endl;
			
		}
	}
	return 0;
}