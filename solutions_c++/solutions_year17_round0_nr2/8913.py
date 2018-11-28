#include<iostream>
#include<vector>
#include<string>
#include<fstream>
using namespace std;
int main()
{
	//ofstream fout("C:\\rei\\Document.txt");
    ios_base::sync_with_stdio(false);
    int t;
	cin>>t;
	for(int ii=1;ii<=t;ii++)
	{
		int n;
		cin>>n;
		int maxxi=0;
		for(int j=0;j<=n;j++)
		{
			int p=j;
			int maxi=1e9;
			bool cc=1;
			while(p)
			{
				int broj=p%10;
				if(broj>maxi){
					cc=false;

				break;}
				maxi=broj;
				p/=10;
			}
			if(cc)
				maxxi=max(maxxi,j);
		}
		cout<<"Case #"<<ii<<": ";
			cout<<maxxi<<endl;
	}
    return 0;
}