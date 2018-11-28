//If you are reading this then you are at wrong place.
#include<bits/stdc++.h>
#define mod 1000000007
using namespace std;
int main()
{
	//your code goes here
	//input for the testcase 
	ifstream cin("B-small-attempt4.in");
	ofstream cout("BS.txt");	
//	ios_base::sync_with_stdio(0);
//    cin.tie(0);
//    cout.tie(0);	
	int t,i,j;
	cin>>t;
	//t=1;
	int counter1=0;
	while(t--)
	{
		counter1++;
		string a;
		cin>>a;
		string b=a;
		sort(b.begin(),b.end());
		if(a==b)
		{
			cout<<"Case #"<<counter1<<": ";
			cout<<a<<endl;
		}
		else
		{
			int check=0;
			for(i=0;i<a.length();i++)
			{
				if(check==1)
				{
					a[i]='9';
				}
				if( (a[i]-'0' >= a[i+1]-'0' )  && check==0 )
				{
					a.at(i)=(char)((a[i]-1));
					check=1;
				}
			}
			cout<<"Case #"<<counter1<<": ";
			//counter1++;
			check=0;
			for(i=0;i<a.length();i++)
			{
				if(a.at(i)=='0' && check==0)
					continue;
				else
				{
					check=1;
					cout<<a.at(i);
				}
			}
			cout<<endl;
		}
		//	counter1++;
		//cout<<"Case #"<<counter1<<" ";
		//print your final answer here
		//cout<<fixed<<setprecision(5)<<answer<<endl;
		//cout<<endl;	
	}	
}

