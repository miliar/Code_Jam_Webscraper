#include <iostream>
#include <iomanip>
#include <map>
#include <cmath>
#include <cstring>
#include <queue>
using namespace std;

const long MAX=100;
const long smallinf=1<<30;
const long INF=smallinf*64*2;//10^9*N+1
long dist[MAX][MAX];
long minDist[MAX][MAX];
double availTime[MAX][MAX];
double minTime[MAX][MAX];

long N,Q;
double EI[MAX], SI[MAX];

int UK[MAX],VK[MAX];

int onecase()
{
	cin>>N>>Q;
	for(int i=0;i<N;i++)
		cin>>EI[i]>>SI[i];

	for(int i=0;i<N;i++)
		for(int j=0;j<N;j++)
			cin>>dist[i][j];
	for(int i=0;i<Q;i++)
		cin>>UK[i]>>VK[i];

	//step 1: calculate minDist pairs
	for(int i=0;i<N;i++)
		for(int j=0;j<N;j++)
		{
			if (dist[i][j]!=-1)
				minDist[i][j]=dist[i][j];
			else
				minDist[i][j]=INF;
		}
	for(int i=0;i<N;i++)
		minDist[i][i]=0;

	for(int t=0;t<N;t++)
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++)
				for(int k=0;k<N;k++)
					if(minDist[i][j]+minDist[j][k]<minDist[i][k])
						minDist[i][k]=minDist[i][j]+minDist[j][k];

	cerr<<"Min dist:"<<endl;
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			long d=minDist[i][j];
			if(d==INF)d=-1;
			cerr<<d<<",";
		}
		cerr<<endl;
	}


	//step 2: calculate availTime
	for(int i=0;i<N;i++)
		for(int j=0;j<N;j++){
			availTime[i][j]=INF;
			if(minDist[i][j]<=EI[i])//the horse can go!
				availTime[i][j]=minDist[i][j]/SI[i];
			minTime[i][j]=availTime[i][j];
		}

	cerr<<"avail time:"<<endl;
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			double d=availTime[i][j];
			if(d==INF)d=-1;
			cerr<<d<<",\t";
		}
		cerr<<endl;
	}

	//step 3: calculate minTime
	for(int t=0;t<N;t++)
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++)
				for(int k=0;k<N;k++)
					if(minTime[i][j]+minTime[j][k]<minTime[i][k])
						minTime[i][k]=minTime[i][j]+minTime[j][k];



	cerr<<"min time:"<<endl;
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			double d=minTime[i][j];
			if(d==INF)d=-1;
			cerr<<d<<",\t";
		}
		cerr<<endl;
	}
	cerr<<"output ans#: "<<endl;
	for(int i=0;i<Q;i++){
		cerr<<"pair="<<UK[i]<<"->"<<VK[i]<<endl;
		double hour=minTime[UK[i]-1][VK[i]-1];
		cout<<setprecision(9)<<hour<<" ";
	}
	cout<<endl;
	return 0;
}

int main(){
	//onecase();return 0;
	
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		//cerr<<"Case:"<<t<<endl;
		cout<<"Case #"<<t<<": ";
		onecase();
	}
	return 0;
}