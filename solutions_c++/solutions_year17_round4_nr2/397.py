#include <bits/stdc++.h>

using namespace std;


int n, c, m;

int seats[1000];

long long  ticketsbougtbyperson[1000];

void read()
{

	cin>>n>>c>>m;

	for (int i = 0; i < n; ++i)
	{
		seats[i] = 0;
	}

	for (int i = 0; i < c; ++i)
	{
		ticketsbougtbyperson[i] = 0;
	}


	for (int i = 0; i < m; ++i)
	{
		int a, b;
		cin>>a>>b;
		seats[a-1]++;
		ticketsbougtbyperson[b-1]++;
	}


}



int solve()
{
	
	long long maks = 0;
	long long sum = 0;

	for (int i = 0; i < n; ++i)
	{
		sum+=seats[i];
		maks = max(maks, sum/(i+1) + (sum % (i+1) > 0) );
	}
	for (int i = 0; i < c; ++i)
	{
		maks = max(ticketsbougtbyperson[i], maks);
	}
	cout<<maks<<" ";
	long long reloc = 0;
	for (int i = 0; i < n; ++i)
	{
		if(seats[i]>maks)
			reloc+=seats[i]-maks;
	}
	cout<<reloc;
	return 0;

}



int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(0);


	int T;
	cin>>T;

	for (int t = 1; t <= T; ++t)
	{
		read();
		cout<<"Case #"<<t<<": ";solve(); cout<<"\n";
	}


	return 0;
}