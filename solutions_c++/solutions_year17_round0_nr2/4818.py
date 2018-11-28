#include <iostream>
using namespace std;

int main()
{
	long long n;

	int dig[19], T, t, m, j;

	cin >> T;

	for(int k=0; k<T ; k++)
	{

		cin >> n;
		m=0;

		while( n/10!=0 )
		{ 
			t = n%10;
			dig[m] = t;
			n=n/10;
			m++;
		}

		dig[m]=n;

		if(m==0)
		{

			cout<<"Case #"<<k+1<<": "<<n<<endl;	
			continue;
		}


		for(int i=m; i>0 ; )
		{
			j= i-1;

			while(dig[j]==dig[i])
			{

				if(j==0)
					break;

				j--;

				
			}

			if(dig[j]<dig[i])
			{
				t=i;
				break;
			}

			else
			{
				i = j;
			}

		t=i;

		}

		cout<<"Case #"<<k+1<<": ";

		if( t == 0)
		{

		for(int i = m ; i>=0 ; i--)
			cout<< dig[i];

		cout<<endl;
		}

		else
		{

			//cout<<"Hi!";

			for( int i=m; i > t ; i-- )
			{
				cout<< dig[i];
			}

			if(dig[t]!=1)
				cout<< dig[t]-1;

			for(int i=t-1; i>=0 ; i--)
				cout<<9;

			cout<<endl;

		}

/*

for(int i = 0; i <= m; i++)
	cout << dig[i]<< "   ";

cout<<"\n";

*/

	}

}