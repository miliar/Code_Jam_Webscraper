#include <iostream>
#include <vector>
using namespace std;

int main() {
	int t;
	long long int n,y,x;
	cin>>t;int tt=0;
	while(t--)
	{
		cin>>n;y=n;tt++;
		vector<int> v;
		int c=0,d=100,flag=-1,p=-2;
		while(n)
		{

			if(d>=n%10){p=d;d=n%10;}
			else {flag=c+1;d=n%10;}
				n/=10;
				v.push_back(d);
			c++;
		}
		cout<<"Case #"<<tt<<": ";
		if(flag==-1)cout<<y<<endl;
		else{int temp=flag,ex=0,k=0;
		    v[temp-1]--;
		    int temp1=temp;
		    while(temp1<=c&&v[temp1-1]<v[temp1])
		    {
		    	v[temp1-1]=9;
		    	v[temp1]--;temp1++;
		    }
		    temp=temp1;
			while(temp<c&&v[temp-1]==0)
			{
				v[temp-1]=9;
				if(temp<c&&v[temp]>0)v[temp]--;temp++;ex=1;
			}
			if(ex==1)for(int i=0;i<flag;i++)v[i]=9;
			flag--;

			while(ex!=1&&flag>0)
			{

				 v[flag-1]=9;
				flag--;
			}

			while(v[c-1]==0)c--;
			for(int i=c-1;i>=0;i--)cout<<v[i];
			cout<<endl;
		}
	}
	return 0;
}
