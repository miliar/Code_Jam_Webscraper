#include<iostream>
using namespace std;
typedef long long LL;
void print9s(LL N)
{
	if(N==0)
		return;
	string nines = "9";
	while(true)
		if(nines.length()*2<=N)
			nines = nines + nines;
		else
			break;
	cout<<nines;
	print9s( N - nines.length() );
}
int main()
{	
	LL T;
	cin >> T;
	for(LL t = 1; t <= T; t++)
	{
		
		cout<<"Case #"<<t<<": ";
		string N;
		cin >> N;
		bool flagged = false;
		
		for(LL pos = 0; pos < N.length() - 1; pos++)
		{
			if(N[pos]>N[pos+1])
			{
				LL fixAt = pos;
				while(N[fixAt] > N[fixAt+1] )
				{
					N[fixAt] = N[fixAt] - 1;
					N[fixAt+1] = '9';
					if(fixAt==0)
						break;
					fixAt--;
					
				}
				if(N[0]=='0')
					cout<<N.substr(1,pos);
				else
					cout<<N.substr(0,pos+1);
				
				print9s(N.length()-pos-1);
				flagged = true;
				break;
			}
		}
		
		if(!flagged)
			cout<<N;
		cout<<endl;
	}
	return 0;
}