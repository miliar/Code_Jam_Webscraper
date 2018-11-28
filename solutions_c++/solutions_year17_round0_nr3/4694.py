
#include <iostream>
using namespace std ;

int main ()
{
    long n,x,y,i,j,flag,l,k,t,w,num,q;
    char str[1005];
    cin>>t;
    for(q=1;q<=t;q++){
    	 cin>>n>>k;
         w=k;
         l=-1;
			while(w>0)
			{
				l++;
				w=w>>1;
			}
            num=1;

			for(i=0;i<l;i++)
			num=num<<1;

			long a,b;

			if((n&1)!=0)
			a=(n>>1);
			else
			a=(n-1)>>1;

			b=n>>1;


			long c,d;
			c=d=1;


			for(long i=1;i<l;i++)
			{

				if(((a&1)!=0) && ((b&1)==0))
				c=(c<<1)+d;
				else if (((a&1)==0)&& ((b&1)!=0))
				d=(d<<1)+c;
				else
				{
					c=c<<1;
					d=d<<1;
				}
				a=(a-1)>>1;
				b=b>>1;
			}
        if(k==1)
                cout<<"Case #"<<q<<": "<<b<<" "<<a<<endl;


        else if(k<(num+d))
			{
				cout<<"Case #"<<q<<": "<<b/2<<" "<<(b-1)/2<<endl;
			}
			else
			{
				cout<<"Case #"<<q<<": "<<a/2<<" "<<(a-1)/2<<endl;
			}


    }

}
