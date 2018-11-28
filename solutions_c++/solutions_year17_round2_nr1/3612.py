#include<bits/stdc++.h>
//#include<map>
using namespace std;

class Cruise
{
	private:
	int t, n;
	//map<int, int>* horse;
	long long int d;
	double pos;
	double speed;
	double weight;
	//int last
	
	
	public:
	Cruise(int x)
	{
		weight = -1;
		t = x;
		cin>>d>>n;
		//horse = new list<int>[n];
		//pos = new int[n];
		//speed = new int[n];
		//double* weight = new double[n];
		
		for(int i=0; i<n; ++i)
		{
			cin>>pos>>speed;
			//weight[i] = (d-pos[i])/speed[i];
			if(weight == -1 || weight<(d-pos)/speed)
			{
				weight = (d-pos)/speed;
			}
		}
		
		cout<<"Case #"<<t<<": "<<fixed<<showpoint<<setprecision(6)<<(double)(d/weight)<<"\n";
	}
};

int main()
{
	int t;
	cin>>t;
	Cruise** obj = new Cruise*[t];
	for(int i=0; i<t; ++i)
		obj[i] = new Cruise(i+1);
}