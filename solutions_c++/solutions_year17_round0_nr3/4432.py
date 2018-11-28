#include <bits/stdc++.h>

using namespace std;







 typedef long long ll;
 ll c=0;



vector <ll>  calc(ll n)
{
	 vector < ll > v;
ll a=0,b=0;
if(n%2)
	{
		

		v.push_back((n-1)/2);
		v.push_back((n-1)/2);



	}
	else if(!(n%2))
	{
		
	
		v.push_back((n+1)/2);
		v.push_back((n-1)/2);
	
	

	}

return  v;

}



//vector<vector<int> > v;

int main()
{
  int t;
  cin >>t;
 for(int j=0;j<t;j++)
  {
ll k,n;
ll count=1;
cin >> n>>k;
c =k;
 vector<ll > v1=calc(n);
 vector <ll >v2;
 	c=c-1;
 	if (!c)
	{
		cout <<"Case #"<<j+1<<": "<<v1[0]<<" "<<v1[1]<<endl;
	}
while(c)
{

	v2.clear();

	for(int i =0;i<v1.size();i++)
		{
			
			v2.push_back(calc(v1[i])[0]);
			v2.push_back(calc(v1[i])[1]);
			//cout <<calc(v1[i])[0]<<" "<<calc(v1[i])[1]<<" ";
		}
		//cout <<endl;
		if(c>(v2.size()/2))

				{
					sort(v2.rbegin(),v2.rend());
				
				c =c -(v2.size()/2);
				//cout <<"\n"<<c<<" "<<v2.size()<<"\n";
				v1 = v2;
			}
			else
			{
				cout <<"Case #"<<j+1<<": "<<v2[2*c-2]<<" "<<v2[2*c-1]<<endl;
				c=0;
			}

	
		
		


}
  }

	return 0;
}