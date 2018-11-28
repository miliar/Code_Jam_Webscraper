#include<iostream>
#include<string>
using namespace std;
#define ll long long int
void print(int arr[],int n)
{
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
int main()
{
	ll a,temp;
	int n,t,i,j;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
	    cout<<"Case #"<<tc<<": ";
	    cin>>a;
	    temp=a;
	    ll s[20],ind=0;
    	while(a)
        {
            s[ind++]=a%10;
            a/=10;
        }
        for(i=0;i<ind/2;i++)
            s[i]=s[ind-i-1]+s[i]-(s[ind-i-1]=s[i]);
//        print(s,ind);
        n=ind;
	    for(i=0;i<n-1;i++)
	    {
	        if(s[i]>s[i+1])
	            break;
	    }
//	    cout<<i<<endl;
	    if(i==n-1)
	    {
	        cout<<temp<<endl;
	    }
	    else
	    {
	        for(j=i;j>=1 && s[j]==s[j-1];j--);
	        s[j]=s[j]-1;
	        for(i=j+1;i<n;i++)
	            s[i]=9;
	         
	        for(i=0;i<n/2;i++)
                s[i]=s[ind-i-1]+s[i]-(s[ind-i-1]=s[i]);
  //          print(s,n); 
            a=0;
            ll dec=1;
            for(i=0;i<n;i++)
            {
                a+=s[i]*dec;
                dec*=10;
            }
            cout<<a<<endl;
	    }
	   
	}
	return 0;
}