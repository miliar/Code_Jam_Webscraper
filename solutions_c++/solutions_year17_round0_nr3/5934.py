#include <bits/stdc++.h>
using namespace std;
struct seats
{
	bool occupied;
	int ls;
	int rs;
};
seats s[1000009];

int main() 
{
		int T,t,n,k,maxi,mini,res,ansmax,ansmin,left,right;
		cin>>T;
		t=T;
		t=1;
		while(T--)
		{
			cin>>n>>k;
			for(int i=0;i<n+2;i++)
			{
				s[i].occupied=false;
				s[i].ls=i-1;
				s[i].rs=n-i;
			}
			s[0].occupied=true;s[n+1].occupied=true;
			int temp=n;
			    left=0;
				right=0;
				ansmax=0;
				ansmin=0;
			for(int i=0;i<k;i++)
			{
				maxi=INT_MIN;
			//	maxi1=INT_MIN;
				for(int j=1;j<=n;j++)
				{
					if(maxi<min(s[j].ls,s[j].rs) && s[j].occupied==false)
						{
						  //  cout<<"New maxi is at "<<j+1<<"  left and right  respectively "<<s[j].ls<<s[j].rs<<endl;
							maxi=min(s[j].ls,s[j].rs);
							res=j;

						}
					else if(maxi==min(s[j].ls,s[j].rs) && s[j].occupied==false)
					{
							if(max(s[j].ls,s[j].rs) > max(s[res].ls,s[res].rs))
							{
				 // cout<<"New maxi/maxi is at "<<j+1<<"  left and right  respectively "<<s[j].ls<<s[j].rs<<endl;

								res=j;
							}
					}
				}
				s[res].occupied=true;
				for(int a=1;a<=n;a++)
				{
				    left=0;right=0;
				for(int q=a-1;q>=0;q--)
				{
					if(s[q].occupied==false)
					left++;
					else
					break; 
				}
			//	cout<<left<<endl;
				for(int q=a+1;q<n+2;q++)
				{
					if(s[q].occupied==false)
					right++;
					else
					break; 
				}
				s[a].ls=left;
				s[a].rs=right;
				}
				//cout<<"The seat that is occupied is "<<res+1<<endl;
			}
			
				//cout<<right<<endl;
				ansmax=max(s[res].ls,s[res].rs);
				ansmin=min(s[res].ls,s[res].rs);
				cout<<"Case #"<<t<<": "<<ansmax<<" "<<ansmin<<endl;
				t++;
		}
}
