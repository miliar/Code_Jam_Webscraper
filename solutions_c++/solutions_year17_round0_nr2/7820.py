#include<bits/stdc++.h>

typedef long long LL;  
using namespace std;

#define fillchar(a, x) memset(a, x, sizeof(a))
#define MP make_pair
#define PB push_back
#define endl '\n'

const int M = (int)1e9+7;

int main()
{
//ios_base::sync_with_stdio(0); 
	cout.precision(15);
	cout.setf(ios::fixed);

	int t;
	cin >> t;

	for(int x=0;x<t;x++)
	{
		LL n;
		cin>>n;

		vector <int> v;

		while(n!=0)
		{
			v.PB(n%10);
			n /= 10;
		}

		reverse(v.begin(),v.end());
		n = v.size();

		int k = -1;

		for(int i=1;i<n;i++)
		{
			if(v[i]<v[i-1])
				{
					k = i;
					break;
				}
		}	

		if(k!=-1)
		{	
			for(int i=k+1;i<n;i++)
				v[i] = 9;

			while(k>0 && v[k]<v[k-1])
			{
				v[k] = 9;
				v[k-1]--;
				k--;
			}
		}
			
		cout<<"Case #"<<x+1<<": ";
		
		int i=0;

		while(v[i]==0) 	
			i++;
		
		for(;i<n;i++)	
			cout<<v[i];
		cout<<endl;
	}	


}
