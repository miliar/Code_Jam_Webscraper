#include<iostream>
using namespace std;
int main()
{
	int t,r,c;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int p,row[30],col[30],f_row[30],f=0;
		char cake1[30],cake[30][30],piece[30],dcake[30][30];
		cin>>r>>c;
		for(int rr=0;rr<r;rr++)
		{
			cin>>cake1;
			p=0;
			for(int cc=0;cc<c;cc++)
			{
				cake[rr][cc]=cake1[cc];
				dcake[rr][cc]=cake1[cc];
				if(cake[rr][cc]!='?')
				{
					piece[p]=cake[rr][cc];
					row[p]=rr;
					col[p++]=cc;
				}
			}
			
			int pp,colm;
			for(pp=0,colm=0;pp<p;pp++)
			{
				for(;colm<=col[pp];colm++)
				{
					cake[rr][colm]=piece[pp];
				}
			}
			for(;colm<c;colm++)
			{
				if(p>0)
				cake[rr][colm]=piece[p-1];
			}
			if(cake[rr][0]!='?')
				f_row[f++]=rr;
			
		}
			cout<<"Case #"<<i<<":"<<endl;
			/*for(int rr1=0;rr1<r;rr1++)
			{
				
				for(int cc1=0;cc1<c;cc1++)
				{
					cout<<dcake[rr1][cc1];
				}
				cout<<endl;
			}*/
		//	cout<<"------------\n";
		for(int rr=0,q=0;rr<r;rr++)
		{
			if(cake[rr][0]!='?')
			{
				q=(q+1<f?q+1:q);
			}
			
			for(int cc=0;cc<c;cc++)
			{
				if(cake[rr][0]!='?')
				{
					
					cout<<cake[rr][cc];
					//cout<<" q: "<<q;	
					
				}
				else
				{
					
					cout<<cake[f_row[q]][cc];
				}
				
			}
				cout<<endl;
		}
			
	}
		
}

