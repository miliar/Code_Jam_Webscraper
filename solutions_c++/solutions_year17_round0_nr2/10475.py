#include<iostream>
using namespace std;
int main()
{
	int T,i,c,x,y,z,q;
	cin>>T;
	int N[T];
	if(T>=1 && T<=100)
	{
	 for(i=1;i<=T;i++)
	 {
	 	cin>>N[i];
	 }	 
	 i=1;
 	 while((i<=T)&&(N[i]>=1 && N[i]<=1000))
	 {
	 	c=N[i];
	 	while(c>0)
	 	{
	 	z = c%10;
	 	q = c/10;
	 	y = q%10;
	 	x = q/10;
	 	if(x<=y && x<=z && y<=z)
	 	{
	 	cout<<"Case #"<<i<<": "<<c;
	 	cout<<"\n";
	 	break;
	 	}
	 	else
	 	{
	 		c--;
	 	}
	    }
	 
	 i++;
}
}
}
