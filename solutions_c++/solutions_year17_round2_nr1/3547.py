#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	
        int c=1;
	while(t--)
	{
	double  D;
	int N;
        cin>>D;
	cin>>N;
	double S[N];
	double K[N];
	for (int i=0;i<N;i++)
	{
		cin>>K[i];
		cin>>S[i];
	}
	double time=0,speed;
	for(int i=0;i<N;i++)
	{
	float ti;	
	double dist=D-K[i];
	ti=dist/S[i];
	if(time<ti)
		time=ti;
	}
	speed=D/time;
	cout<<"Case #"<< c <<": ";
	c++;
	printf("%0.6f\n",speed);
	}
return 0;
}
