//If you are reading this then you are at wrong place.
#include<bits/stdc++.h>
#define mod 1000000007
using namespace std;
bool prime [1000001];
void debug(int a){cout<<a<<endl;}
int sieve(int a){memset(prime,true,sizeof(prime));int p,i;for(p=2;p*p<=a;p++){if(prime[p]==true){for(i=p*2;i<=a;i+=p)prime[i]=false;}}return 0;}
int main()
{
	//your code goes here
	//input for the testcase 
	ifstream cin("A-large.in");
	ofstream cout("AL.txt");	
	ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);	
	int t,i,j;
	cin>>t;
	//t=1;
	int counter1=0;
	while(t--)
	{
		counter1++;
		string a;
		cin>>a;
		int k;
		cin>>k;
		int count1=0;
		for(i=0;i<a.size();i++)
		{
			if(i+k-1>=a.size())
				break;	
			else if(a.at(i)=='-')
			{
				for(j=i;j<i+k;j++)
				{
					if(a.at(j)=='-')
						a.at(j)='+';
					else
						a.at(j)='-';
				}
				count1++;
			}
		//	cout<<a<<endl;
		}
		int flag=0;
		for(i=0;i<a.size();i++)
		{
			if(a.at(i)=='-')
				flag=1;
		}
		cout<<"Case #"<<counter1<<": ";
		if(flag==1)
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		else
			cout<<count1<<endl;	
		//print your final answer here
		//cout<<fixed<<setprecision(5)<<answer<<endl;
		//cout<<endl;	
	}	
}

