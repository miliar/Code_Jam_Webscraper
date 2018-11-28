#include <iostream>
#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int testcases;
	cin>>testcases;
	int casecon=1;
	while(testcases--)
	{
            long long destination;
            int numhorse;
            cin>>destination>>numhorse;

            long long arrcordinate[numhorse];
            long long arrspeed[numhorse];

            for(int i=0;i<numhorse;i++)
            {
            	cin>>arrcordinate[i];
            	cin>>arrspeed[i];
            }

            double timrequired=-1;
             for(int i=0;i<numhorse;i++)
             {
             	double value=double(destination- arrcordinate[i] )/arrspeed[i];
             	if(value>=timrequired)
             	{
             		timrequired=value;
             	}
             }

             cout<<"Case #"<<casecon<<": "<<fixed<<setprecision(6)<<(destination/timrequired)<<endl;
              

		casecon++;
	}
	return 0;
}