#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    unsigned long long int  test,x,y,t;
    bool set=true;
    fstream fin,fout;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
    cin>>test;
    
  
  for( int k=0;k<test;k++)
  {
  	cin>>x;
    for(int i=x; i>0; i=i-1)
    {
    	set=true;
    	    t=i;
    	  
    	while( t!=0 )
    	{
    		if(t<10)
    		 {
    		 	//cout<<i<<"\n";
				break;
    		 }
    		 else if( (t%10) >= ((t/10)%10) )
    		 {
    		 	t= t/10;
    		 //	cout<<i<<"\n";
    		 }
    		 else
    		 {
    		 	set=false;break;
    		 }
    	}
    	if(set)
    	 { 
		    cout<<"Case #"<<k+1<<":"<<" "<<i<<"\n"; break;
		 }
    	  
    }
 }
    	
		return 0;
}
