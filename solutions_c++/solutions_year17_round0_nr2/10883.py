#include <iostream>
using namespace std;

int main() {
int T,N,y,NN;
long int a[18];
a[0]=10;
int flag=0;
cin>>T;
for(int x=1;x<=T;x++)
{ xyzz:

	if(x==T+1)
	{return 0;}
	x++;
	

    cin>>N;
    if((N<1)||(N>1000))
    {
        return 0;
    }
    mnop:
    NN=N;
    for(y=1;y>0;y++)
    {   
        if(NN!=0)
        {
        a[y]=NN%10;
        NN=NN/10;
        
        if((a[y]<a[y-1]||a[y]==a[y-1])&&a[y]!=0)
        {
            flag=1;
        continue;
        }
        else
        {
        
         N--; 
         flag=0;
         goto mnop;   
        }
        }
        else
        {
            if(flag==1)
            {
                cout<<"Case #"<<x-1<<":"<<N<<endl;
                 goto xyzz;
                 	
            }
           
        }
    }

}
	return 0;
}
