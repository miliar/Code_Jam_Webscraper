#include <iostream>
#include <fstream>
#include <stdio.h>
#include <iomanip>

using namespace std;

int main()
{
    ofstream outfile;
    int t;
    int d,n;
    int k,s;
    double max;
    double temp;
    int p;
    double speed;
    scanf("%d",&t);
    outfile.open("out.txt");
    for(int i=0;i<t;i++)
    {
    	scanf("%d",&d);
    	scanf("%d",&n);
    	max = 0;
    	for(int j=0;j<n;j++)
    	{
    		scanf("%d",&k);
    		scanf("%d",&s);
    		temp = ((double)(d-k))/(double)s;
    		if(max<temp)
    		{
    			max = temp;
    		}
    	}
    	speed = ((double)d)/max;
    	p = i+1;
    	outfile <<"Case #"<<p<<": "<<fixed<<setprecision(10)<<speed<<endl;
    	printf("%lf\n",speed);
    }
   outfile.close();
	return 0;
}