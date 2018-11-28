#include<iostream>

using namespace std;


int main()
{
    int t,n,k,p,x,y,z;
    cin>>t;
     p=1;
    while(t--)
    {
        cin>>n>>k;
        int slots[n+2]={0};
        slots[0]=slots[n+1]=1;
        int arr[n+2][2];
        
        
    for(int h=0;h<k;h++)
    {
        int min[n],max[n];
        
        int cnt=0;
       for(int i=1;i<n+1;i++)
       {
           if(slots[i-1]==0)
            {
                cnt++;
                arr[i][0]=cnt;
            }
            
            else
            {
                cnt=0;
                arr[i][0]=cnt;
            }
            
       }
        cnt=0;
         for(int i=n;i>0;i--)
       {
           if(slots[i+1]==0)
            {
                cnt++;
                arr[i][1]=cnt;
            }
            
            else
            {
                cnt=0;
                arr[i][1]=cnt;
            }
            
       }
       int i;
       int j=0;
       int m=-1;



       for(i=1;i<n+1;i++)
{
            min[i-1]=arr[i][0]<=arr[i][1]?arr[i][0]:arr[i][1];
	   max[i-1]=arr[i][0]>arr[i][1]?arr[i][0]:arr[i][1];			
		
}


for(i=1;i<n+1;i++)
{
	if(m<min[i-1] && slots[i]!=1)
		m=min[i-1];
}

j=0;
int min_arr[n];
for(i=1;i<n+1;i++)
{	
	if(m==min[i-1] && slots[i]!=1)
		min_arr[j++]=i;
}



if(j==1)
{
	slots[min_arr[0]]=1;
	y=max[min_arr[0]-1];	
	z=min[min_arr[0]-1];
}

else
{
	m=-1;
	int r=0;
	for(i=0;i<j;i++)
	{
		int u=min_arr[i];
		if(m<max[u-1] && slots[u]!=1)
		{
			m=max[u-1];
			r=u;	
		}

	}
	
	y=m;
	slots[r]=1;
	y=max[r-1];	
	z=min[r-1];
}




}
    
    cout<<"Case #"<<p<<": "<<y<<" "<<z<<endl;
    
    p++;
    }
    
    return 0;
}
