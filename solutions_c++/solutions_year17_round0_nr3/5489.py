#include <iostream>
using namespace std;

void boundfind(int arr[],int size,int &lb,int &ub)
{
	int tlb,tub;
	 int i=0;
	 for( i=0;i<size;i++)
	 {
	 	if(arr[i]==0)
	 	{
	 		tlb=i;
	 		tub=i;
	 		break;
	 	}
	 }

   lb=i;ub=i;

   for(int j=i+1;j<size;j++)
   {
          //  cout<<"j:"<<j<<" tub:"<<tub<<" tlb: "<<tlb<<" ub: "<<ub<<" lb: "<<lb<<endl;
   	     if(arr[j]==0)
   	     {

              tub++;
          
              if(tub-tlb > ub - lb)
              {
              	ub=tub;
              	lb=tlb;
              }
              if(tub==size)
              {
              	tub=size-1;
              }
   	     }
   	     else
   	     {
   	       if(j+1<size)
   	       {
   	       	tlb=j+1;
   	       	tub=j+1;
   	       }
   	     }
   }
}

void minfun(int arr[],int location,int size,int &lmin,int & umin)
{
	    lmin=0;
      for(int i=location-1;i>0;i--)
      {
            if(arr[i]==0)
            {
            	lmin++;
            }
            else{
            	break;
            }
      }

       umin=0;
      for(int i=location+1;i<size-1;i++)
      {
      	if(arr[i]==0)
      	{
      		umin++;

      	}
      	else
      	{
      		break;
      	}
      }

     
}

int main(int argc, char const *argv[])
{
	int testcases;
    cin>>testcases;
         int i=0;
    while(testcases--)
    {
       int n,m;
       cin>>n>>m;
       int arr[n+2];
       arr[0]=1; arr[n+1]=1;

       for(int j=1;j<n+1;j++)
       {
       	arr[j]=0;
       }
         int location=0;

      while(m--)
      {
      	  int lb=0,ub=0;
      	  boundfind(arr,n+2,lb,ub);
      	  location=(lb+ub)/2;
      	  arr[location]=1;
      }
   
  //     for(int tu=0;tu<n+2;tu++)
  //     {
  //     	cout<<arr[tu]<<" ";
  //     }
  // cout<<endl;
      int min=0;
      int max=0;
      minfun(arr,location,n+2,min,max);
      if(max<min)
      {
             int t=min;
             min=max;
             max=t;
      }

    cout<<"Case #"<<i<<": "<<max<<" "<<min<<endl;


    i++;
    }
	return 0;
}