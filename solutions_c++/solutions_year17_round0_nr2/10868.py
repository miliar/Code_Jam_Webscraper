#include <iostream>
#include <string>
using namespace std;

int main()
{
	FILE *F;
	FILE *Q;

	F=fopen("inP.txt","r");
	Q=fopen("outP.txt","w");
	int n;
	fscanf(F,"%d",&n);
	int k=1;
	while(n>0)
	{
		

		long int m;
		//cout<<"getting m"<<endl;
		fscanf(F,"%ld",&m);

		long int lnum=m;
		long int dude=1;

		while( lnum>0 )
		{
			if( lnum%10 >= ((lnum/10) % 10))
			{
				lnum/=10;
			}
			else
			{
				lnum=m-dude;
				dude++;
			}
		}

		
		fprintf(Q,"Case #%d: %ld\n",k,m-dude+1);
		


		n--;
		k++;
	}
	
	system("pause");
	return 0;


}


/*
cout<<" here 1"<<endl;
	while(n>0)
	{
		p = (int*) malloc( 1* sizeof(int) );

		long int m;
		cout<<"getting m"<<endl;
		cin>>m;


		//cout<<" here 2"<<endl;

		long int lnum=0;
		for(long int i=1;i<=m;i++)
		{
			//cout<<" b while"<<endl;
			int j=i;
			while(j>1)
			{
			p =(int*)realloc(   p,(lnum+1 +1)*sizeof(int)   );
			p[lnum]=j%10;
			//cout<<"i%10"<<j%10<<endl;
			//cout<<lnum<<endl;
			//cout<<" guess here"<<endl;
			

			//cout<<" here 3"<<endl;

			j/=10;
			lnum++;
			}

			cout<<" here 4"<<endl;
		}


		//cout<<"here"<<endl;
		//lnum =s.length()-1;

		lnum--;
		while( p[lnum]<=p[lnum-1]&& lnum>=1 )
		{
			//cout<<"stuck"<<endl;
			lnum--;
		}

		long int fnum=lnum;
		while( p[fnum]>=p[fnum-1]&& fnum>=1 )
		{
			cout<<"aint stuck"<<endl;
			fnum--;
		}


		cout<<"Case #"<<":"<<n;
		for(int i=fnum-1; i<=lnum-1; i++)
		{
			cout<<p[i];
		}
		cout<<endl;
		n--;
	}
*/
