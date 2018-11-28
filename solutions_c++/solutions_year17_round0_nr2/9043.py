#include <bits/stdc++.h>
using namespace std;

int main() {
	long long int n,bn,ans;
	vector<int> num;
	
	int t,nod;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		
		cin>>n;
		nod=0;
		bn=0;
		bn=n;
		//cout<<"\n"<<n<<"\n";
		/*for(int i=0;i<20;i++)
			num[i]=0;*/
		num.clear();
		while(bn)
		{
			num.push_back(bn%10);
			nod++;
			bn/=10;
		}
		reverse(num.begin(),num.end());
		/*for(vector <int>::iterator it=num.begin();it!=num.end();it++)
		cout<<*it<<" ";*/
		for(int i=0;i<nod-1;i++)
		{
			if(num[i]>num[i+1])
			{
				num[i]=num[i]-1;
				for(int j=i+1;j<nod;j++)
					num[j]=9;
				i=-1;
			}
			
			
		}
		reverse(num.begin(),num.end());
		ans=0;
		for(int i=nod-1;i>=0;i--)
		{
			ans=ans*10 + num[i];
		}
		cout<<"Case #"<<test<<": "<<ans<<"\n";
		
		
	}
	return 0;
}