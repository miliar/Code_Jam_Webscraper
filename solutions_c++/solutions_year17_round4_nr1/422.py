#include <bits/stdc++.h>

using namespace std;



int rest[10], p, n;

void read()
{

	cin>>n>>p;


	for (int i = 0; i < 10; ++i)
	{
		rest[i] = 0;
	}
	for (int i = 0; i < n; ++i)
	{
		int a;
		cin>>a;
		rest[a%p]++;
	}

}



int solve()
{
	int wynik = rest[0];


	bool again = true;
	
	if(p == 2)
	{
		while(again)
		{
			again = false;
			if(rest[1]>=2)
			{
				wynik+=1;
				rest[1]-=2;
				again= true;
			}
		}
	}
	if(p==3)
	{
		while(again)
		{
			again = false;
			if(rest[1] > 0 && rest[2] > 0 )
			{
				wynik++;
				rest[1]--;
				rest[2]--;
				again = true;
			}
			else
			if(rest[1]>=3)
			{
				wynik+=1;
				rest[1]-=3;
				again = true;
			}
			else
			if(rest[2]>=3)
			{
				wynik+=1;
				rest[2]-=3;
				again = true;
			}
			
		}
	}
	if(p==4)
	{
		while(again)
		{
			again = false;
			if( rest[2]>=2)
			{
				wynik+=1;
				rest[2]-=2;
				again = true;	
			}
			else
			if(rest[1]>0 && rest[3] > 0 )
			{
				wynik++;
				rest[1]--;
				rest[3]--;
				again = true;
			}
			else
			if(rest[2]>0 && rest[1] > 1 )
			{
				wynik++;
				rest[2]--;
				rest[1]-=2;
				again = true;
			}
			else
			if(rest[2]>0 && rest[3] > 1 )
			{
				wynik++;
				rest[2]--;
				rest[3]-=2;
				again = true;
			}
			else
			if(rest[1]>=4)
			{
				wynik+=1;
				rest[1]-=4;
				again = true;
			}
			else
			if(rest[3]>=4)
			{
				wynik+=1;
				rest[3]-=4;
				again = true;
			}
		}
	}
	//cout<<rest[0]<<" "<<rest[1]<<" "<<rest[2]<<" "<<rest[3]<<"\n";
	return wynik+min(1,rest[1]+rest[2]+rest[3]);

}



int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(0);


	int T;
	cin>>T;

	for (int t = 1; t <= T; ++t)
	{
		read();
		cout<<"Case #"<<t<<": "<<solve()<<"\n";
	}


	return 0;
}